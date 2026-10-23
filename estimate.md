# Ước lượng SWP và giờ

Báo cáo của skill chấm điểm (HTML, mở được bằng trình duyệt, không cần mạng): [reports/sun-estimate-mk-seafood-lab5.html](reports/sun-estimate-mk-seafood-lab5.html).

Nguồn chấm là chính GitHub Project: 404 mục, trong đó 350 issue lá được chấm Scope × Complexity (tra ra SWP, Standard Work Point) và 54 issue cha lấy tổng con. Điểm đã chốt nằm ở trường `point`, giờ ở trường `Giờ ước lượng`. Tổng toàn dự án: **1.647 SWP, 5.764,5 giờ** (khoảng 824 ngày công).

## 2. Issue mẫu skill chọn để kiểm

Skill chọn năm issue theo quy tắc cố định (nhỏ nhất, trung vị thấp, lớn nhất, ngoại lệ, độ tin cậy thấp nhất). Mỗi issue được hỏi hai vòng: mức độ khó, rồi điểm cụ thể. Bốn issue giữ nguyên, một issue được nâng.

| Issue | Skill chấm | Bạn chốt | Lý do |
|---|---|---|---|
| #55 E01-CLR-01 | 1 SWP (nhỏ nhất) | 1 SWP (giữ nguyên) | Chỉ một câu hỏi làm rõ, quyết định ghi vào ADR hoặc PREMISE; không có việc phát triển |
| #94 E02-FE-07 | 5 SWP (trung vị) | 5 SWP (giữ nguyên) | Một màn có modal hai tab, bốn trạng thái, nhiều mã lỗi số dư, yêu cầu aal2 và online; 5 SWP khoảng hai ngày rưỡi |
| #398 E11-QA-04 | 10 SWP (lớn nhất) | 10 SWP (giữ nguyên) | Diễn tập toàn bộ lịch sử trên hai môi trường, cutover, nhánh no-go khôi phục; 10 SWP là 35 giờ |
| #193 E05-QA-03 | 10 SWP (ngoại lệ) | 10 SWP (giữ nguyên) | Ma trận hai phiên đồng thời trên PostgreSQL cho ba RPC, lặp 100 lần, kiểm lỗi 40P01 và bất biến |
| #98 E02-CLR-01 | 1 SWP (độ tin cậy thấp nhất) | 8 SWP (nâng) | Nâng từ 1 lên 8 vì cần khảo sát trình duyệt và tablet thực tế trước khi hỏi khách. Chỉ riêng issue này: #55 cùng nhóm làm rõ giữ 1 SWP; nếu lan sang 26 issue làm rõ cùng nhóm thì tổng tăng thêm 178 SWP, quá tay so với việc thật |

Sau khi năm mẫu được chốt, một lượt review độc lập (agent khác đọc dữ liệu chấm) phát hiện chấm không nhất quán giữa các issue cùng loại. Tôi đối chiếu từng issue với nội dung rồi sửa 16 issue dưới đây; không dùng hệ số điều chỉnh theo lô hay toàn cục.

| Issue | Vấn đề | Điểm | Cách sửa |
|---|---|---|---|
| #29, #70, #79, #80, #113, #116, #117, #179, #180, #232, #240, #307 | RPC có chuỗi khóa hoặc ca đua nhưng chấm độ khó thấp hơn các RPC cùng loại | +1 SWP mỗi issue | Nâng độ khó một bậc (C2 → C3), giữ phạm vi |
| #340, #369 | Phục hồi vận hành có đo RPO/RTO và diễn tập thật | +1 SWP mỗi issue | Nâng độ khó một bậc (C2 → C3) |
| #383 | Schema staging có năm bảng nhưng chấm như một bảng | 3 → 4 SWP | Mở rộng phạm vi (S2 → S3), hạ độ khó (C2 → C1): DDL theo khuôn, cố ý không ép kiểu |
| #5 | Màn nhập giao hàng nhận độ khó đồng thời của backend | 6 → 5 SWP | Hạ C3 → C2: khóa đồng thời do RPC sở hữu, giao diện chỉ chống bấm đôi |

