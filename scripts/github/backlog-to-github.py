#!/usr/bin/env python3
"""Đưa backlog (scripts/backlog/e-*.json) lên GitHub: epic, issue, sub-issue, nhãn và trường Project.
Dùng: python3 scripts/github/backlog-to-github.py <lệnh> [--keys K1,K2 ...]
  labels   tạo nhãn trong repo
  create   tạo issue chưa có (theo --keys, mặc định tất cả), lưu số vào scripts/github/issue-map.json
  sync     dựng lại thân issue (kèm số #phụ thuộc), nối sub-issue, đặt trường Project cho issue đã tạo
Chạy lại an toàn: issue đã có trong issue-map.json không bị tạo lại."""
import glob, json, os, subprocess, sys, time

OWNER, REPO, PROJECT = 'minhht-0134', 'mk_seafood_lab5', 1
MAP = os.path.join(os.path.dirname(__file__), 'issue-map.json')
SPECIAL = [  # (từ khóa trong nhãn special, giá trị trường Nhóm đặc thù), thứ tự ưu tiên
    ('di trú', 'Di trú dữ liệu'), ('audit bất biến', 'Audit bất biến'), ('sửa sau chốt', 'Sửa sau chốt'),
    ('締め再開', '締め再開 hai người'), ('hai người', '締め再開 hai người'), ('締め chốt sổ', '締め chốt sổ'),
    ('業務規程', '業務規程 có phiên bản'), ('許可/承認', '許可 và 承認'), ('失効', '許可 và 承認'),
    ('căn cứ chờ', '許可 và 承認'), ('参加上限', '参加上限'), ('khóa ngày hai lớp', 'Khóa ngày hai lớp'),
    ('outbox', 'Outbox và worker'), ('MFA', 'MFA'), ('offline', 'Offline'), ('完納奨励金', '完納奨励金')]


def gh(args, data=None):
    r = subprocess.run(['gh'] + args, input=data, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr.strip() or r.stdout.strip())
    return r.stdout


def api(method, path, body=None):
    out = gh(['api', '-X', method, path, '--input', '-'], json.dumps(body) if body is not None else None)
    return json.loads(out) if out.strip() else {}


def gql(query, **v):
    args = ['api', 'graphql', '-f', 'query=' + query]
    for k, x in v.items():
        args += ['-F' if isinstance(x, int) else '-f', f'{k}={x}']
    return json.loads(gh(args))['data']


def load_backlog():
    items = []
    for f in sorted(glob.glob('scripts/backlog/e-[0-9]*.json')):
        d = json.load(open(f, encoding='utf-8'))
        e = d['epic']
        items.append({'key': e['key'], 'type': 'epic', 'title': e['title'], 'epic': e['key'], 'goal': e['goal'],
                      'dod': ['Hoàn thành khi mọi issue con của epic xong'], 'specs': e.get('specs', []),
                      'out': e.get('out_of_scope', []), 'depends': [], 'parent': None, 'special': None})
        for i in d['issues']:
            ek = 'E-' + i['key'][1:3]
            parent = i.get('parent') or ek
            items.append({'key': i['key'], 'type': i['type'], 'title': i['title'], 'epic': ek, 'goal': i['goal'],
                          'dod': i['dod'], 'specs': i['specs'], 'out': [], 'depends': i.get('depends', []),
                          'parent': parent, 'special': i.get('special'), 'container': 'parent_of' in i})
    return items


def special_value(s):
    for k, v in SPECIAL:
        if s and k.lower() in s.lower():
            return v
    return 'Không'


def body(it, m):
    num = lambda k: f' (#{m[k]["number"]})' if k in m else ''
    out = [f'**Mã backlog:** `{it["key"]}` · **Loại:** {it["type"]} · **Epic:** {it["epic"]}{num(it["epic"]) if it["key"] != it["epic"] else ""}',
           '', '## Mục tiêu', it['goal'], '', '## Phạm vi và ngoài phạm vi']
    if it['type'] == 'epic':
        out += ['Trong phạm vi: ' + it['goal'], 'Ngoài phạm vi:'] + ['- ' + x for x in it['out']]
    else:
        out += ['Trong phạm vi: như mục tiêu ở trên.', f'Ngoài phạm vi: xem mục ngoài phạm vi của epic {it["epic"]}{num(it["epic"])}.']
    out += ['', '## Định nghĩa xong (DoD)'] + ['- [ ] ' + x for x in it['dod']]
    out += ['', '## Tham chiếu spec (theo mã, không chép nguyên văn)'] + ['- ' + x for x in it['specs']]
    out += ['', '## Phụ thuộc'] + (['- `' + k + '`' + num(k) for k in it['depends']] or ['- Không có'])
    if it['special']:
        out += ['', '## Nhóm đặc thù', f'{it["special"]} (nhóm: {special_value(it["special"])})']
    return '\n'.join(out)


