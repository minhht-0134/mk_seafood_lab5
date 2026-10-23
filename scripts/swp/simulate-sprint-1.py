#!/usr/bin/env python3
"""Giả lập kết quả Sprint 1 từ kế hoạch (sprint-plan.json): mỗi người làm tuần tự theo thứ tự kế hoạch,
5,6 giờ thực mỗi ngày; việc chỉ bắt đầu khi mọi phụ thuộc đã xong; vài việc chạy quá giờ hoặc bị chặn theo kịch bản.
Ra scripts/swp/sprint-1-simulation.json (nhật ký giả lập, đẩy lên repo cùng báo cáo). Không ghi gì lên GitHub."""
import json
D = json.load(open('scripts/swp/work/sprint-plan.json')); P, N = D['plan'], D['nodes']
DAYS = ['2026-11-02', '2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-09', '2026-11-10', '2026-11-11', '2026-11-12', '2026-11-13']
PER_DAY = 5.6
OVERRUN = {'E10-INF-01': 1.7, 'E10-DB-03': 1.4}   # kịch bản: dựng hạ tầng khung và bảng audit chậm hơn ước
BLOCKED = {'E09-CLR-02'}                           # kịch bản: chờ khách hàng trả lời
s1 = {k: v for k, v in P.items() if v['sprint'] == 1}
OVERRUN.clear(); OVERRUN.update({'E10-INF-01': 1.3})
t_done, status, log = {}, {}, []
for k in BLOCKED:
    status[k] = 'Blocked'; log.append({'key': k, 'owner': s1[k]['owner'], 'status': 'Blocked', 'note': 'Chờ khách hàng trả lời câu hỏi làm rõ'})
# lập lịch theo thời gian: mỗi người, tại thời điểm rảnh, chọn việc đủ điều kiện có nhiều việc phía sau nhất
free = {o: 0.0 for o in set(v['owner'] for v in s1.values())}
todo = {k for k in s1 if k not in BLOCKED}
while todo:
    best = None
    for o in free:
        mine = [k for k in todo if s1[k]['owner'] == o]
        if not mine: continue
        cand = []
        for k in mine:
            ds = [d for d in N[k]['deps'] if d in s1]
            if any(status.get(d) == 'Blocked' or (d in todo and d not in t_done and status.get(d) is None and d not in s1) for d in ds): continue
            if any(d in todo for d in ds) and not all(d in t_done for d in ds): continue  # phụ thuộc chưa lập lịch xong
            if any(status.get(d) == 'Blocked' for d in ds): continue
            start = max([free[o]] + [t_done[d] for d in ds])
            if start >= len(DAYS): continue  # hết sprint hoặc phụ thuộc chưa xong: không bắt đầu
            cand.append((start, -N[k]['desc'], k))
        if cand:
            c = min(cand)
            if best is None or c[0] < best[0][0]: best = (c, o)
    if best is None:
        for k in sorted(todo):
            status[k] = 'Todo'; log.append({'key': k, 'owner': s1[k]['owner'], 'status': 'Todo', 'note': 'Chờ việc phụ thuộc chưa xong'})
        break
    (start, _, k), o = best
    dur = s1[k]['hours'] * OVERRUN.get(k, 1.0) / PER_DAY; end = start + dur; free[o] = end; todo.discard(k)
    if end <= len(DAYS):
        status[k] = 'Done'; t_done[k] = end
        log.append({'key': k, 'owner': o, 'status': 'Done', 'done_on': DAYS[min(int(end - 1e-9), 9)], 'actual_hours': round(s1[k]['hours'] * OVERRUN.get(k, 1.0), 1)})
    else:
        status[k] = 'In Progress'; t_done[k] = 99
        log.append({'key': k, 'owner': o, 'status': 'In Progress', 'note': 'Chưa xong cuối sprint', 'actual_hours': round(max(0.0, len(DAYS) - start) * PER_DAY, 1)})
out = {'sprint': 'Sprint 1', 'from': DAYS[0], 'to': DAYS[-1], 'simulated': True, 'planned_swp': sum(v['swp'] for v in s1.values()),
       'planned_hours': sum(v['hours'] for v in s1.values()), 'scenario': {'overrun': OVERRUN, 'blocked': sorted(BLOCKED)}, 'items': log}
json.dump(out, open('scripts/swp/work/sprint-1-simulation.json', 'w'), ensure_ascii=False, indent=1)
import collections
c = collections.Counter(i['status'] for i in log); sw = collections.Counter()
for i in log: sw[i['status']] += s1[i['key']]['swp']
print(dict(c), dict(sw), 'kế hoạch', out['planned_swp'], 'SWP')
for i in log: print(i['status'], i['owner'], i['key'], s1[i['key']]['swp'], i.get('done_on', ''))
