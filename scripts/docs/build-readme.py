#!/usr/bin/env python3
"""Sinh README.md. Chạy tại gốc repo sau các build khác: python3 scripts/docs/build-readme.py"""
import collections, sys
sys.path.insert(0, 'scripts/docs')
from docs_data import BACKLOG, ISSUES, EPIC_NUM, special_value, table, NUM, REPORT
from premise_rows import build

REPO = 'https://github.com/minhht-0134/mk_seafood_lab5'
PROJECT = 'https://github.com/users/minhht-0134/projects/1'
fixes, assumes, index = build()
tot = sum(r['finalSWP'] for r in REPORT['issues'])
leaves = [v for v in ISSUES.values() if v['leaf']]
rows = []
for ek, b in BACKLOG.items():
    e = b['epic']
    ls = [v for v in leaves if v['epic'] == ek]
    sp = collections.Counter(special_value(v.get('special')) for v in ls); sp.pop('Không', None)
    s = [c for c, g in fixes if g['epic'] == ek]; g_ = [c for c, g in assumes if g['epic'] == ek]
    note = ', '.join(f'{k} ({n})' for k, n in sp.most_common(4)) or 'không có nhóm đặc thù chính'
    if s or g_: note += '. PREMISE: ' + ', '.join(s + g_)
    rows.append((', '.join(e['specs']), f'#{EPIC_NUM[ek]} — {e["title"]}', note))
rows.append(('PREMISE S-01, H-03 (API Design cho từng epic)', 'Cả 11 epic, mỗi epic một issue `doc`', 'Thêm so với LAB-4'))
rows.append(('PREMISE H-02 (hạ tầng chung và di trú)', f'#{EPIC_NUM["E-10"]} — E-10; #{EPIC_NUM["E-11"]} — E-11', 'Hai epic ngoài chín feature; E-11 là di trú dữ liệu (FR-RPA-008, ADR-014)'))
text = f'''# Sakura Suisan (Product A): break task và báo cáo tiến độ, LAB-5

- **Dự án:** Hệ thống hỗ trợ nghiệp vụ chợ 桜水産市場 (Sakura Suisan), chợ bán buôn thủy sản
- **Mã học viên:** minhht-0134
- **Đề:** Product A

## Tổng quan

Backlog được break từ bộ thiết kế LAB-4 bản 0.3.3 (cập nhật 14/10/2026). `PREMISE.md` **có thay đổi** so với LAB-4: {len(fixes) + 1} dòng thêm/sửa spec, {len(assumes) + 6} giả định bổ sung, 9 hướng chốt khi LAB-4 còn nhiều phương án.

Backlog có **11 epic** (chín feature của LAB-4 cộng nền tảng chung và di trú dữ liệu), 43 issue cha và 350 issue lá, tổng cộng {str(tot)[0]}.{str(tot)[1:]} SWP và 5.764,5 giờ ước lượng.
Đã giả lập **Sprint 1** (02/11 đến 13/11/2026) chạy xong; Sprint 2 đã xếp kế hoạch. Số liệu sprint là giả lập.

## Link

- Repo: {REPO}
- GitHub Project: {PROJECT}
- Báo cáo HTML của skill chấm SWP: [reports/sun-estimate-mk-seafood-lab5.html](reports/sun-estimate-mk-seafood-lab5.html) (mở trực tiếp bằng trình duyệt)
- Đã mở thử bằng cửa sổ ẩn danh: **chưa**. Repo và Project đang private, sẽ mở thử và ghi lại ở đây sau khi chuyển sang public.

## Cấu trúc repo

''' + table(['File/thư mục', 'Nội dung'], [
    ('`README.md`', 'Tệp này: tổng quan, link, cấu trúc, ánh xạ spec sang epic'),
    ('`PREMISE.md`', 'Khác biệt so với LAB-4: spec thêm/sửa, giả định bổ sung, hướng đã chốt'),
    ('`task-breakdown.md`', 'Nguyên tắc chia task, ánh xạ spec sang issue, hạng mục đặc thù, chỗ hở của spec'),
    ('`estimate.md`', 'Issue mẫu kiểm SWP, cách quy ra giờ, tổng theo epic, so với LAB-1'),
    ('`progress-report.md`', 'Báo cáo tiến độ Sprint 1 (giả lập): trạng thái, burndown, rủi ro trễ'),
    ('`AI-report.md`', 'Cách dùng AI: skill và prompt, cách review, điểm đặc biệt'),
    ('`reports/`', 'Báo cáo HTML của skill `tkm:sun-estimate` (một tệp, tự chứa, không cần mạng)'),
    ('`scripts/backlog/`', 'Backlog dạng JSON của 11 epic và script kiểm (khóa duy nhất, cha-con, phụ thuộc, vòng)'),
    ('`scripts/github/`', 'Script tạo issue, sub-issue và trường Project; bản đồ khóa backlog sang số issue'),
    ('`scripts/swp/`', 'Script chấm SWP, ghi `point` và `Giờ ước lượng`, xếp và giả lập sprint; nhật ký giả lập Sprint 1'),
    ('`scripts/docs/`', 'Script sinh các tệp Markdown từ dữ liệu Project để số liệu khớp nhau'),
    ('`skills/review-loop/`', 'Skill tự viết cho vòng review chéo giữa AI viết và reviewer độc lập: sinh prompt, kiểm chứng từng phát hiện, soi lại phần vừa sửa, ghi nhật ký'),
    ('`.gitignore`', 'Loại tài liệu gốc (RFP, bộ spec LAB-4) và nháp làm việc khỏi repo'),
]) + '''

Thư mục `skills/` chứa một skill tự viết là `review-loop` (bản v1); các skill còn lại dùng nguyên bản có sẵn của bộ công cụ.

## Spec → epic

Cột "Epic" là số issue trên GitHub Project. Ghi chú liệt kê nhóm nghiệp vụ đặc thù chính của epic (số trong ngoặc là số issue lá) và các dòng `PREMISE.md` liên quan.

''' + table(['Spec', 'Epic trên Project', 'Ghi chú'], rows) + '\n'
open('README.md', 'w', encoding='utf-8').write(text)
print('README.md', len(text))