def labels_of(it):
    ls = [it['type'], it['epic']] + (['issue-cha'] if it.get('container') else [])
    return ls + (['đặc-thù'] if special_value(it['special']) != 'Không' else [])


def cmd_labels():
    names = ['epic', 'doc', 'db', 'be', 'fe', 'job', 'qa', 'clarify', 'issue-cha', 'đặc-thù'] + [f'E-{n:02d}' for n in range(1, 12)]
    for n in names:
        gh(['label', 'create', n, '--repo', f'{OWNER}/{REPO}', '--force'])
    print('đã tạo', len(names), 'nhãn')


def cmd_create(items, keys):
    m = json.load(open(MAP)) if os.path.exists(MAP) else {}
    for it in items:
        if it['key'] in m or (keys and it['key'] not in keys):
            continue
        r = api('POST', f'repos/{OWNER}/{REPO}/issues',
                {'title': f'[{it["key"]}] {it["title"]}', 'body': body(it, m), 'labels': labels_of(it)})
        m[it['key']] = {'number': r['number'], 'node': r['node_id'], 'id': r['id']}
        json.dump(m, open(MAP, 'w'), ensure_ascii=False, indent=1)
        print('tạo', it['key'], '#' + str(r['number'])); time.sleep(1.2)


def project_ids():
    d = gql('query($o:String!,$n:Int!){user(login:$o){projectV2(number:$n){id fields(first:40){nodes{... on ProjectV2FieldCommon{id name} '
            '... on ProjectV2SingleSelectField{options{id name}}}}}}}', o=OWNER, n=PROJECT)['user']['projectV2']
    return d['id'], {f['name']: f for f in d['fields']['nodes']}


def cmd_sync(items, keys):
    m = json.load(open(MAP))
    pid, fl = project_ids()
    opt = lambda f, v: fl[f]['options'][[o['name'] for o in fl[f]['options']].index(v)]['id']
    for it in items:
        if it['key'] not in m or (keys and it['key'] not in keys):
            continue
        n = m[it['key']]['number']
        api('PATCH', f'repos/{OWNER}/{REPO}/issues/{n}', {'body': body(it, m)})
        if it['parent'] in m and not m[it['key']].get('linked'):
            try:
                api('POST', f'repos/{OWNER}/{REPO}/issues/{m[it["parent"]]["number"]}/sub_issues', {'sub_issue_id': m[it['key']]['id']})
            except RuntimeError as e:  # đã nối ở lần chạy trước dừng giữa chừng
                if 'duplicate sub-issues' not in str(e) and 'only have one parent' not in str(e):
                    raise
            m[it['key']]['linked'] = True
        if not m[it['key']].get('item'):
            q = 'mutation($p:ID!,$c:ID!){addProjectV2ItemById(input:{projectId:$p,contentId:$c}){item{id}}}'
            try:
                m[it['key']]['item'] = gql(q, p=pid, c=m[it['key']]['node'])['addProjectV2ItemById']['item']['id']
            except RuntimeError as e:  # đã có trong Project (lần chạy trước dừng giữa chừng): tra lại id mục
                if 'already exists' not in str(e):
                    raise
                r = gql('query($i:ID!){node(id:$i){... on Issue{projectItems(first:10){nodes{id project{id}}}}}}', i=m[it['key']]['node'])
                m[it['key']]['item'] = [x['id'] for x in r['node']['projectItems']['nodes'] if x['project']['id'] == pid][0]
        item = m[it['key']]['item']
        sets = [('Mã backlog', 'text', it['key']), ('Loại', 'opt', it['type']), ('Epic', 'opt', it['epic']),
                ('Nhóm đặc thù', 'opt', special_value(it['special'])), ('Status', 'opt', 'Todo')]
        parts = []
        for i, (f, kind, v) in enumerate(sets):
            val = '{text:"%s"}' % v if kind == 'text' else '{singleSelectOptionId:"%s"}' % opt(f, v)
            parts.append(f'a{i}:updateProjectV2ItemFieldValue(input:{{projectId:"{pid}",itemId:"{item}",fieldId:"{fl[f]["id"]}",value:{val}}}){{clientMutationId}}')
        gql('mutation{' + ' '.join(parts) + '}')
        json.dump(m, open(MAP, 'w'), ensure_ascii=False, indent=1)
        print('đồng bộ', it['key']); time.sleep(0.8)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    keys = set(sys.argv[sys.argv.index('--keys') + 1].split(',')) if '--keys' in sys.argv else None
    if cmd == 'labels': cmd_labels()
    elif cmd == 'create': cmd_create(load_backlog(), keys)
    elif cmd == 'sync': cmd_sync(load_backlog(), keys)
    else: print(__doc__)
