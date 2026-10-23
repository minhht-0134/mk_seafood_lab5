#!/usr/bin/env python3
"""Sinh PREMISE.md từ bảng chỗ hở (scripts/docs/gaps.json). Chạy tại gốc repo: python3 scripts/docs/build-premise.py"""
import sys
sys.path.insert(0, 'scripts/docs')
from docs_data import ISSUES, EPIC_NUM, keys_in, nums, num_text, table, cut, NUM
from premise_rows import build, body

fixes, assumes, index = build()
doc_parents = [NUM[k] for k in ISSUES if k.endswith('-DOC-01') and ISSUES[k]['type'] == 'doc'] or \
    [NUM[f'E{n:02d}-DOC-01'] for n in range(1, 12) if f'E{n:02d}-DOC-01' in NUM]
n_doc = sum(1 for i in ISSUES.values() if i['type'] == 'doc' and i['leaf'])

out = ['''# PREMISE: khác biệt so với bản LAB-4

Backlog được break từ bản LAB-4 đã nộp. Tài liệu này khai từng chỗ lệch: spec phải sửa hoặc thêm, giả định lấp chỗ spec để ngỏ, và hướng chọn khi LAB-4 còn nhiều phương án. Mã `S-xx`, `G-xx`, `H-xx` là mã dòng để `task-breakdown.md` và `estimate.md` trỏ tới. `#N` là số issue trên GitHub Project.
Mọi chỗ hở dưới đây phát hiện khi break từng epic; không có góp ý review LAB-4 nào được dùng làm nguồn.

## 1. Spec thêm, bỏ, sửa so với LAB-4
''']
rows = [('S-01', 'api-design/_index (viết ở LAB-5), mẫu BM-2-901-52', 'Thêm',
         'LAB-4 ghi tài liệu API Design `{API_ID}_API.md` là việc của LAB-5 nhưng chưa có tệp nào → mỗi epic thêm một issue `doc` soạn API Design cho nhóm API của epic '
         f'({n_doc} issue `doc` lá, kể cả hai tài liệu di trú inventory và runbook ở E-11); issue BE phụ thuộc issue `doc` của epic mình',
         'Chỗ hở lặp lại ở cả 11 epic (dòng 1 bảng chỗ hở mỗi epic): BE không có hợp đồng API để làm theo', nums([NUM[k] for k in ISSUES if ISSUES[k]['type'] == 'doc' and ISSUES[k]['leaf']], 12))]
for code, g in fixes:
    ks = [k for k in keys_in(g['xl'] + ' ' + g['gap'])]
    rows.append((code, g['spec'], 'Sửa', f"{cut(num_text(g['gap']), 260)} → {cut(body(g['xl']), 300)}",
                 f"Chỗ hở phát hiện khi break {g['epic']} (dòng {g['n']} bảng chỗ hở): hai nguồn spec lệch nhau hoặc để ngỏ ({g['spec']})",
                 nums([NUM[k] for k in ks]) or f"epic {g['epic']} (#{EPIC_NUM[g['epic']]})"))
out.append(table(['Spec', 'Thêm/Bỏ/Sửa', 'Trước → sau', 'Vì sao', 'Issue bị ảnh hưởng'], [r[:1] and (f'**{r[0]}** · {r[1]}',) + r[2:] for r in rows]))
out.append('\nKhông có dòng nào thuộc loại "Bỏ": mọi FR và ADR của LAB-4 đều thành issue, trừ hai ngoại lệ ghi ở `task-breakdown.md` mục 2.\n\n## 2. Giả định bổ sung\n')
plan = [
    ('**G-01** · Kickoff 02/11/2026 (thứ Hai đầu tiên sau mốc 01/11 của LAB-1); sprint hai tuần', 'Lịch LAB-1 chỉ có kickoff giả định, chưa có lịch sprint', 'Mốc Iteration Sprint 1 từ 02/11, Sprint 2 từ 16/11/2026; toàn bộ dữ liệu sprint là giả lập'),
    ('**G-02** · Năm vai trò: BE-1, BE-2, FE-1, QA-1 nhận issue, PL-1 dẫn dắt không nhận issue', 'Cơ cấu nhân sự dự án chưa chốt', 'Sức chứa sprint 224 giờ; FE-1 và QA-1 chỉ một người nên cổ chai ở hai vai trò này'),
    ('**G-03** · Một ngày 7 giờ (quy ước Sun*), một sprint 10 ngày làm việc, hiệu suất thực 80% → 56 giờ mỗi người mỗi sprint', 'Quy ước giờ chưa có trong spec', 'Quy ra giờ và số sprint cần (`estimate.md` mục 3)'),
    ('**G-04** · 29 issue làm rõ chưa có quyết định của khách: các issue phụ thuộc được chấm theo phương án đề xuất ghi trong issue làm rõ, độ tin cậy thấp', 'Các câu hỏi mở của REQ-001 §8 còn chờ khách', 'Nếu khách chọn phương án khác phải chấm lại các issue phụ thuộc (đa số ở E-08, E-09, E-10, E-11)'),
    ('**G-05** · Điểm SWP chấm theo thân issue (mục tiêu, DoD, mã spec), không đọc lại nguyên văn spec cho từng issue', 'Giới hạn thời gian và công sức của bài lab', 'Sai lệch chấm có thể còn ở các RPC có tranh khóa; đã rà bằng một lượt review độc lập (`AI-report.md`)'),
    ('**G-06** · Chỉ lập kế hoạch Sprint 1 và Sprint 2; các sprint sau chưa xếp issue', 'Lịch chi tiết cả dự án nằm ngoài yêu cầu bài lab', 'Chỉ 33 trên 350 issue lá có Iteration; phần còn lại nằm trong backlog'),
]
arows = list(plan)
for code, g in assumes:
    ks = keys_in(g['xl'] + ' ' + g['gap'])
    arows.append((f'**{code}** · [{cut(g["spec"], 70)}] {cut(body(g["xl"]), 320)}', f"{g['spec']}: {cut(num_text(g['gap']), 240)}",
                  (nums([NUM[k] for k in ks]) or f"epic {g['epic']} (#{EPIC_NUM[g['epic']]})") + '. Đổi giả định thì chấm lại SWP của các issue này'))
