# Sakura Suisan (Product A): break task và báo cáo tiến độ, LAB-5

- **Dự án:** Hệ thống hỗ trợ nghiệp vụ chợ 桜水産市場 (Sakura Suisan), chợ bán buôn thủy sản
- **Mã học viên:** minhht-0134
- **Đề:** Product A

## Tổng quan

Backlog được break từ bộ thiết kế LAB-4 bản 0.3.3 (cập nhật 14/10/2026). `PREMISE.md` **có thay đổi** so với LAB-4: 22 dòng thêm/sửa spec, 64 giả định bổ sung, 9 hướng chốt khi LAB-4 còn nhiều phương án.

Backlog có **11 epic** (chín feature của LAB-4 cộng nền tảng chung và di trú dữ liệu), 43 issue cha và 350 issue lá, tổng cộng 1.647 SWP và 5.764,5 giờ ước lượng.
Đã giả lập **Sprint 1** (02/11 đến 13/11/2026) chạy xong; Sprint 2 đã xếp kế hoạch. Số liệu sprint là giả lập.

## Link

- Repo: https://github.com/minhht-0134/mk_seafood_lab5
- GitHub Project: https://github.com/users/minhht-0134/projects/1
- Báo cáo HTML của skill chấm SWP: [reports/sun-estimate-mk-seafood-lab5.html](reports/sun-estimate-mk-seafood-lab5.html) (mở trực tiếp bằng trình duyệt)
- Đã mở thử bằng cửa sổ ẩn danh: **chưa**. Repo và Project đang private, sẽ mở thử và ghi lại ở đây sau khi chuyển sang public.

## Cấu trúc repo

| File/thư mục | Nội dung |
|---|---|
| `README.md` | Tệp này: tổng quan, link, cấu trúc, ánh xạ spec sang epic |
| `PREMISE.md` | Khác biệt so với LAB-4: spec thêm/sửa, giả định bổ sung, hướng đã chốt |
| `task-breakdown.md` | Nguyên tắc chia task, ánh xạ spec sang issue, hạng mục đặc thù, chỗ hở của spec |
| `estimate.md` | Issue mẫu kiểm SWP, cách quy ra giờ, tổng theo epic, so với LAB-1 |
| `progress-report.md` | Báo cáo tiến độ Sprint 1 (giả lập): trạng thái, burndown, rủi ro trễ |
| `AI-report.md` | Cách dùng AI: skill và prompt, cách review, điểm đặc biệt |
| `reports/` | Báo cáo HTML của skill `tkm:sun-estimate` (một tệp, tự chứa, không cần mạng) |
| `scripts/backlog/` | Backlog dạng JSON của 11 epic và script kiểm (khóa duy nhất, cha-con, phụ thuộc, vòng) |
| `scripts/github/` | Script tạo issue, sub-issue và trường Project; bản đồ khóa backlog sang số issue |
| `scripts/swp/` | Script chấm SWP, ghi `point` và `Giờ ước lượng`, xếp và giả lập sprint; nhật ký giả lập Sprint 1 |
| `scripts/docs/` | Script sinh các tệp Markdown từ dữ liệu Project để số liệu khớp nhau |
| `skills/review-loop/` | Skill tự viết cho vòng review chéo giữa AI viết và reviewer độc lập: sinh prompt, kiểm chứng từng phát hiện, soi lại phần vừa sửa, ghi nhật ký |
| `.gitignore` | Loại tài liệu gốc (RFP, bộ spec LAB-4) và nháp làm việc khỏi repo |

Thư mục `skills/` chứa một skill tự viết là `review-loop` (bản v1); các skill còn lại dùng nguyên bản có sẵn của bộ công cụ.

## Spec → epic

Cột "Epic" là số issue trên GitHub Project. Ghi chú liệt kê nhóm nghiệp vụ đặc thù chính của epic (số trong ngoặc là số issue lá) và các dòng `PREMISE.md` liên quan.

