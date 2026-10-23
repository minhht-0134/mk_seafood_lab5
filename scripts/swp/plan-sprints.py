#!/usr/bin/env python3
"""Xếp issue lá vào sprint (giả lập) theo phụ thuộc, sức chứa từng vai trò và thứ tự ưu tiên epic.
Ra scripts/swp/work/sprint-plan.json. Không ghi gì lên GitHub."""
import glob, json, re, sys
CAP = 56  # giờ thực mỗi người mỗi sprint (D7: 70 giờ × 80%)
ROLES = ['BE-1', 'BE-2', 'FE-1', 'QA-1']
PRIO = ['E-10', 'E-01', 'E-02', 'E-03', 'E-04', 'E-05', 'E-06', 'E-07', 'E-08', 'E-09', 'E-11']
N = int(sys.argv[1]) if len(sys.argv) > 1 else 2
v = json.loads(re.search(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', open('reports/sun-estimate-mk-seafood-lab5.html').read(), re.S).group(1))
m = json.load(open('scripts/github/issue-map.json'))
swp = {int(r['issueRef'].split('#')[1]): r['finalSWP'] for r in v['issues']}
nodes = {}
for f in sorted(glob.glob('scripts/backlog/e-[0-9]*.json')):
    for i in json.load(open(f))['issues']:
        n = m[i['key']]['number']
        if n in swp: nodes[i['key']] = {'key': i['key'], 'n': n, 'type': i['type'], 'epic': 'E-' + i['key'][1:3], 'deps': i.get('depends', []), 'swp': swp[n]}
# phụ thuộc vào issue cha: thay bằng mọi con lá của cha đó
kids = {}
for f in sorted(glob.glob('scripts/backlog/e-[0-9]*.json')):
    for i in json.load(open(f))['issues']:
        if i.get('parent'): kids.setdefault(i['parent'], []).append(i['key'])
def leaves(k): return [x for c in kids[k] for x in leaves(c)] if k in kids else [k]
for x in nodes.values():
    x['deps'] = sorted({l for d in x['deps'] for l in (leaves(d) if d in kids else [d]) if l in nodes and l != x['key']})
role = lambda x: 'FE-1' if x['type'] == 'fe' else 'QA-1' if x['type'] in ('qa', 'clarify') else None  # clarify: phân tích nghiệp vụ, QA-1 nhận
done, plan, load = set(), {}, {}
ch = {}
for x in nodes.values():
    for d in x['deps']: ch.setdefault(d, []).append(x['key'])
def descs(k, seen=None):
    seen = set() if seen is None else seen
    for c in ch.get(k, []):
        if c not in seen: seen.add(c); descs(c, seen)
    return seen
for x in nodes.values(): x['desc'] = len(descs(x['key']))
# ưu tiên: nhiều việc phía sau phụ thuộc vào trước (đường găng), rồi epic, rồi mã
order = sorted(nodes.values(), key=lambda x: (-x['desc'], PRIO.index(x['epic']), x['key']))
for s in range(1, N + 1):
    load = {r: 0.0 for r in ROLES}; added = []
    progress = True
    while progress:
        progress = False
        for x in order:
            if x['key'] in plan or any(d not in done and d not in added for d in x['deps']): continue
            h = x['swp'] * 3.5
            # ràng buộc: phụ thuộc cùng sprint chỉ chấp nhận nếu người làm khác nhau hoặc xếp sau (đơn giản: cho phép)
            r = role(x) or min(('BE-1', 'BE-2'), key=lambda q: load[q])
            if load[r] + h > CAP: continue
            load[r] += h; plan[x['key']] = {'sprint': s, 'owner': r, 'hours': h, 'swp': x['swp'], 'n': x['n'], 'epic': x['epic'], 'type': x['type']}; added.append(x['key']); progress = True
    done |= set(added)
    print('Sprint', s, '|', len(added), 'issue |', sum(plan[k]['swp'] for k in added), 'SWP |', {r: round(l, 1) for r, l in load.items()})
json.dump({'plan': plan, 'nodes': nodes}, open('scripts/swp/work/sprint-plan.json', 'w'), ensure_ascii=False)
