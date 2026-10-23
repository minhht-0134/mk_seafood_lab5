#!/usr/bin/env python3
"""Sinh progress-report.md từ số liệu đọc trực tiếp trên GitHub Project #1 (trạng thái, Iteration, point, giờ)
và nhật ký giả lập Sprint 1 (ngày hoàn thành từng issue, chỉ dùng cho burndown). Chạy tại gốc repo."""
import collections, json, subprocess, sys, time
sys.path.insert(0, 'scripts/docs')
from docs_data import ISSUES, NUM, MAP, table, nums

FIELDS = 'st:fieldValueByName(name:"Status"){... on ProjectV2ItemFieldSingleSelectValue{name}} it:fieldValueByName(name:"Iteration"){... on ProjectV2ItemFieldIterationValue{title}} pt:fieldValueByName(name:"point"){... on ProjectV2ItemFieldNumberValue{number}} hr:fieldValueByName(name:"Giờ ước lượng"){... on ProjectV2ItemFieldNumberValue{number}} sg:fieldValueByName(name:"Nhóm đặc thù"){... on ProjectV2ItemFieldSingleSelectValue{name}} ow:fieldValueByName(name:"Người phụ trách (giả định)"){... on ProjectV2ItemFieldSingleSelectValue{name}}'


def gql(q):
    for k in range(4):
        r = subprocess.run(['gh', 'api', 'graphql', '-f', 'query=' + q], capture_output=True, text=True)
        if not r.returncode:
            return json.loads(r.stdout)['data']
        time.sleep(3 * (k + 1))
    raise RuntimeError(r.stderr)


def vi(x, dec=0):
    return f'{x:,.{dec}f}'.replace(',', '#').replace('.', ',').replace('#', '.')


leaves = {k: v for k, v in ISSUES.items() if v['leaf']}
P = {}  # khóa -> trường đọc từ Project
keys = list(leaves)
for i in range(0, len(keys), 40):
    part = keys[i:i + 40]
    q = 'query{nodes(ids:[%s]){... on ProjectV2Item{id %s}}}' % (','.join('"%s"' % MAP[k]['item'] for k in part), FIELDS)
    for k, nd in zip(part, gql(q)['nodes']):
        g = lambda f, key: (nd[f] or {}).get(key)
        P[k] = dict(status=g('st', 'name'), sprint=g('it', 'title'), swp=g('pt', 'number'), hours=g('hr', 'number'), group=g('sg', 'name'), owner=g('ow', 'name'))
sim = json.load(open('scripts/swp/sprint-1-simulation.json'))
S1 = {k: p for k, p in P.items() if p['sprint'] == 'Sprint 1'}
S2 = {k: p for k, p in P.items() if p['sprint'] == 'Sprint 2'}
assert len(S1) == 20 and all(abs(P[k]['swp'] - leaves[k]['swp']) < 1e-9 for k in P), 'Project lệch báo cáo'
agg = lambda d: (len(d), sum(p['swp'] for p in d.values()), sum(p['hours'] for p in d.values()))
by = lambda d, st: {k: p for k, p in d.items() if p['status'] == st}
tot_swp = sum(p['swp'] for p in P.values()); tot_h = sum(p['hours'] for p in P.values())
s1n, s1s, s1h = agg(S1)
done = by(S1, 'Done'); dn, ds, dh = agg(done)
actual = {i['key']: i.get('actual_hours', 0) for i in sim['items']}
o = []
o.append(f'''# Báo cáo tiến độ: Sprint 1

**Iteration:** Sprint 1, từ 02/11/2026 đến 13/11/2026 (hai tuần, 10 ngày làm việc).
**Lưu ý:** đây là sprint **giả lập** để minh họa theo dõi tiến độ; ngày tháng và kết quả do kịch bản đặt ra, không phải số liệu dự án thật. Số issue, điểm và giờ lấy trực tiếp từ GitHub Project của dự án.

**Cách đọc số liệu.** *SWP* là điểm khối lượng công việc chuẩn (một điểm khoảng nửa ngày công, 3,5 giờ). Dự án có {len(leaves)} đầu việc, tổng {vi(tot_swp)} điểm, khoảng {vi(tot_h, 1)} giờ. Nhóm làm việc giả định gồm bốn người (hai backend, một giao diện, một kiểm thử); sức chứa mỗi sprint khoảng 224 giờ, tức khoảng 64 điểm.

## 2. Trạng thái

**Sprint 1: cam kết {s1n} đầu việc, {s1s:.0f} điểm ({vi(s1h, 1)} giờ). Đã xong {dn} đầu việc, {ds:.0f} điểm ({vi(ds / s1s * 100)}%).**
''')
rows = []
notes = {'Done': 'Gồm 11 câu hỏi làm rõ nghiệp vụ, tài liệu thiết kế API của giao dịch, khung dự án và quy trình phát hành (#338), cấu trúc dữ liệu nền đầu tiên (#343) và một thành phần giao diện dùng chung',
         'In Progress': 'Cấu trúc dữ liệu nền thứ hai: hàm dùng chung cho các thao tác (#344); còn khoảng 2 ngày công',
         'Todo': 'Chưa bắt đầu vì phải chờ cấu trúc dữ liệu nền xong: bảng ngày nghiệp vụ (#345), bảng nhật ký kiểm toán (#348), mở rộng bảng tài khoản (#7)',
         'Blocked': 'Một câu hỏi làm rõ đang chờ khách hàng trả lời'}