| Spec | Epic trên Project | Ghi chú |
|---|---|---|
| FR-PAU-001..008, design/participants-auth, PAU_DB, ADR-004, ADR-010, ADR-011, ADR-013 (phần cấu hình) | #6 — E-01 Participant và xác thực (participants-auth) | 許可 và 承認 (17), MFA (7), 参加上限 (2). PREMISE: S-02, S-03, S-04, S-05, G-07, G-08, G-09, G-10, G-11, G-12, G-13 |
| FR-LOT-001..005, design/lots, LOT_DB, ADR-009 | #60 — E-02 Lot (lots) | Offline (18). PREMISE: S-06, G-14, G-15, G-16, G-17 |
| FR-TRD-001..007, design/trading, TRD_DB, ADR-013, ADR-004 R7 | #100 — E-03 Giao dịch (trading) | 参加上限 (11). PREMISE: S-07, S-08, S-09, G-18, G-19, G-20, G-21, G-22 |
| FR-ADJ-001..003, design/trade-adjustment, ADJ_DB, ADR-006, ADR-005 | #137 — E-04 Điều chỉnh giao dịch (trade-adjustment) | Sửa sau chốt (12), 締め再開 hai người (4), Khóa ngày hai lớp (3), 完納奨励金 (1). PREMISE: S-10, S-11, S-12, S-13, G-23 |
| FR-CLS-001..004, design/daily-closing, CLS_DB, ADR-005, ADR-015 | #164 — E-05 Đối soát và chốt sổ (daily-closing) | Khóa ngày hai lớp (7), 締め chốt sổ (7), 締め再開 hai người (4). PREMISE: S-14, G-24, G-25 |
| FR-INC-001..003, design/incentive, INC_DB, ADR-003, ADR-006 | #197 — E-06 Tiền thưởng thanh toán đúng hạn và phiên bản 業務規程 (incentive) | 完納奨励金 (15), 業務規程 có phiên bản (7), 締め再開 hai người (4), Outbox và worker (1). PREMISE: S-15, G-26, G-27, G-28, G-29, G-30 |
| FR-DLV-001..005, design/delivery, DLV_DB, ADR-006, ADR-005 (khóa ngày) | #1 — E-07 Giao hàng (delivery) | Khóa ngày hai lớp (10), 完納奨励金 (9). PREMISE: S-16, G-31, G-32, G-33, G-34 |
| FR-NTF-001..003, design/notifications-rules, NTF_DB, ADR-007 | #256 — E-08 Thông báo (notifications-rules) | Outbox và worker (14), MFA (9). PREMISE: S-17, G-35, G-36, G-37, G-38, G-39, G-40, G-41, G-42, G-43, G-44, G-45 |
| FR-RPA-001..007, design/reports-audit, RPA_DB, AUDIT_DB, ADR-007, ADR-008 | #288 — E-09 Báo cáo và kiểm toán (reports-audit) | MFA (11), Outbox và worker (9), Audit bất biến (7), 完納奨励金 (2). PREMISE: S-18, G-46, G-47, G-48, G-49, G-50, G-51, G-52, G-53, G-54, G-55 |
| ADR-001, ADR-002, ADR-007, ADR-008, ADR-010, CORE_DB, AUDIT_DB, OUTBOX_DB, ARCH-01, ARCH-05, api-list §1, §2.1, error-codes §1, log-convention | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | MFA (7), Outbox và worker (5), Audit bất biến (3), Khóa ngày hai lớp (2). PREMISE: S-19, G-56, G-57, G-58, G-59, G-60 |
| FR-RPA-008, ADR-014, RPA_MIGRATION_LOAD_TECH, RPA_DB §4.3..§4.10, api-list §3 RPA_MIGRATION_* | #376 — E-11 Di trú dữ liệu ban đầu (FR-RPA-008) | Di trú dữ liệu (13), MFA (3), Khóa ngày hai lớp (1), Audit bất biến (1). PREMISE: S-20, S-21, S-22, G-61, G-62, G-63, G-64 |
| PREMISE S-01, H-03 (API Design cho từng epic) | Cả 11 epic, mỗi epic một issue `doc` | Thêm so với LAB-4 |
| PREMISE H-02 (hạ tầng chung và di trú) | #336 — E-10; #376 — E-11 | Hai epic ngoài chín feature; E-11 là di trú dữ liệu (FR-RPA-008, ADR-014) |
