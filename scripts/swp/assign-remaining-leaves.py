#!/usr/bin/env python3
"""Gán assignee GitHub (minhht-0134) cho các issue lá chưa nằm trong Sprint 1/2. Chạy lại an toàn."""
import json, re, subprocess, time
v = json.loads(re.search(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', open('reports/sun-estimate-mk-seafood-lab5.html').read(), re.S).group(1))
leaves = {int(r['issueRef'].split('#')[1]) for r in v['issues']}
m = json.load(open('scripts/github/issue-map.json')); key = {x['number']: k for k, x in m.items()}
s1 = {i['key'] for i in json.load(open('scripts/swp/sprint-1-simulation.json'))['items']}; s2 = set(json.load(open('scripts/swp/sprint-2-plan.json'))['plan'])
todo = sorted(n for n in leaves if key[n] not in s1 | s2)
print('cần gán', len(todo), flush=True)
for i, n in enumerate(todo, 1):
    for k in range(4):
        r = subprocess.run(['gh', 'api', '-X', 'POST', f'repos/minhht-0134/mk_seafood_lab5/issues/{n}/assignees', '-f', 'assignees[]=minhht-0134', '--silent'], capture_output=True, text=True)
        if not r.returncode: break
        time.sleep(3 * (k + 1))
    else: raise SystemExit(f'lỗi #{n}: {r.stderr}')
    if i % 25 == 0: print('đã gán', i, '/', len(todo), flush=True)
    time.sleep(0.8)
print('xong', len(todo))
