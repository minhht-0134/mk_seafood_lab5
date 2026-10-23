#!/usr/bin/env python3
"""Đọc (chỉ đọc) 404 issue từ repo + trường Project, chuẩn hóa cho tkm:sun-estimate.
Ra: file JSON ở đường dẫn truyền vào (mặc định scripts/swp/work/candidates.json, thư mục work/ không đẩy lên repo)."""
import json, subprocess, sys, os
Q = '''query($endCursor:String){repository(owner:"minhht-0134",name:"mk_seafood_lab5"){issues(first:50,after:$endCursor,orderBy:{field:CREATED_AT,direction:ASC}){
pageInfo{hasNextPage endCursor} nodes{number url title body state labels(first:10){nodes{name}} parent{number}
projectItems(first:3){nodes{fieldValueByName(name:"Loại"){... on ProjectV2ItemFieldSingleSelectValue{name}}}}}}}}'''
out = subprocess.run(['gh', 'api', 'graphql', '--paginate', '-f', 'query=' + Q, '--jq',
    '.data.repository.issues.nodes[]|@json'], capture_output=True, text=True, check=True).stdout
rows = [json.loads(l) for l in out.splitlines() if l.strip()]
res = []
for r in rows:
    labels = sorted(n['name'] for n in r['labels']['nodes'])
    res.append({'sourceType': 'github', 'issueRef': f"minhht-0134/mk_seafood_lab5#{r['number']}", 'num': r['number'],
                'url': r['url'], 'title': r['title'], 'body': r['body'], 'labels': labels, 'state': r['state'].lower(),
                'parentNum': (r['parent'] or {}).get('number'), 'status': 'Todo'})
dst = sys.argv[1] if len(sys.argv) > 1 else 'scripts/swp/work/candidates.json'
os.makedirs(os.path.dirname(dst), exist_ok=True)
json.dump(res, open(dst, 'w'), ensure_ascii=False, indent=1)
print(len(res), 'issue;', sum(1 for r in res if r['parentNum']), 'có cha')
