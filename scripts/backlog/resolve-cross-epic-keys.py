#!/usr/bin/env python3
"""Thay khóa tạm giữa các epic bằng khóa thật trong trường depends của mọi scripts/backlog/e-*.json
(theo bảng ánh xạ trong check-cross-epic-cycles.py). Giữ thứ tự, bỏ trùng, bỏ tham chiếu tới chính mình.
Dùng: python3 scripts/backlog/resolve-cross-epic-keys.py [--dry-run]"""
import glob, importlib.util, json, sys

spec = importlib.util.spec_from_file_location('chk', 'scripts/backlog/check-cross-epic-cycles.py')
chk = importlib.util.module_from_spec(spec); spec.loader.exec_module(chk)

files = sorted(glob.glob('scripts/backlog/e-[0-9]*.json'))
data = {f: json.load(open(f, encoding='utf-8')) for f in files}
real = {i['key'] for d in data.values() for i in d['issues']}
changed = unresolved = 0
for f, d in data.items():
    for i in d['issues']:
        out = []
        for dep in i.get('depends', []):
            r = chk.resolve(i['key'], dep, real)
            if r is None:
                unresolved += 1; print('CHƯA PHÂN GIẢI:', i['key'], '->', dep); r = [dep]
            for k in r:
                if k != i['key'] and k not in out:
                    out.append(k)
        if out != i.get('depends', []):
            changed += 1; i['depends'] = out
if '--dry-run' not in sys.argv and not unresolved:
    for f, d in data.items():
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('issue đổi depends:', changed, '| chưa phân giải:', unresolved)
sys.exit(1 if unresolved else 0)
