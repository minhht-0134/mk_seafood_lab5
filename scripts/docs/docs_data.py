"""Dữ liệu dùng chung để sinh các tệp Markdown nộp bài (đọc backlog, issue-map, báo cáo SWP, nhật ký sprint)."""
import glob, importlib.util, json, re

BACKLOG = {}
for f in sorted(glob.glob('scripts/backlog/e-[0-9]*.json')):
    d = json.load(open(f, encoding='utf-8')); BACKLOG[d['epic']['key']] = d
MAP = json.load(open('scripts/github/issue-map.json'))
NUM = {k: v['number'] for k, v in MAP.items()}
_spec = importlib.util.spec_from_file_location('b2g', 'scripts/github/backlog-to-github.py')
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
special_value = _m.special_value
REPORT = json.loads(re.search(r'<script[^>]*type="application/json"[^>]*>(.*?)</script>',
                              open('reports/sun-estimate-mk-seafood-lab5.html').read(), re.S).group(1))
SWP = {int(r['issueRef'].split('#')[1]): r['finalSWP'] for r in REPORT['issues'] + REPORT['parents']}
LEAF = {int(r['issueRef'].split('#')[1]) for r in REPORT['issues']}
HOURS = lambda s: round(s * 3.5 * 2) / 2
ISSUES = {}  # khóa backlog -> dữ liệu issue kèm epic, số issue, điểm
for ek, d in BACKLOG.items():
    for i in d['issues']:
        n = NUM[i['key']]
        ISSUES[i['key']] = dict(i, n=n, epic=ek, leaf=n in LEAF, swp=SWP.get(n))
EPIC_NUM = {ek: NUM[ek] for ek in BACKLOG}
KEY_RE = re.compile(r'\bE\d\d-[A-Z]+-\d\d[a-z]?\b')


def num_text(s):
    """Thay mã khóa backlog bằng #số issue trên Project (khóa không có thật thì giữ nguyên)."""
    s = KEY_RE.sub(lambda m: f'#{NUM[m.group(0)]}' if m.group(0) in NUM else m.group(0), s)
    return re.sub(r'`(#\d+)`', r'\1', s)


def keys_in(s):
    return [k for k in dict.fromkeys(KEY_RE.findall(s)) if k in NUM]


def nums(ns, cap=8):
    ns = sorted(set(ns))
    return ', '.join(f'#{n}' for n in ns[:cap]) + (f' … (+{len(ns) - cap})' if len(ns) > cap else '')


def esc(s):
    return str(s).replace('|', '\\|').replace('\n', ' ')


def table(head, rows):
    return '\n'.join(['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
                     + ['| ' + ' | '.join(esc(c) for c in r) + ' |' for r in rows])


def cut(s, limit):
    """Cắt theo ranh giới câu/mệnh đề gần nhất dưới giới hạn."""
    if len(s) <= limit:
        return s
    h = s[:limit]
    p = max(h.rfind('. '), h.rfind('; '), h.rfind(', '))
    return (h[:p] if p > limit * 0.5 else h).rstrip(' ,;.') + ' …'
