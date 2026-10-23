#!/usr/bin/env python3
"""Ghi Iteration, Người phụ trách (giả định), Status lên Project #1 theo kết quả giả lập (scripts/swp/sprint-1-simulation.json
và sprint-2-plan.json). Không đóng issue. Chạy lại an toàn. Ra cuối: đọc ngược đối chiếu."""
import json, subprocess, time
S1 = json.load(open('scripts/swp/sprint-1-simulation.json')); S2 = json.load(open('scripts/swp/sprint-2-plan.json'))
m = json.load(open('scripts/github/issue-map.json'))
def gql(q):
    for k in range(4):
        r = subprocess.run(['gh', 'api', 'graphql', '-f', 'query=' + q], capture_output=True, text=True)
        if not r.returncode: return json.loads(r.stdout)['data']
        time.sleep(3 * (k + 1))
    raise RuntimeError(r.stderr.strip() or r.stdout.strip())
d = gql('query{user(login:"minhht-0134"){projectV2(number:1){id fields(first:40){nodes{... on ProjectV2Field{id name} ... on ProjectV2SingleSelectField{id name options{id name}} ... on ProjectV2IterationField{id name configuration{iterations{id title}}}}}}}}')['user']['projectV2']
pid = d['id']; F = {f['name']: f for f in d['fields']['nodes'] if f.get('name')}
opt = lambda f, n: next(o['id'] for o in F[f]['options'] if o['name'] == n)
itr = {i['title']: i['id'] for i in F['Iteration']['configuration']['iterations']}
rows = [(i['key'], 'Sprint 1', i['owner'], i['status']) for i in S1['items']] + [(k, 'Sprint 2', v['owner'], 'Todo') for k, v in S2['plan'].items()]
def mut(a, key, item, field, val): return f'{a}:updateProjectV2ItemFieldValue(input:{{projectId:"{pid}",itemId:"{item}",fieldId:"{F[field]["id"]}",value:{val}}}){{clientMutationId}}'
for i in range(0, len(rows), 6):
    parts = []
    for j, (k, sp, ow, st) in enumerate(rows[i:i+6]):
        it = m[k]['item']; a = f'a{i+j}'
        parts += [mut(a + 'i', k, it, 'Iteration', '{iterationId:"%s"}' % itr[sp]),
                  mut(a + 'o', k, it, 'Người phụ trách (giả định)', '{singleSelectOptionId:"%s"}' % opt('Người phụ trách (giả định)', ow)),
                  mut(a + 's', k, it, 'Status', '{singleSelectOptionId:"%s"}' % opt('Status', st))]
    gql('mutation{' + ' '.join(parts) + '}'); print('đã ghi', min(i + 6, len(rows)), '/', len(rows), flush=True); time.sleep(1)
# đối chiếu ngược theo id mục
want = {m[k]['item']: (sp, ow, st) for k, sp, ow, st in rows}; bad = 0; ids = list(want)
for i in range(0, len(ids), 40):
    q = 'query{nodes(ids:[%s]){... on ProjectV2Item{id it:fieldValueByName(name:"Iteration"){... on ProjectV2ItemFieldIterationValue{title}} ow:fieldValueByName(name:"Người phụ trách (giả định)"){... on ProjectV2ItemFieldSingleSelectValue{name}} st:fieldValueByName(name:"Status"){... on ProjectV2ItemFieldSingleSelectValue{name}}}}}' % ','.join('"%s"' % x for x in ids[i:i+40])
    for nd in gql(q)['nodes']:
        if (nd['it'] and nd['it']['title'], nd['ow'] and nd['ow']['name'], nd['st'] and nd['st']['name']) != want[nd['id']]: bad += 1
print('đối chiếu', len(ids), 'mục | lệch', bad)
