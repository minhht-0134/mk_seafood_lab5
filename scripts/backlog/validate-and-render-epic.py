#!/usr/bin/env python3
"""Kiểm cấu trúc một file backlog epic (JSON) và sinh bản markdown dễ đọc.

Dùng: python3 validate-and-render-epic.py <epic.json> [<out.md>]
Kiểm: trường bắt buộc (trước mọi truy cập), khóa duy nhất, parent/parent_of nhất quán hai chiều,
cây parent không vòng, phụ thuộc nội bộ tồn tại, không vòng phụ thuộc (kể cả qua container). Phụ thuộc sang epic khác (khóa E02-.. E11-..) chỉ được liệt kê.
"""
import collections
import json
import re
import sys

REQUIRED = ("key", "type", "title", "goal", "specs", "dod")


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate(data):
    issues = data["issues"]
    errors = []
    # 1. Schema trước mọi truy cập khác, báo theo vị trí để issue thiếu key vẫn được chỉ ra.
    for n, i in enumerate(issues):
        for f in REQUIRED:
            if not i.get(f):
                errors.append(f"issue #{n} ({i.get('key', 'THIẾU KEY')}): thiếu {f}")
    if errors:
        return errors, {}
    keys = [i["key"] for i in issues]
    dup = [k for k, n in collections.Counter(keys).items() if n > 1]
    if dup:
        errors.append(f"khóa trùng: {dup}")
    by_key = {i["key"]: i for i in issues}
    epic_prefix = data["epic"]["key"].replace("-", "")  # E-01 -> E01
    parents = {i["key"] for i in issues if "parent_of" in i}
    # 2. Cha-con phải nhất quán hai chiều.
    for i in issues:
        for c in i.get("parent_of", []):
            if c not in by_key:
                errors.append(f"{i['key']}: parent_of {c} không tồn tại")
            elif by_key[c].get("parent") != i["key"]:
                errors.append(f"{i['key']}: parent_of {c} nhưng {c} không trỏ parent về {i['key']}")
        if "parent" in i:
            par = by_key.get(i["parent"])
            if par is None or i["parent"] not in parents:
                errors.append(f"{i['key']}: parent {i['parent']} không có parent_of")
            elif i["key"] not in par.get("parent_of", []):
                errors.append(f"{i['key']}: trỏ parent {i['parent']} nhưng cha không liệt kê con này trong parent_of")
        if i["key"] in parents and i.get("depends"):
            errors.append(f"{i['key']}: issue cha không được có depends (khai ở issue lá)")
    # 3. Cây parent không có vòng.
    for i in issues:
        seen, cur = [], i["key"]
        while cur in by_key and "parent" in by_key[cur]:
            if cur in seen:
                errors.append("vòng parent: " + " > ".join(seen + [cur]))
                break
            seen.append(cur)
            cur = by_key[cur]["parent"]
    # 4. Phụ thuộc nội bộ phải tồn tại.
    for i in issues:
        for dep in i.get("depends", []):
            k = dep.split(" ")[0]
            if k.startswith(epic_prefix + "-") and k not in by_key:
                errors.append(f"{i['key']}: phụ thuộc nội bộ không tồn tại {k}")
    # 5. Đồ thị hoàn thành: depends khai báo, cộng cạnh container -> các con
    #    (container chỉ xong khi mọi con xong), nên lá phụ thuộc container chứa chính nó bị bắt.
    graph = {
        i["key"]: [d.split(" ")[0] for d in i.get("depends", []) if d.startswith(epic_prefix + "-")]
        for i in issues
    }
    for i in issues:
        for c in i.get("parent_of", []):
            if c in graph:
                graph[i["key"]].append(c)
    state = {}

    def dfs(node, path):
        if state.get(node) == 1:
            errors.append("vòng phụ thuộc: " + " > ".join(path + [node]))
            return
        if state.get(node) == 2:
            return
        state[node] = 1
        for nxt in graph.get(node, []):
            if nxt in graph:
                dfs(nxt, path + [node])
        state[node] = 2

    for n in graph:
        dfs(n, [])
    leaves = [i for i in issues if i["key"] not in parents]
    summary = {
        "tổng": len(issues),
        "cha": len(parents),
        "lá": len(leaves),
        "lá theo loại": dict(collections.Counter(i["type"] for i in leaves)),
        "phụ thuộc ngoài epic": sorted(
            {d for i in issues for d in i.get("depends", []) if not d.startswith(epic_prefix + "-")}
        ),
    }
    return errors, summary


def render(data):
    issues = data["issues"]
    by_key = {i["key"]: i for i in issues}
    e = data["epic"]

    def dep_text(i):
        return ", ".join(x.split(" ")[0] for x in i.get("depends", [])) or "—"

    def row(i, indent=""):
        return f"| {indent}{i['key']} | {i['type']} | {i['title']} | {i.get('special', '—')} | {dep_text(i)} |"

    out = [
        f"# {e['title']}: bản đọc để duyệt\n",
        "> Sinh tự động từ file JSON nguồn. Sửa ở JSON rồi sinh lại, không sửa tay file này.\n",
        f"**Mục tiêu epic:** {e['goal']}\n",
        "**Ngoài phạm vi:** " + "; ".join(e["out_of_scope"]) + "\n",
        "## Tổng quan\n",
        "| Khóa | Loại | Tên | Đặc thù | Phụ thuộc |",
        "|---|---|---|---|---|",
    ]
    for i in issues:
        if "parent" in i:
            continue
        out.append(row(i))
        for c in i.get("parent_of", []):
            out.append(row(by_key[c], "↳ "))
    out.append("\n## Chi tiết từng issue\n")
    for i in issues:
        out.append(f"### {i['key']}: {i['title']}")
        meta = f"Loại: {i['type']}"
        if "parent" in i:
            meta += f" · Thuộc: {i['parent']}"
        if i.get("special"):
            meta += f" · Ràng buộc đặc thù: {i['special']}"
        out.append(meta + "\n")
        out.append(f"**Mục tiêu:** {i['goal']}\n")
        out.append("**Tham chiếu spec:** " + "; ".join(i["specs"]) + "\n")
        out.append("**Định nghĩa xong:**")
        out += [f"- [ ] {x}" for x in i["dod"]]
        if i.get("depends"):
            out.append("\n**Phụ thuộc:** " + "; ".join(i["depends"]))
        out.append("")
    return "\n".join(out)


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    data = load(sys.argv[1])
    errors, summary = validate(data)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if errors:
        print("LỖI:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print("Cấu trúc hợp lệ")
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w", encoding="utf-8") as f:
            f.write(render(data))
        print("Đã sinh", sys.argv[2])


if __name__ == "__main__":
    main()