Bốn issue gắn nhãn đồng thời nhưng vẫn C2 (#26, #72, #75, #264) được giữ nguyên vì DoD chưa đủ bằng chứng. Kết quả sau sửa: **1.647 SWP** (1.626 điểm chấm ban đầu, cộng 7 của #98 và 14 của lượt sửa này).

## 3. Cách quy ra giờ

**Cách chọn: đặt quy ước đổi SWP sang giờ** (cách b của đề), không ước trực tiếp từng issue. Skill chấm SWP không quy giờ, và ước tay 350 issue vừa tốn công vừa khó nhất quán.

**Quy ước: 1 SWP = 3,5 giờ**, tuyến tính, làm tròn 0,5 giờ, một hệ số cho mọi loại issue (be, fe, db, job, qa, doc, clarify). Issue cha có giờ bằng tổng giờ con. Chưa cộng buffer. Một ngày công là 7 giờ nên 1 SWP là nửa ngày: issue 5 SWP là 17,5 giờ, issue 10 SWP là 35 giờ.

**Vì sao 3,5.** Hai nguồn độc lập cho kết quả gần nhau:
1. Hiệu chuẩn theo LAB-1 trên chín epic đầu: phần dựng (be, fe, db, job) là 976 SWP so với 491,5 ngày công thô của LAB-1 (BE, FE, UX; đã gồm kiểm thử đơn vị và sửa lỗi, chưa nhân buffer 30%), tức 3,53 giờ mỗi SWP. Phần QA là 231 SWP so với 107,9 ngày công, tức 3,27 giờ mỗi SWP.
2. Ước trực tiếp tám issue mốc:

| Issue mốc | Nội dung | SWP | Giờ ước trực tiếp | Giờ/SWP |
|---|---|---|---|---|
| #55 | làm rõ một câu hỏi | 1 | 3 | 3,0 |
| #94 | màn modal hai tab | 5 | 17 | 3,4 |
| #113 | RPC chốt giao dịch có chuỗi khóa | 6 | 21 | 3,5 |
| #70 | RPC ghi offline lần đầu | 4 | 12 | 3,0 |
| #237 | DB gắn trigger bất biến đã có | 3 | 7 | 2,3 |
| #193 | QA đồng thời chốt sổ | 10 | 28 | 2,8 |
| #273 | worker ghi kết quả SFTP | 10 | 35 | 3,5 |
| #398 | QA diễn tập và cutover | 10 | 40 | 4,0 |

Trung bình khoảng 3,2 giờ mỗi SWP, trong khoảng 2,3 đến 4,0, gần 3,5; nên giữ một hệ số tuyến tính cho đơn giản.

**Áp dụng nhất quán.** Giờ mọi issue lá bằng SWP × 3,5, làm tròn 0,5 giờ; giờ issue cha bằng tổng giờ con. Script đọc từ chính báo cáo SWP rồi ghi vào trường `Giờ ước lượng`, đối chiếu ngược 404 mục khớp. Tổng 350 lá là 5.764,5 giờ.

**Hạn chế phải nói rõ.** Hệ số lấy từ LAB-1 nên so sánh ở mục 5 chỉ có nghĩa ở **phân bổ giữa các epic**, không phải kiểm chứng độc lập tổng giờ. Giờ chưa gồm buffer 30% của LAB-1, không gồm quản lý dự án hay BrSE. Với sức chứa 224 giờ mỗi sprint (bốn người, 56 giờ mỗi người), tổng giờ cần khoảng **26 sprint** (khoảng 12 tháng), dài hơn lịch chín tháng phát triển của LAB-1; xem `progress-report.md`.

## 4. Tổng theo epic

| Epic | Số issue | Tổng SWP | Tổng giờ | Ghi chú |
|---|---|---|---|---|
| #6 E-01 Participant và xác thực | 47 lá (6 cha) | 184 | 644,0 | MFA, 許可/承認, 参加上限 (FR-PAU-006..008 là FR mới so với LAB-1); 47 lá gồm 25 BE, 13 FE |
| #60 E-02 Lot | 34 lá (5 cha) | 150 | 525,0 | 18 issue lá thuộc offline F-006/F-007 (87 SWP); 9 issue làm rõ chờ khách |
| #100 E-03 Giao dịch | 31 lá (5 cha) | 142 | 497,0 | Chuỗi khóa lot → participant → giao dịch, 参加上限 kiểm hai lần; điểm tập trung ở nhóm RPC khóa |
| #137 E-04 Điều chỉnh giao dịch | 22 lá (4 cha) | 103 | 360,5 | Sửa sau chốt (逆仕訳, 差額記録), delta thưởng; nhiều issue DB và trigger |
| #164 E-05 Đối soát và chốt sổ | 28 lá (4 cha) | 137 | 479,5 | 締め, 締め再開 hai người, chặn khi còn pending; QA đồng thời có hai issue 10 SWP |
| #197 E-06 Tiền thưởng thanh toán đúng hạn và phiên bản 業務規程 | 31 lá (4 cha) | 169 | 591,5 | 完納奨励金 và vòng đời phiên bản 業務規程; job tính và kích hoạt |
| #1 E-07 Giao hàng | 23 lá (4 cha) | 106 | 371,0 | Giao hàng, xác định 完納; 11 issue giao diện |
| #256 E-08 Thông báo | 28 lá (3 cha) | 139 | 486,5 | Outbox và worker gửi tin (14 issue); lịch gửi theo giây còn một câu hỏi kỹ thuật mở |
| #288 E-09 Báo cáo và kiểm toán | 40 lá (7 cha) | 205 | 717,5 | Báo cáo, xuất tệp SFTP, audit hash-chain (một phần); 10 issue làm rõ |
| #336 E-10 Nền tảng chung | 39 lá (0 cha) | 181 | 633,5 | Khung dự án, DB, RLS/RPC, outbox nền, audit nền, sao lưu; không có trong chín epic LAB-1 |
| #376 E-11 Di trú dữ liệu ban đầu | 27 lá (1 cha) | 131 | 458,5 | Di trú dữ liệu ban đầu, diễn tập, đối chiếu, rollback; ngoài phạm vi LAB-1 |
| **Tổng** | 350 lá (43 cha) | **1647** | **5.764,5** | Tổng của 11 epic bằng tổng 350 lá |

Theo loại việc (SWP): be 674, fe 359, db 144, job 11, qa 299, doc 116, clarify 44.

## 5. So với estimate LAB-1

Đơn vị so sánh: LAB-1 tính bằng ngày công thô (một ngày 7 giờ, BE + FE + UX, đã gồm kiểm thử đơn vị và sửa lỗi, chưa nhân buffer 30%; bản 16/10/2026); LAB-5 quy từ SWP bằng 1 SWP = 3,5 giờ, tức 0,5 ngày công. Cột "LAB-5" của từng epic là phần dựng (be, fe, db, job) để cùng phạm vi với LAB-1; số tổng gồm cả QA, tài liệu API Design và issue làm rõ ghi trong ngoặc.

| Phần | LAB-1 | LAB-5 | Chênh | Vì sao |
|---|---|---|---|---|
| E-01 participants-auth | 68,5 ngày công | 77,0 ngày công (phần dựng; tổng cả epic 92,0) | +8,5 (+12%) | LAB-5 thêm FR-PAU-006, 007, 008 (MFA, 許可/承認, 参加上限) mà 38 function của LAB-1 chưa có; LAB-1 có 11,5 ngày UX, LAB-5 không (thiết kế giao diện đã có từ LAB-4) nên chênh thực còn lớn hơn |
| E-02 lots | 56,0 ngày công | 56,0 ngày công (phần dựng; tổng cả epic 75,0) | +0,0 (+0%) | Khớp tổng, nhưng LAB-5 gộp offline F-006/F-007 vào E-02 (87 SWP gồm cả QA) còn LAB-1 để offline ngoài chín epic (35 ngày); bỏ phần offline thì E-02 thấp hơn LAB-1. Khớp là ngẫu nhiên |
| E-03 trading | 74,0 ngày công | 57,5 ngày công (phần dựng; tổng cả epic 71,0) | -16,5 (-22%) | LAB-1 có 18 ngày UX cho giao dịch mà LAB-5 không tính; trừ UX, LAB-1 còn 56, gần bằng LAB-5 |
| E-04 trade-adjustment | 35,5 ngày công | 37,0 ngày công (phần dựng; tổng cả epic 51,5) | +1,5 (+4%) | Khớp; LAB-5 thêm trigger và bút toán ở tầng DB (18 SWP DB) |
| E-05 daily-closing | 42,5 ngày công | 48,5 ngày công (phần dựng; tổng cả epic 68,5) | +6,0 (+14%) | LAB-5 tách riêng 締め再開 hai người (FR-CLS-004 mới) và điều kiện không chốt khi còn pending |
| E-06 incentive | 46,5 ngày công | 61,5 ngày công (phần dựng; tổng cả epic 84,5) | +15,0 (+32%) | LAB-5 thêm vòng đời phiên bản 業務規程 hai người duyệt, job tính và kích hoạt, delta thưởng sau chốt (P7, ADR-003); LAB-1 chưa có |
| E-07 delivery | 36,0 ngày công | 34,5 ngày công (phần dựng; tổng cả epic 53,0) | -1,5 (-4%) | Khớp |
| E-08 notifications-rules | 24,0 ngày công | 46,0 ngày công (phần dựng; tổng cả epic 69,5) | +22,0 (+92%) | LAB-5 đặt worker gửi tin dùng chung ở E-08 (14 issue outbox/worker); LAB-1 mô tả E-08 nhỏ. Hệ số 5,8 SWP/ngày công của E-08 cao nhất trong chín epic, nên ưu tiên rà lại |
| E-09 reports-audit | 108,5 ngày công | 70,0 ngày công (phần dựng; tổng cả epic 102,5) | -38,5 (-35%) | Nền audit (bảng, trigger, ghi chuỗi băm) nằm ở E-10 (ADR-008), nên E-09 chủ yếu còn báo cáo, xuất tệp và job kiểm tra; phần chênh âm được bù ở E-10. LAB-1 còn có 14,5 ngày UX |
| Chín epic LAB-1 (E-01..E-09) | 491,5 ngày công | 488,0 ngày công | -3,5 (-0,7%) | Gần như khớp vì hệ số 3,5 giờ/SWP hiệu chuẩn từ chính tổng này; chỉ phân bổ giữa các epic mới có ý nghĩa |
| Nền tảng chung (E-10) | 58,5 ngày công (PLAT-01..06) | 68,5 ngày công (phần dựng; tổng 90,5) | +10,0 | LAB-5 có audit nền, outbox nền và sao lưu ở E-10 (PREMISE H-02). Hạ tầng AWS của LAB-1 (ECS, RDS, WAF, Terraform) không còn vì LAB-4 chọn Next.js, Supabase, Vercel (P2, ADR-001, ADR-002) |
| Di trú dữ liệu (E-11) | 0 (ngoài phạm vi LAB-1) | 37,5 ngày công (phần dựng; tổng 65,5) | +37,5 | LAB-4 đưa FR-RPA-008 và ADR-014 vào phạm vi (PREMISE H-02) |
| QA | 107,9 ngày công | 149,5 ngày công | +41,6 (+39%) | LAB-1 ước QA theo tỷ lệ so với dựng; LAB-5 có issue QA cụ thể (luồng, ma trận đồng thời hai phiên PostgreSQL, diễn tập di trú) nên cao hơn |
| Tổng (chưa buffer, chưa hạ tầng AWS) | 692,9 ngày công (585 dựng + 107,9 QA) | 823,5 ngày công | +130,6 (+19%) | Phần chênh chủ yếu do di trú (PREMISE H-02), tài liệu API Design (S-01), issue làm rõ và FR mới ở E-01, E-05, E-06; LAB-1 ghi độ chính xác "Super Rough" nên không coi đây là sai lệch |

Hai điều khi đọc bảng này. Thứ nhất, LAB-1 ước theo function còn LAB-5 theo màn và RPC/job, nên chỉ so được ở mức epic. Thứ hai, E-08 (hệ số cao nhất) và E-09 (chênh âm lớn nhất) là hai epic nên ưu tiên rà lại khi có thêm thông tin; phần nền audit di chuyển giữa E-09 và E-10 làm hai epic này không so trực tiếp được với LAB-1.