for st in ('Done', 'In Progress', 'Blocked', 'Todo'):
    n, s, h = agg(by(S1, st))
    rows.append((st, n, f'{s:.0f}', vi(h, 1), notes[st]))
rows.append(('**Cộng Sprint 1**', f'**{s1n}**', f'**{s1s:.0f}**', f'**{vi(s1h, 1)}**', ''))
o.append(table(['Trạng thái', 'Số issue', 'Tổng SWP', 'Tổng giờ (kế hoạch)', 'Ghi chú'], rows))
rest = {k: p for k, p in P.items() if p['sprint'] is None}
o.append(f'''
**Toàn dự án ({len(leaves)} đầu việc).** Xong {dn} ({ds:.0f} điểm, {vi(ds / tot_swp * 100, 1)}% tổng điểm), đang làm 1, bị chặn 1, còn lại chưa bắt đầu. Sprint 2 đã xếp {len(S2)} đầu việc mới ({sum(p['swp'] for p in S2.values()):.0f} điểm), ngoài năm đầu việc chuyển tiếp từ Sprint 1 ({sum(p['swp'] for k, p in S1.items() if p['status'] != 'Done'):.0f} điểm). {len(rest)} đầu việc chưa xếp vào sprint nào.
''')
o.append('**Các hạng mục nghiệp vụ đặc thù đang ở đâu.**\n')
G = {'完納奨励金 (thưởng thanh toán đủ đúng hạn)': ['完納奨励金'], '業務規程 có phiên bản': ['業務規程'], '許可 và 承認': ['許可/承認', '失効', 'căn cứ chờ'],
     '参加上限 (hạn mức mua trong ngày)': ['参加上限'], '締め (chốt sổ) và không chốt khi còn pending': ['締め chốt sổ'], '締め再開 hai người duyệt': ['締め再開'],
     'Sửa sau chốt': ['sửa sau chốt'], 'Audit bất biến': ['audit bất biến'], 'Offline': ['offline'], 'Outbox và worker': ['outbox'], 'MFA': ['MFA'], 'Di trú dữ liệu': ['di trú']}
rows = []
for name, kws in G.items():
    ks = [k for k, v in leaves.items() if v.get('special') and any(w.lower() in v['special'].lower() for w in kws)]
    c = collections.Counter(P[k]['status'] for k in ks); sp = collections.Counter(P[k]['sprint'] or '-' for k in ks)
    started = [k for k in ks if P[k]['status'] != 'Todo' or P[k]['sprint']]
    where = 'chưa xếp sprint nào' if not started else 'đã xếp: ' + ', '.join(f'{v} ở {s}' for s, v in sorted(sp.items()) if s != '-')
    rows.append((name, len(ks), c['Done'], c['In Progress'] + c['Blocked'], c['Todo'], where))
