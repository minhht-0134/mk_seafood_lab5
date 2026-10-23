#!/usr/bin/env python3
"""Ghi một dòng nhật ký cho một vòng review vào tệp Markdown (nối cuối).
Dùng: python3 skills/review-loop/scripts/log-round.py --file notes/ai-work-log.md --subject "E-05" --round 2 \
        --found 12 --agree 10 --partial 1 --reject 0 --pending 1 --caused-by-fix 3 [--note "..."] [--date 2026-10-23]
Kiểm: đồng ý + một phần + bác + chưa đủ dữ liệu phải bằng số phát hiện."""
import argparse, datetime, sys

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('--file', required=True)
p.add_argument('--subject', required=True, help='đối tượng review, ví dụ E-05 hoặc estimate.md')
p.add_argument('--round', type=int, required=True)
p.add_argument('--found', type=int, required=True)
p.add_argument('--agree', type=int, default=0)
p.add_argument('--partial', type=int, default=0)
p.add_argument('--reject', type=int, default=0)
p.add_argument('--pending', type=int, default=0, help='chưa đủ dữ liệu')
p.add_argument('--caused-by-fix', type=int, default=0, help='số phát hiện do lượt sửa trước gây ra')
p.add_argument('--note', default='')
p.add_argument('--date', default=datetime.date.today().isoformat())
a = p.parse_args()
if a.agree + a.partial + a.reject + a.pending != a.found:
    sys.exit(f'Lỗi: {a.agree}+{a.partial}+{a.reject}+{a.pending} khác số phát hiện {a.found}')
if a.caused_by_fix > a.found:
    sys.exit('Lỗi: số phát hiện do lượt sửa gây ra lớn hơn tổng')
rate = round(a.agree * 100 / a.found) if a.found else 0
line = (f'- {a.date} · review {a.subject}, vòng {a.round}: {a.found} phát hiện; đồng ý {a.agree}, một phần {a.partial}, '
        f'bác {a.reject}, chưa đủ dữ liệu {a.pending} (tỷ lệ đồng ý {rate}%); do lượt sửa trước gây ra: {a.caused_by_fix}.')
if a.note: line += f' {a.note}'
if a.found and rate > 90: line += ' CẢNH BÁO: đồng ý trên 90%, kiểm lại đã mở nguồn cho từng điểm chưa.'
with open(a.file, 'a', encoding='utf-8') as f:
    f.write(line + '\n')
print(line)