out.append(table(['Giả định', 'Chỗ spec/RFP để ngỏ', 'Ảnh hưởng tới issue/estimate'], arows))
out.append('\n## 3. Hướng đã chốt\n')
H = [
    ('**H-01** · Độ hạt issue', 'LAB-4 không quy định cách chia việc', 'Một issue là một màn FE hoặc một RPC/job BE; tách sub-issue khi vượt khoảng ba ngày công', 'Đủ nhỏ để làm xong trong một sprint; DoD kiểm được từ AC của FR và quy tắc R1..Rn của ADR'),
    ('**H-02** · Epic cho hạ tầng chung và di trú', 'LAB-4 có 9 feature; khung dự án, DB, RLS/RPC, outbox, audit nằm rải trong các tài liệu `_common`; di trú dữ liệu ở FR-RPA-008 và ADR-014', 'Thêm hai epic ngoài 9 feature: E-10 Nền tảng chung và E-11 Di trú dữ liệu ban đầu', 'Tránh mỗi epic tự dựng lại khung; di trú là hạng mục đặc thù phải tách riêng'),
    ('**H-03** · Nơi soạn API Design', 'Để ngỏ cho LAB-5 (xem S-01)', 'Một issue `doc` cho mỗi epic, BE phụ thuộc issue đó', 'Có hợp đồng API trước khi làm BE; FE làm theo cùng hợp đồng'),
    ('**H-04** · Cặp API LIST và GET cùng tài nguyên', 'LAB-4 liệt kê hai API riêng', 'Gộp thành một issue BE (7 cặp: ADJ_REQUEST, CLS_DISPUTE, DLV, INC_RULE_VERSION, PAU_ACCOUNT, PAU_PARTICIPANT, TRD)', 'Cùng bảng, cùng quyền, cùng bộ kiểm thử; hai issue chỉ làm tăng chi phí điều phối'),
    ('**H-05** · Phụ thuộc đặt ở đâu', 'Chưa quy định', 'Issue cha không khai phụ thuộc; mọi phụ thuộc khai ở issue lá, kiểm bằng script (không vòng, không khóa lạ)', 'Tránh cộng đôi và phụ thuộc vòng khi issue cha chỉ là tổng con'),
    ('**H-06** · Số trạng thái màn hình', 'Số trạng thái nêu ở nhiều chỗ, có chỗ lệch', 'Chỉ dùng tên và số trạng thái trong bảng trạng thái của từng SPEC; không đếm tệp ảnh', 'Một nguồn duy nhất cho DoD và kiểm thử màn'),
    ('**H-07** · Đưa câu hỏi mở thành issue', 'Spec ghi `[ĐIỀN]` hoặc câu hỏi Q chưa chốt', 'Tạo issue loại `clarify` cho 29 chỗ cần khách hoặc Tech Lead quyết; backlog đi tiếp bằng giả định G-xx', 'Không chặn dự án nhưng không để câu hỏi chìm trong ghi chú'),
    ('**H-08** · Hạng mục đặc thù', 'Nằm lẫn trong issue CRUD nếu theo spec', 'Mỗi ràng buộc ở mục 4 đề bài có issue riêng và nhãn trường "Nhóm đặc thù" trên Project', 'Theo dõi và chấm riêng được; xem `task-breakdown.md` mục 3'),
    ('**H-09** · Đổi SWP ra giờ', 'LAB-1 tính bằng ngày công; skill chấm SWP không quy giờ', 'Một SWP bằng 3,5 giờ, tuyến tính, làm tròn 0,5 giờ, chưa cộng buffer', 'Hiệu chuẩn từ LAB-1 và tám issue mốc; xem `estimate.md` mục 3'),
]
out.append(table(['Vấn đề', 'Các phương án ở LAB-4', 'Phương án chốt', 'Vì sao'], H))
text = '\n'.join(out) + '\n'
open('PREMISE.md', 'w', encoding='utf-8').write(text)
print('PREMISE.md', len(text), 'ký tự |', len(fixes) + 1, 'dòng S |', len(assumes) + 6, 'dòng G |', len(H), 'dòng H')