o.append(table(['Hạng mục', 'Số đầu việc', 'Xong', 'Đang làm / bị chặn', 'Chưa làm', 'Vị trí'], rows))
o.append('\nPhần lớn hạng mục đặc thù chưa bắt đầu vì dựa trên nền tảng chung (bảng dữ liệu, kiểm soát truy cập, ghi nhật ký) mà Sprint 1 chỉ mới xong một phần. Đây là thứ tự làm có chủ đích, không phải chậm trễ riêng của từng hạng mục.\n')

# burndown theo ngày từ nhật ký giả lập, đối chiếu với tổng điểm xong trên Project
days = ['2026-11-02', '2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-09', '2026-11-10', '2026-11-11', '2026-11-12', '2026-11-13']
fin = collections.Counter()
for i in sim['items']:
    if i['status'] == 'Done':
        fin[i['done_on']] += P[i['key']]['swp']
assert sum(fin.values()) == ds, 'Nhật ký giả lập lệch Project'
rem = s1s; rows = []; bar = []
for d_i, d in enumerate(days):
    rem -= fin[d]; ideal = s1s * (1 - (d_i + 1) / 10)
    rows.append((f'{d[8:]}/{d[5:7]}', f'{ideal:.1f}'.replace('.', ','), f'{rem:.0f}', f'{fin[d]:.0f}' if fin[d] else '—'))
    bar.append(f'{d[8:]}/{d[5:7]} | {"█" * round(rem / 3)}{" " * (17 - round(rem / 3))}| còn {rem:.0f} (kế hoạch {ideal:.0f})')
