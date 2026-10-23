#!/usr/bin/env python3
"""Ghi trường số lên Project #1 từ báo cáo HTML của sun-estimate, rồi đọc ngược đối chiếu theo lô.
  point            = finalSWP (lá), tổng con (cha)
  Giờ ước lượng    = SWP × 3,5 giờ (quy ước B6, D6), làm tròn 0,5 giờ
Dùng: python3 scripts/swp/write-project-numbers.py <point|hours> [--verify-only]"""
import json, re, subprocess, sys, time
REPORT, MAP = 'reports/sun-estimate-mk-seafood-lab5.html', 'scripts/github/issue-map.json'
FIELDS = {'point': ('point', lambda s: s), 'hours': ('Giờ ước lượng', lambda s: round(s * 3.5 * 2) / 2)}
mode = sys.argv[1]; fname, conv = FIELDS[mode]
v = json.loads(re.search(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>', open(REPORT).read(), re.S).group(1))
want = {int(r['issueRef'].split('#')[1]): conv(r['finalSWP']) for r in v['issues'] + v['parents']}
m = json.load(open(MAP)); by = {x['number']: x['item'] for x in m.values()}
def gql(q):
    for k in range(4):  # lỗi 5xx tạm thời của GitHub: thử lại
        r = subprocess.run(['gh', 'api', 'graphql', '-f', 'query=' + q], capture_output=True, text=True)
        if not r.returncode: return json.loads(r.stdout)['data']
        time.sleep(3 * (k + 1))
    raise RuntimeError(r.stderr.strip() or r.stdout.strip())
d = gql('query{user(login:"minhht-0134"){projectV2(number:1){id fields(first:40){nodes{... on ProjectV2Field{id name dataType}}}}}}')['user']['projectV2']
pid = d['id']; f = next(x for x in d['fields']['nodes'] if x.get('name') == fname); fid = f['id']
print('trường', fname, f['dataType'], '| mục', len(want), '| tổng', sum(want[n] for n in want if n in {int(r['issueRef'].split('#')[1]) for r in v['issues']}))
items = sorted(want.items())
if '--verify-only' not in sys.argv:
    for i in range(0, len(items), 20):
        q = 'mutation{' + ' '.join(f'a{n}:updateProjectV2ItemFieldValue(input:{{projectId:"{pid}",itemId:"{by[n]}",fieldId:"{fid}",value:{{number:{p}}}}}){{clientMutationId}}' for n, p in items[i:i+20]) + '}'
        gql(q); print('đã ghi', min(i + 20, len(items)), '/', len(items), flush=True); time.sleep(1)
bad, got = [], {}
for i in range(0, len(items), 50):
    ids = [by[n] for n, _ in items[i:i+50]]
    q = 'query{nodes(ids:[%s]){... on ProjectV2Item{id c:content{... on Issue{number}} v:fieldValueByName(name:"%s"){... on ProjectV2ItemFieldNumberValue{number}}}}}' % (','.join('"%s"' % x for x in ids), fname)
    for nd in gql(q)['nodes']:
        got[nd['c']['number']] = nd['v']['number'] if nd.get('v') else None
for n, w in items:
    if got.get(n) != w: bad.append((n, got.get(n), w))
leaf = {int(r['issueRef'].split('#')[1]) for r in v['issues']}
print('đối chiếu', len(got), 'mục | lệch', len(bad), bad[:5], '| tổng lá', sum(got[n] for n in leaf if got.get(n) is not None))
