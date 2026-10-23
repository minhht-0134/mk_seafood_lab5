#!/usr/bin/env python3
"""Lập kế hoạch Sprint 2 sau khi Sprint 1 chạy xong (giả lập): việc chưa xong ở Sprint 1 chiếm sức chứa trước,
việc mới chỉ được chọn khi mọi phụ thuộc đã Done. Ra scripts/swp/work/sprint-2-plan.json. Không ghi gì lên GitHub."""
import json
CAP = 56
D = json.load(open('scripts/swp/work/sprint-plan.json')); P, N = D['plan'], D['nodes']
S = json.load(open('scripts/swp/work/sprint-1-simulation.json'))
done = {i['key'] for i in S['items'] if i['status'] == 'Done'}
left = [i for i in S['items'] if i['status'] != 'Done']
load = {'BE-1': 0.0, 'BE-2': 0.0, 'FE-1': 0.0, 'QA-1': 0.0}
for i in left:  # giờ còn lại ≈ giờ kế hoạch trừ giờ đã làm
    load[i['owner']] += max(0.0, P[i['key']]['hours'] - i.get('actual_hours', 0.0))
role = lambda x: 'FE-1' if x['type'] == 'fe' else 'QA-1' if x['type'] in ('qa', 'clarify') else None
plan = {}
for x in sorted(N.values(), key=lambda x: (-x['desc'], x['key'])):
    if x['key'] in done or x['key'] in P and P[x['key']]['sprint'] == 1: continue
    if any(d not in done for d in x['deps']): continue
    h = x['swp'] * 3.5; r = role(x) or min(('BE-1', 'BE-2'), key=lambda q: load[q])
    if load[r] + h > CAP: continue
    load[r] += h; plan[x['key']] = {'owner': r, 'hours': h, 'swp': x['swp'], 'n': x['n']}
json.dump({'plan': plan, 'carry_over': [i['key'] for i in left], 'load': load}, open('scripts/swp/work/sprint-2-plan.json', 'w'), ensure_ascii=False, indent=1)
print('Sprint 2:', len(plan), 'issue mới |', sum(v['swp'] for v in plan.values()), 'SWP | tải', {k: round(v, 1) for k, v in load.items()}, '| chuyển sang:', [i['key'] for i in left])
for k, v in plan.items(): print(' ', v['owner'], k, v['swp'])