o.append(f'''## 3. Burndown (điểm còn lại của Sprint 1)

Đường kế hoạch giảm đều từ {s1s:.0f} điểm xuống 0 sau 10 ngày. Số "còn lại" tính từ ngày hoàn thành từng đầu việc trong nhật ký giả lập, đối chiếu với trạng thái trên Project (tổng điểm xong khớp: {ds:.0f}).
''')
o.append(table(['Ngày', 'Kế hoạch còn', 'Thực tế còn', 'Xong trong ngày'], rows))
o.append('\n```text\n' + '\n'.join(bar) + '\n```\n')
o.append(f'''
**Lệch kế hoạch ở đâu.** Hai ngày đầu tiến độ sát kế hoạch vì chủ yếu là câu hỏi làm rõ và tài liệu, việc nhỏ và ít phụ thuộc. Từ 04/11 đường thực tế tụt dần: các việc nền tảng lớn phải làm nối tiếp nhau, và khung dự án với quy trình phát hành (5 điểm) làm quá giờ khoảng 30% nên chỉ xong ngày 06/11, trong khi các cấu trúc dữ liệu nền phải chờ nó. Khoảng cách rộng nhất ở cuối sprint: còn {s1s - ds:.0f} điểm chưa xong gồm cấu trúc dữ liệu nền thứ hai còn dở, ba đầu việc chưa bắt đầu và một câu hỏi làm rõ bị chặn chờ khách hàng.

**Dự báo.** Tốc độ Sprint 1 là {ds:.0f} điểm. Phần chưa xong không phải do thiếu người mà do việc phía sau chưa mở khóa (nhóm giao diện gần như không có việc: chỉ 10,5 giờ trong Sprint 1). Nếu từ Sprint 2 đạt sức chứa khoảng 64 điểm mỗi sprint, {vi(tot_swp - ds)} điểm còn lại cần khoảng {vi((tot_swp - ds) / 64)} sprint, tức khoảng 12 tháng. Con số này dài hơn lịch chín tháng phát triển ở bản ước lượng đầu; xem rủi ro 4.

## 4. Rủi ro trễ
''')
inf = NUM['E10-INF-01']; db2 = NUM['E10-DB-02']; clr = NUM['E09-CLR-02']
open_cl = sum(1 for k, v in leaves.items() if v['type'] == 'clarify' and P[k]['status'] != 'Done')
rows = [
    ('1. Cấu trúc dữ liệu nền chưa xong, ba đầu việc phụ thuộc chưa bắt đầu', f"#{db2} (đang làm), {nums([NUM[k] for k in ('E10-DB-03', 'E10-AUD-01', 'E01-DB-01')])}", 'Mốc bắt đầu làm nghiệp vụ đầu tiên (đăng nhập, quản lý người tham gia): lùi khoảng một sprint nếu không xử lý', 'Hoàn tất phần nền thứ hai trong tuần đầu Sprint 2; hai backend làm song song các phần độc lập nhau', 'BE-1 và BE-2, hạn 18/11/2026'),
    ('2. Một câu hỏi làm rõ bị chặn chờ khách hàng', f'#{clr}', 'Các báo cáo và xuất tệp (epic Báo cáo, 32 đầu việc phía sau): không chặn ngay nhưng sẽ chặn khi tới lượt', 'Nhắc khách trả lời; hết hạn thì làm theo phương án đề xuất ghi trong đầu việc và ghi rõ là giả định', 'PL-1, nhắc ngay 16/11, hạn 20/11/2026'),
    ('3. Nhóm giao diện thiếu việc (10,5 giờ trên 56 giờ trong Sprint 1, 0 giờ trong Sprint 2)', 'Các màn hình của mọi epic', 'Hiệu suất nhóm: khoảng 100 giờ giao diện chưa dùng trong hai sprint đầu; màn hình dồn về sau', 'Cho giao diện dựng khung dùng chung và màn hình theo thiết kế bằng dữ liệu mẫu, rồi nối vào hợp đồng API khi sẵn sàng (cần đổi quy tắc phụ thuộc)', 'PL-1 và FE-1, quyết định khi lập kế hoạch Sprint 2 ngày 13/11/2026'),
    ('4. Tổng thời gian dài hơn lịch ban đầu (khoảng 26 sprint so với chín tháng)', 'Toàn dự án', 'Mốc go-live giả định 01/08/2027 của lịch ban đầu', 'Trình khách ba phương án: thêm một backend, giảm phạm vi (hoãn một số báo cáo), hoặc dời mốc go-live', 'PL-1, trình khách trước 27/11/2026 (hết Sprint 2)'),
    ('5. Nhiều câu hỏi làm rõ chưa có quyết định', f'{open_cl} câu hỏi chưa xong (trong 29)', 'Các đầu việc phụ thuộc chỉ chấm điểm theo giả định, có thể phải chấm lại', 'Gửi khách danh sách câu hỏi theo thứ tự ưu tiên; mỗi câu ghi phương án đề xuất để khách chỉ cần xác nhận', 'QA-1 soạn, PL-1 gửi, hạn trả lời 27/11/2026'),
    ('6. Ước lượng điểm chưa kiểm chéo toàn bộ', 'Nhóm đầu việc có tranh khóa đồng thời (chuỗi khóa, ca đua)', 'Độ chính xác của tổng điểm; dự báo số sprint có thể lệch', 'Kiểm chéo khoảng 35 đầu việc (10%) bằng người ước lượng khác, lệch từ một bậc trở lên thì chấm lại cả nhóm cùng cơ chế', 'PL-1 chỉ định, xong trước Sprint 3 (27/11/2026)'),
]
o.append(table(['Rủi ro', 'Issue', 'Ảnh hưởng tới mốc nào', 'Hành động', 'Ai làm, khi nào'], rows))
text = '\n'.join(o) + '\n'
open('progress-report.md', 'w', encoding='utf-8').write(text)
print('progress-report.md', len(text), 'ký tự | Sprint 1:', s1n, 'issue', s1s, 'SWP, xong', ds, '| Sprint 2:', len(S2))
