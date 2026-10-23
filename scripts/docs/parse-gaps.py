"""Tách bảng chỗ hở từ notes/e-*-review.md (nháp nội bộ) thành scripts/docs/gaps.json."""
import re,glob,json,collections
rows=[]
for f in sorted(glob.glob('notes/e-[0-9]*-review.md')):
    ep='E-'+re.search(r'e-(\d\d)',f).group(1)
    txt=open(f).read()
    sec=re.search(r'## Chỗ hở.*?\n(.*?)(?=\n## )',txt,re.S)
    if not sec: print('không có mục',f);continue
    for l in sec.group(1).splitlines():
        if not l.startswith('|') or l.startswith('|---') or l.startswith('| #'): continue
        c=[x.strip() for x in l.strip().strip('|').split(' | ')]
        if len(c)<4: print('lệch cột',f,l[:80]);continue
        rows.append({'epic':ep,'n':c[0],'spec':c[1],'gap':c[2],'xl':' | '.join(c[3:])})
print(len(rows))
def kind(x):
    x=x.lower()
    if x.startswith('tạo issue làm rõ'): return 'clarify'
    if 'sửa thiết kế' in x[:80]: return 'fix'
    if x.startswith('giả định'): return 'assume'
    if x.startswith('để mở'): return 'open'
    return 'other'
cnt=collections.Counter(kind(r['xl']) for r in rows);print(cnt)
for r in rows:
    r['kind']=kind(r['xl'])
print([ (r['epic'],r['n'],r['xl'][:90]) for r in rows if r['kind']=='other'][:20])
json.dump(rows,open('scripts/docs/gaps.json','w'),ensure_ascii=False,indent=1)
