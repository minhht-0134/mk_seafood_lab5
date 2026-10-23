# Break task: epic → issue → sub-issue

Backlog gồm **11 epic, 43 issue cha và 350 issue lá** (404 mục trên GitHub Project, số issue từ #1 đến #404). Cột `#N` là số issue trên Project. Nguồn chia việc là thiết kế chi tiết LAB-4 cộng với `PREMISE.md`.

## 1. Nguyên tắc chia task

**Độ hạt.** Một issue là một màn hình FE (một `SCREEN_ID`) hoặc một RPC/job BE (một `FUNC_ID`). Issue quá lớn hoặc mơ hồ thì tách sub-issue; ngưỡng là khoảng ba ngày công (một ngày công = 7 giờ). Chỗ hay phải tách: migration nhiều bảng, RPC có chuỗi khóa, ca kiểm hai phiên PostgreSQL, màn nhiều trạng thái. Hai issue gộp thành một khi cùng bảng, cùng quyền và cùng bộ kiểm thử (cặp LIST + GET của cùng tài nguyên). Ngoài việc làm theo màn và RPC, có thêm ba loại: `doc` (soạn API Design cho epic), `qa` (kiểm đầu cuối theo luồng) và `clarify` (làm rõ một câu hỏi mở). Số issue lá theo loại: be 137, fe 78, qa 42, db 36, clarify 29, doc 25, job 3.

**Định nghĩa xong (DoD).** Mỗi issue có: mục tiêu một dòng; phạm vi và ngoài phạm vi (ngoài phạm vi trỏ về epic); DoD là danh sách đánh dấu quan sát được; tham chiếu spec chỉ bằng mã (`FR-`, `ADR-`, `SCREEN_ID`, `FUNC_ID`), không chép nguyên văn; phụ thuộc bằng số issue; nhãn nhóm đặc thù khi thuộc mục 3. Điều kiện chấp nhận lấy từ AC của FR và quy tắc R1..Rn của ADR. Một issue chỉ xong khi mọi dòng DoD tick được; không có dòng "làm xong phần việc" chung chung.

**Cách dùng epic → issue → sub-issue trên Project.**
- *Epic* là một issue loại `epic` (11 issue, #1, #6, #60, #100, #137, #164, #197, #256, #288, #336, #376). Epic có `Mã backlog` `E-NN`, danh sách ngoài phạm vi, và không tự chấm điểm: điểm bằng tổng con.
- *Issue cha* là issue có sub-issue (nhãn `issue-cha`); điểm và giờ bằng tổng con, không khai phụ thuộc.
- *Issue lá* là đơn vị chấm điểm, giao việc và đưa vào sprint. Quan hệ cha-con dùng sub-issue gốc của GitHub.
- Trường trên Project: `Status` (Todo, In Progress, Blocked, Done), `Iteration` (Sprint 1, Sprint 2), `Assignees`, `Người phụ trách (giả định)`, `point` (chỉ SWP), `Giờ ước lượng`, và các trường lọc `Loại`, `Epic`, `Nhóm đặc thù`, `Mã backlog`.
- Phụ thuộc giữa issue lá khai trong thân issue và đã kiểm tự động: không vòng, không khóa lạ (1447 cạnh).

## 2. Spec → issue

| Spec | Epic | Issue/sub-issue | Phần spec chưa thành issue và vì sao |
|---|---|---|---|
| FR-PAU-001..008 | #6 — E-01 Participant và xác thực (participants-auth) | 35 issue: #7, #10, #11, #12, #13, #14, #15, #16, #17, #19 … (+25) | — |
| design/participants-auth | #6 — E-01 Participant và xác thực (participants-auth) | toàn bộ 47 issue lá của epic | Không. Mỗi `SCREEN_ID_SPEC` thành issue FE, mỗi `FUNC_ID_TECH` thành issue BE |
| PAU_DB | #6 — E-01 Participant và xác thực (participants-auth) | 8 issue: #7, #8, #9, #10, #12, #15, #22, #26 | — |
| ADR-004 | #6 — E-01 Participant và xác thực (participants-auth) | 12 issue: #8, #9, #10, #11, #23, #29, #30, #31, #32, #33 … (+2) | — |
| ADR-010 | #6 — E-01 Participant và xác thực (participants-auth) | 7 issue: #14, #15, #20, #21, #41, #55, #57 | — |
| ADR-011 | #6 — E-01 Participant và xác thực (participants-auth) | 6 issue: #7, #12, #13, #17, #40, #57 | — |
| ADR-013 (phần cấu hình) | #6 — E-01 Participant và xác thực (participants-auth) | 3 issue: #8, #28, #58 | — |
| FR-LOT-001..005 | #60 — E-02 Lot (lots) | 26 issue: #64, #65, #66, #67, #68, #70, #71, #72, #73, #74 … (+16) | — |
| design/lots | #60 — E-02 Lot (lots) | toàn bộ 34 issue lá của epic | Không. Mỗi `SCREEN_ID_SPEC` thành issue FE, mỗi `FUNC_ID_TECH` thành issue BE |
| LOT_DB | #60 — E-02 Lot (lots) | 8 issue: #63, #64, #65, #71, #76, #77, #95, #99 | — |
| ADR-009 | #60 — E-02 Lot (lots) | 7 issue: #62, #64, #65, #66, #72, #73, #96 | — |
| FR-TRD-001..007 | #100 — E-03 Giao dịch (trading) | 24 issue: #105, #109, #110, #111, #113, #114, #115, #116, #117, #118 … (+14) | — |
| design/trading | #100 — E-03 Giao dịch (trading) | toàn bộ 31 issue lá của epic | Không. Mỗi `SCREEN_ID_SPEC` thành issue FE, mỗi `FUNC_ID_TECH` thành issue BE |
| TRD_DB | #100 — E-03 Giao dịch (trading) | 3 issue: #105, #106, #108 | — |
| ADR-013 | #100 — E-03 Giao dịch (trading) | 8 issue: #102, #105, #106, #109, #114, #118, #135, #136 | — |
| ADR-004 R7 | #100 — E-03 Giao dịch (trading) | phủ gián tiếp qua spec con của feature | Chưa có issue dẫn riêng mã này; việc nằm trong các issue theo màn và RPC của epic |
| FR-ADJ-001..003 | #137 — E-04 Điều chỉnh giao dịch (trade-adjustment) | 17 issue: #141, #142, #143, #144, #145, #146, #148, #149, #150, #151 … (+7) | — |
| design/trade-adjustment | #137 — E-04 Điều chỉnh giao dịch (trade-adjustment) | toàn bộ 22 issue lá của epic | Không. Mỗi `SCREEN_ID_SPEC` thành issue FE, mỗi `FUNC_ID_TECH` thành issue BE |
| ADJ_DB | #137 — E-04 Điều chỉnh giao dịch (trade-adjustment) | 3 issue: #141, #142, #143 | — |
| ADR-006 | #137 — E-04 Điều chỉnh giao dịch (trade-adjustment) | 12 issue: #140, #141, #142, #143, #144, #148, #149, #150, #151, #161 … (+2) | — |
| ADR-005 | #137 — E-04 Điều chỉnh giao dịch (trade-adjustment) | phủ gián tiếp qua spec con của feature | Chưa có issue dẫn riêng mã này; việc nằm trong các issue theo màn và RPC của epic |
| FR-CLS-001..004 | #164 — E-05 Đối soát và chốt sổ (daily-closing) | 20 issue: #169, #170, #171, #173, #174, #175, #176, #177, #178, #179 … (+10) | — |
| design/daily-closing | #164 — E-05 Đối soát và chốt sổ (daily-closing) | toàn bộ 28 issue lá của epic | Không. Mỗi `SCREEN_ID_SPEC` thành issue FE, mỗi `FUNC_ID_TECH` thành issue BE |
| CLS_DB | #164 — E-05 Đối soát và chốt sổ (daily-closing) | 8 issue: #168, #169, #170, #178, #179, #180, #194, #196 | — |
| ADR-005 | #164 — E-05 Đối soát và chốt sổ (daily-closing) | 7 issue: #167, #175, #176, #177, #186, #192, #193 | — |
| ADR-015 | #164 — E-05 Đối soát và chốt sổ (daily-closing) | 8 issue: #166, #173, #175, #183, #184, #185, #191, #195 | — |
| FR-INC-001..003 | #197 — E-06 Tiền thưởng thanh toán đúng hạn và phiên bản 業務規程 (incentive) | 21 issue: #201, #202, #205, #207, #208, #209, #210, #211, #212, #213 … (+11) | — |
| design/incentive | #197 — E-06 Tiền thưởng thanh toán đúng hạn và phiên bản 業務規程 (incentive) | toàn bộ 31 issue lá của epic | Không. Mỗi `SCREEN_ID_SPEC` thành issue FE, mỗi `FUNC_ID_TECH` thành issue BE |
| INC_DB | #197 — E-06 Tiền thưởng thanh toán đúng hạn và phiên bản 業務規程 (incentive) | 6 issue: #201, #202, #204, #206, #228, #230 | — |
| ADR-003 | #197 — E-06 Tiền thưởng thanh toán đúng hạn và phiên bản 業務規程 (incentive) | 11 issue: #200, #201, #205, #209, #211, #212, #213, #215, #226, #227 … (+1) | — |
| ADR-006 | #197 — E-06 Tiền thưởng thanh toán đúng hạn và phiên bản 業務規程 (incentive) | 3 issue: #201, #209, #229 | — |
| FR-DLV-001..005 | #1 — E-07 Giao hàng (delivery) | 16 issue: #2, #5, #236, #237, #238, #239, #240, #241, #242, #243 … (+6) | — |
| design/delivery | #1 — E-07 Giao hàng (delivery) | toàn bộ 23 issue lá của epic | Không. Mỗi `SCREEN_ID_SPEC` thành issue FE, mỗi `FUNC_ID_TECH` thành issue BE |
| DLV_DB | #1 — E-07 Giao hàng (delivery) | 4 issue: #2, #236, #237, #255 | — |
| ADR-006 | #1 — E-07 Giao hàng (delivery) | 1 issue: #239 | — |
| ADR-005 (khóa ngày) | #1 — E-07 Giao hàng (delivery) | phủ gián tiếp qua spec con của feature | Chưa có issue dẫn riêng mã này; việc nằm trong các issue theo màn và RPC của epic |
| FR-NTF-001..003 | #256 — E-08 Thông báo (notifications-rules) | 17 issue: #260, #261, #262, #264, #265, #266, #267, #268, #272, #273 … (+7) | — |
| design/notifications-rules | #256 — E-08 Thông báo (notifications-rules) | toàn bộ 28 issue lá của epic | Không. Mỗi `SCREEN_ID_SPEC` thành issue FE, mỗi `FUNC_ID_TECH` thành issue BE |
| NTF_DB | #256 — E-08 Thông báo (notifications-rules) | 9 issue: #260, #261, #262, #264, #268, #269, #285, #286, #287 | — |
| ADR-007 | #256 — E-08 Thông báo (notifications-rules) | 7 issue: #259, #271, #273, #274, #281, #283, #286 | — |
| FR-RPA-001..007 | #288 — E-09 Báo cáo và kiểm toán (reports-audit) | 31 issue: #292, #293, #294, #296, #297, #298, #299, #300, #302, #303 … (+21) | — |
| design/reports-audit | #288 — E-09 Báo cáo và kiểm toán (reports-audit) | toàn bộ 40 issue lá của epic | Không. Mỗi `SCREEN_ID_SPEC` thành issue FE, mỗi `FUNC_ID_TECH` thành issue BE |
| RPA_DB | #288 — E-09 Báo cáo và kiểm toán (reports-audit) | 11 issue: #290, #292, #293, #298, #300, #302, #307, #313, #325, #330 … (+1) | — |
| AUDIT_DB | #288 — E-09 Báo cáo và kiểm toán (reports-audit) | 6 issue: #291, #294, #309, #310, #311, #334 | — |
| ADR-007 | #288 — E-09 Báo cáo và kiểm toán (reports-audit) | 6 issue: #292, #293, #302, #307, #325, #327 | — |
| ADR-008 | #288 — E-09 Báo cáo và kiểm toán (reports-audit) | 7 issue: #294, #309, #310, #312, #323, #328, #333 | — |
| ADR-001 | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 5 issue: #338, #339, #340, #369, #370 | — |
| ADR-002 | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 14 issue: #342, #343, #344, #346, #349, #354, #356, #357, #358, #359 … (+4) | — |
| ADR-007 | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 5 issue: #351, #352, #353, #354, #368 | — |
| ADR-008 | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 5 issue: #348, #349, #350, #365, #369 | — |
| ADR-010 | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 4 issue: #343, #344, #356, #367 | — |
| CORE_DB | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 6 issue: #345, #346, #347, #366, #373, #375 | — |
| AUDIT_DB | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 3 issue: #348, #349, #350 | — |
| OUTBOX_DB | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 5 issue: #351, #352, #353, #354, #368 | — |
| ARCH-01 | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 8 issue: #338, #339, #340, #356, #360, #363, #370, #374 | — |
| ARCH-05 | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 7 issue: #339, #343, #356, #357, #361, #365, #367 | — |
| api-list §1, §2.1 | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 9 issue: #337, #355, #357, #358, #360, #361, #362, #363, #371 | — |
| error-codes §1 | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 9 issue: #337, #344, #356, #358, #359, #363, #364, #367, #374 | — |
| log-convention | #336 — E-10 Nền tảng chung (khung dự án, DB, RLS và RPC, outbox, audit hash-chain) | 2 issue: #341, #342 | — |
| FR-RPA-008 | #376 — E-11 Di trú dữ liệu ban đầu (FR-RPA-008) | 11 issue: #378, #379, #380, #381, #386, #387, #390, #391, #396, #398 … (+1) | — |
| ADR-014 | #376 — E-11 Di trú dữ liệu ban đầu (FR-RPA-008) | 19 issue: #378, #379, #380, #381, #382, #387, #388, #389, #390, #392 … (+9) | — |
| RPA_MIGRATION_LOAD_TECH | #376 — E-11 Di trú dữ liệu ban đầu (FR-RPA-008) | 20 issue: #377, #378, #379, #383, #385, #386, #387, #388, #389, #390 … (+10) | — |
| RPA_DB §4.3..§4.10 | #376 — E-11 Di trú dữ liệu ban đầu (FR-RPA-008) | 12 issue: #377, #380, #381, #382, #383, #391, #392, #393, #400, #401 … (+2) | — |
| api-list §3 RPA_MIGRATION_* | #376 — E-11 Di trú dữ liệu ban đầu (FR-RPA-008) | 6 issue: #377, #382, #391, #392, #393, #404 | — |
| FR-NTF-004 | #256 — E-08 (ghi chú), #197 — E-06 | không có issue riêng | FR-NTF-004 đã gộp vào FR-INC-002 theo P7 (gộp F-033 vào F-023), nên thành một chức năng ở E-06; E-08 chỉ ghi nhận |
| ADR-012 | — | không có issue | Quy ước trình bày tài liệu LAB-4, không có việc phát triển |
| FR-RPA-008, ADR-014, P17 | #376 — E-11 Di trú dữ liệu | 27 issue lá | Không. FR này ngoài phạm vi LAB-1 nhưng LAB-4 đưa vào |

Cả 47 FR của REQ-001 §4, 42 màn (S-001 đến S-042), 132 API và 15 ADR đều có issue, trừ hai ngoại lệ ở cuối bảng (kiểm bằng script lúc rà cuối: không có FR, màn, API nào bị bỏ sót).

## 3. Hạng mục chịu ràng buộc đặc thù của đề

Mỗi hạng mục dưới đây có issue riêng, không nằm lẫn trong issue CRUD, và được gắn trường `Nhóm đặc thù` trên Project để lọc. Một issue có thể chạm nhiều nhóm; trường `Nhóm đặc thù` ghi nhóm chính, còn cột Issue liệt kê theo nội dung (từ khóa trong nhãn đặc thù của issue).

| Ràng buộc | Issue | Vì sao tách riêng |
|---|---|---|
| 完納奨励金 (thưởng thanh toán đủ đúng hạn), tỷ lệ có phiên bản | 27 issue lá (E-04 1, E-06 15, E-07 9, E-09 2): #2, #4, #151, #201, #202, #205, #206, #207, #208, #209, #210, #217 … (+15) | Tỷ lệ đổi theo phiên bản 業務規程, tính khi khóa ngày và sinh delta khi sửa sau chốt; gộp F-033 vào F-023 (P7, ADR-003). Sai ở đây là sai tiền thưởng, nên tính, vòng đời phiên bản và delta tách ba nhóm việc riêng |
| 業務規程 có phiên bản | 9 issue lá (E-06 7, E-10 2): #211, #214, #215, #220, #222, #223, #227, #347, #375 | Một chợ, quy tắc theo phiên bản có hiệu lực theo ngày (P1, ADR-003). Mọi nghiệp vụ đọc tham số từ một nguồn; nhúng vào từng issue sẽ rải hằng số khắp nơi |
| 許可 và 承認 (gỡ tạm dừng có điều kiện, 再審査) | 17 issue lá (E-01 17): #8, #9, #10, #11, #23, #26, #27, #30, #31, #32, #33, #36 … (+5) | Hai khái niệm khác nhau, hai trạng thái và luật chuyển khác nhau cho 仲卸 và 売買参加者 (P3, P24, ADR-004, BP-a); có job hết hạn hằng ngày |
| 参加上限 (hạn mức mua trong ngày) | 15 issue lá (E-01 4, E-03 11): #23, #28, #46, #50, #106, #109, #111, #114, #118, #124, #127, #131 … (+3) | Kiểm hai lần, lúc tạo và lúc chốt giao dịch, trong cùng chuỗi khóa (P4, P16, ADR-013); sai thì vượt hạn mức hoặc chặn nhầm |
| 締め (chốt sổ) và không chốt khi còn giao dịch pending | 7 issue lá (E-05 7): #173, #174, #175, #183, #185, #191, #193 | Khóa ngày kéo theo nhiều bảng; điều kiện không còn `pending` phải kiểm trong cùng giao dịch (P5, P19, ADR-005, ADR-015) |
| 締め再開 hai người duyệt, chỉ ngày gần nhất trong N ngày | 5 issue lá (E-05 4, E-10 1): #176, #177, #186, #192, #345 | Hai người khác nhau duyệt, giới hạn cửa sổ ngày (P5, P25, ADR-005); luồng riêng với chốt sổ vì quyền, trạng thái và tham số khác |
| Sửa sau chốt chỉ bằng 逆仕訳 hoặc 差額記録 | 12 issue lá (E-04 12): #141, #142, #143, #145, #146, #149, #150, #153, #154, #155, #161, #163 | Không ghi đè dữ liệu đã khóa (P6, ADR-006); bút toán và giá trị hiệu lực là một thiết kế riêng |
| Audit bất biến: trigger chặn sửa/xóa, hash-chain, job kiểm tra hằng ngày | 11 issue lá (E-09 7, E-10 3, E-11 1): #309, #310, #311, #322, #323, #328, #329, #348, #349, #350, #397 | Nền tảng chung cho mọi nghiệp vụ (P11, ADR-008); chuỗi băm và job kiểm tra không thể làm kèm trong issue nghiệp vụ |
| Offline chỉ cho F-006 và F-007; giao dịch và chốt sổ bắt buộc online | 18 issue lá (E-02 18): #65, #66, #67, #70, #71, #72, #73, #82, #83, #84, #85, #86 … (+6) | Chỉ hai chức năng được phép offline (P10, ADR-009): hàng đợi, đồng bộ, FIFO, xung đột; phần còn lại cố ý chặn khi mất mạng |
| Outbox + worker (thông báo, SFTP CSV, retry cho Critical) | 29 issue lá (E-06 1, E-08 14, E-09 9, E-10 5): #204, #260, #261, #262, #263, #268, #269, #271, #272, #273, #274, #275 … (+17) | Gửi tin và xuất tệp tách khỏi giao dịch nghiệp vụ (P12, P23, ADR-007); retry, claim, kết quả muộn là bài toán riêng |
| MFA bắt buộc cho ROLE-005, 006, 007 | 37 issue lá (E-01 7, E-08 9, E-09 11, E-10 7, E-11 3): #14, #15, #20, #21, #41, #52, #55, #264, #265, #266, #267, #277 … (+25) | Mức xác thực aal2 áp lên nhiều RPC và màn (P9, ADR-010); đăng nhập, đăng ký yếu tố, khôi phục thành issue riêng, các màn khác chỉ dùng guard chung |
| Di trú dữ liệu ban đầu (rehearsal, đối chiếu, rollback) | 13 issue lá (E-11 13): #380, #381, #382, #383, #385, #386, #387, #388, #390, #394, #395, #396 … (+1) | Ngoài phạm vi LAB-1; có diễn tập, đối chiếu và rollback (P17, ADR-014); rủi ro cao nhất khi go-live nên có epic riêng E-11 |
| Khóa ngày hai lớp (bổ sung ngoài đề) | 23 issue lá (E-04 3, E-05 7, E-07 10, E-10 2, E-11 1): #5, #144, #160, #162, #169, #170, #178, #187, #189, #190, #194, #236 … (+11) | Chặn ghi vào ngày đã khóa bằng hàm kiểm và trigger, dùng bởi nhiều RPC; tách để một nơi giữ luật |


## 4. Chỗ hở và mâu thuẫn của spec LAB-4 phát hiện khi break

Ghi nhận **210 chỗ hở** (32 đã sửa thiết kế, 58 giả định, 29 tạo issue làm rõ, 91 để mở). Cột "Xử lý" trỏ tới dòng `PREMISE.md` (S-xx là sửa/thêm, G-xx là giả định) hoặc số issue làm rõ. Ghi chú: có 5 dòng khi rà chỉ ghi nhận quyết định đã chốt, không phải chỗ hở thật nên không liệt kê.

| Spec | Chỗ hở/mâu thuẫn | Xử lý |
|---|---|---|
| E-01 · PAU README, api-design/_index | API Design `{API_ID}_API.md` ghi "viết ở LAB-5" nhưng chưa có file nào (lệch L5) | Đã sửa thiết kế: PREMISE S-01 |
| E-01 · PAU_DB §8 và REQ-001 §8 | PAU_DB ghi `open` cho Q2, Q11, Q12, Q13, Q28; REQ-001 ghi `resolved` (chủ dự án 2026-10-14, chờ khách xác nhận) | Để mở: lệch ghi chép, backlog theo REQ-001 vì đó là nơi giữ trạng thái |
| E-01 · ADR-004 R4 và TECH §4.6 #4, Q28 | R4 ghi bác 再審査 thì về 一時停止; TECH và Q28: khởi từ hết hạn thì bác về 失効 | Đã sửa thiết kế: PREMISE S-02 |
| E-01 · FR-PAU-007 | Cột "Vai trò liên quan" ghi ROLE-003 nhưng người duyệt 再審査 là ROLE-005 (TECH §4.6, PAU_DB §5) | Để mở: không ảnh hưởng issue, #33 theo ROLE-005; DOC-01c ghi rõ hợp đồng quyền |
| E-01 · ADR-010 R7 | ROLE-007 duy nhất mất thiết bị thì không ai gỡ được MFA; quy trình khôi phục `[ĐIỀN]` | Tạo issue làm rõ #55 |
| E-01 · TECH §4.7 | Giờ chạy job hết hạn `[ĐIỀN]` (đề xuất 00:05) không có mã Q | Giả định: PREMISE G-07 |
| E-01 · PAU_DB §5, Q8 | ROLE-005 thấy cả `contact` và `basis_no`; phạm vi APPI chờ Q8 (giao LAB-5) | Giả định: PREMISE G-08 |
| E-01 · Q31 | Nơi và thời hạn lưu tệp chứng cứ chưa chốt | Giả định: PREMISE G-09 |
| E-01 · S01: ADR-010 R6, api-list PAU_MFA_VERIFY, PAU_LOGIN_SPEC A3, OQ-2 | Sai MFA lần thứ 3: "quá 3 lần" hay "sau 3 lần"; chỉ tạo challenge mới hay đăng xuất phiên aal1 | Giả định: PREMISE G-10 |
| E-01 · S02: FR-PAU-004 AC2, ADR-004 R6 và TECH §4.6 #4 | "Chỉ job ghi hết hạn" nhưng bác 再審査 khởi từ hết hạn cũng có thể ghi hết hạn (cạnh `review_reject`) | Đã sửa thiết kế: PREMISE S-03 |
| E-01 · S03: PAU_DB §5 `rpc_participant_save` và TECH §4.8 #2 | Điều kiện gia hạn thẳng: căn cứ hiện hành chưa quá hạn, hay hạn hiệu dụng lớn nhất của căn cứ hiện hành và chờ | Đã sửa thiết kế: PREMISE S-04 |
| E-01 · S04: PROFILE_FORM A5, VALIDITY I-3 và ADR-013 R3, R4, R7, PREMISE P16 | FE spec mô tả "mức đã dùng" là pending + confirmed, trong khi api-list `TRD_LIMIT_USAGE_GET` (dòng 115) và ADR-013 R7 đã định nghĩa `used_jpy` gồm cả điều chỉnh | Để mở: FE hiển thị đúng `used_jpy` API trả; #58 ghi cách hiển thị chi tiết khi điều chỉnh khác 0 |
| E-01 · S05: FR-PAU-004 AC7 và EXPIRY_WARNING_SPEC A1, TECH §4.7 #4 | "Còn căn cứ chờ không bị cảnh báo" so với "cảnh báo theo hạn hiệu dụng" | Giả định: PREMISE G-11 |
| E-01 · S06: VALIDITY E-5, api-list PAU_PARTICIPANT_LIST, PAU_DB §4.7 | Một trường `expires_on` hai nghĩa (hạn hiệu dụng và hạn căn cứ hiện hành); view không có căn cứ chờ nên role đọc qua view không tính được hạn hiệu dụng | Để mở: chốt trường và cách lấy ở #58 |
| E-01 · Q89 | Đăng xuất khi mất mạng (`PAU_LOGOUT` không gọi được) chưa định nghĩa | Giả định: PREMISE G-12 |
| E-01 · Q13 | Chỉ chốt người duyệt; nội dung hồ sơ 再審査 và quy tắc gỡ tạm dừng 買出人 vẫn `[ĐIỀN]` | Để mở: #30 giữ quy tắc LAB-1 cho 買出人, #32 nhận ghi chú và tệp hồ sơ; chờ khách |
| E-01 · Q87, Q88 | Hủy căn cứ chờ; khoảng trống giữa hai căn cứ | Giả định: PREMISE G-13 |
| E-01 · FR-PAU-004 AC7, FR-PAU-007 AC8, api-list PAU_PARTICIPANT_UPDATE và REVIEW_DECIDE so với TECH §4.8 #4, #5 | REQ và api-list diễn đạt rộng "ngày hiệu lực mới không muộn hơn hạn cũ + 1 ngày"; TECH chỉ áp khi căn cứ hiện hành còn phủ hôm nay và căn cứ mới bắt đầu ở tương lai | Đã sửa thiết kế: PREMISE S-05 |
| E-02 · README lots §4, api-design/_index | API Design `{API_ID}_API.md` của feature lots ghi "chưa có file (LAB-5)" | Đã sửa thiết kế: PREMISE S-01 |
| E-02 · Q36: REQ-001 §8 và LOT_QUANTITY_RESERVATION_TECH §4.6 #2, LOT_DB §2 và §8, README lots §5 #9, LOT_ATTRIBUTE_CORRECTION_SPEC A7 | REQ-001 ghi Q36 đã chốt (chủ dự án 2026-10-14): hoàn số lượng thì lot `sold` quay về `public`. TECH §4.6 #2 ghi "không có chiều sold → public cho tới khi Q36 trả lời"; LOT_DB §2, §6, §8 còn mở … | Đã sửa thiết kế: PREMISE S-06 |
| E-02 · README lots §5 #9, LOT_DB §8, 6 SPEC | Còn ghi `open` cho Q36, Q48, Q49, Q50, Q71, Q75, Q76; REQ-001 §8 đã `resolved` (chờ khách xác nhận). Các câu còn mở thật của feature: Q5, Q89, OQ-2, OQ-3, OQ-7 và vế "delivered" của Q36 | Để mở: lệch ghi chép, backlog theo REQ-001 |
| E-02 · Q5 (REQ-001 §8) | Thời gian mất kết nối phải chịu, chu kỳ thử lại (đề xuất 15 giây `[ĐIỀN]`), danh sách trình duyệt và tablet; giao LAB-5 | Giả định: PREMISE G-14 |
| E-02 · LOT_INTAKE_FORM_SPEC OQ-3 | Có dùng Background Sync (gửi khi tab đã đóng) không, chưa chốt | Giả định: PREMISE G-15 |
| E-02 · LOT_JUDGMENT_QUEUE_SPEC OQ-2 | Xóa cache danh sách khi tài khoản khác đăng nhập trên thiết bị chung chưa chốt (cache đã khóa theo tài khoản) | Để mở: chốt ở #62 |
| E-02 · LOT_OFFLINE_SYNC_TECH §4.1 #2, §4.2 #2, LOT_INTAKE_FORM_SPEC OQ-7 | Giá trị `schemaVersion` khởi đầu (đề xuất 1) và ngưỡng lệch giờ thiết bị (đề xuất 5 phút) là `[ĐIỀN]` không có mã Q | Giả định: PREMISE G-16 |
| E-02 · LOT_OFFLINE_SYNC_TECH §4.4 #1 và các SPEC (DQ-4) | Khóa request và response (kể cả của `SYNC_DUPLICATE`) ghi "chốt ở LAB-5" | Để mở: chốt ở #62, #63 |
| E-02 · LOT_DB §2 | Điều kiện `sold → delivered` là `[ĐIỀN]` | Để mở: thuộc E-07 (delivery) |
| E-02 · Q89 (REQ-001 §8) | Đăng xuất khi mất mạng chưa định nghĩa | Giả định: PREMISE G-17 |
| E-02 · LOT_JUDGMENT_FORM_SPEC §4.2 và LOT_OFFLINE_SYNC_TECH §4.3 #4, Q35 | JF §4.2 ghi "không chặn lưu khi kết quả sửa giống hiện tại, RPC vẫn ghi audit"; TECH #4 và Q35 trả SYNC_DUPLICATE (không ghi audit) khi cùng grade, note và cùng người sửa | Để mở: ưu tiên nhánh SYNC_DUPLICATE khi cùng người sửa, ghi bản sửa bình thường khi người sửa khác; chốt ở #62, ghi ở #71, #72 |
| E-02 · LOT_QUANTITY_RESERVATION_TECH §4.5, §4.6 và LOT_ATTRIBUTE_CORRECTION_SPEC A2, A3, Q71 | F-009 cộng chênh lệch dương vào `available_qty` (trần chỉ so với `initial_qty`) trong lúc còn giao dịch giữ chỗ; hoàn trả sau đó có thể làm số dư vượt `initial_qty` và vỡ CHECK (TECH coi vượt là dữ liệu hỏng, trả 500) … | Tạo issue làm rõ #99 |
| E-03 · README trading §4, api-design/_index | API Design `{API_ID}_API.md` ghi "viết ở LAB-5", chưa có file | Đã sửa thiết kế: PREMISE S-01 |
| E-03 · Q36: REQ-001 §8 và TRD_CONFIRM_TECH §4.5 #3, TRD_NEGOTIATED_LOT_LIST_SPEC A4, TRD_AUCTION_LOT_LIST_SPEC A1 | REQ-001 ghi Q36 đã chốt (lot đã bán quay về công khai khi hoàn số lượng); TECH ghi "không có chiều sold → public (Q36)", hai SPEC ghi lot `sold` được hoàn vẫn không hiện lại ở danh sách | Đã sửa thiết kế: PREMISE S-07 |
| E-03 · TRD_DB §8, S-014 OQ-4, S-015 OQ-4, S-016 OQ-6, S-018 OQ-5, OQ-6, S-019 OQ-2, OQ-5, S-020 OQ-1 | Còn ghi `open` hoặc chờ khách cho Q2, Q6, Q18, Q20, Q36, Q49, Q70; REQ-001 §8 đã `resolved` cho Q2, Q6, Q18, Q20, Q26, Q69, Q70, Q85 (chờ khách xác nhận) | Để mở: lệch ghi chép, backlog theo REQ-001 |
| E-03 · TRD_AUCTION_RESULT_RECORD_SPEC A3 và PAU_PARTICIPANT_PROFILE_FORM_SPEC A5, so với TRD_NEGOTIATED_CREATE_TECH §4.4 #3, api-list `TRD_LIMIT_USAGE_GET`, ADR-013 R7, S-015 A3 | S-019 A3 và PROFILE_FORM A5 mô tả mức đã dùng chỉ là pending và confirmed; TECH, api-list, ADR và S-015 có thêm tổng điều chỉnh (差額記録) | Để mở: hợp đồng đã có (`used_jpy` gồm ba thành phần); FE hiển thị `used_jpy` của API; chốt cách hiển thị chi tiết ở #102. Cùng chỗ hở với E-01 |
| E-03 · Q2 (REQ-001 §8) và api-list TRD_CREATE, TRD_NEGOTIATED_CREATE_TECH §4.4 | Spec còn thiết kế hai nhánh khi chưa đặt hạn mức (mã `PARTICIPATION_LIMIT_NOT_SET`, "chỉ khi Q2 chọn chặn"); Q2 đã chốt: chưa đặt thì không giới hạn | Đã sửa thiết kế: PREMISE S-08 |
| E-03 · TRD_NEGOTIATED_CREATE_TECH §4.6 #1, TRD_AUCTION_RECORD_TECH §4.5 #1 (DQ-4) | Hai API tạo trả hai dạng response khác nhau (TRD_CREATE: id, trade_code, status, qty, lot; TRD_AUCTION_RECORD: trade_code, remaining); khóa "chốt ở LAB-5" | Để mở: chốt ở #102 |
| E-03 · TRD_DB (trigger), ADJ_LOCKED_DAY_GUARD_TECH | `trades_guard_locked_day` được liệt kê trong TRD_DB nhưng là "component" của TECH ADJ_LOCKED_DAY_GUARD (F-018) | Giả định: PREMISE G-18 |
| E-03 · S-014 OQ-2, OQ-3; S-018 OQ-1 | Chưa có danh mục mặt hàng; thứ tự mặc định của danh sách lot (đề xuất `received_at` tăng); S-018 hỏi sắp theo mã lot hay theo thứ tự lên sàn | Giả định: PREMISE G-19 |
| E-03 · TRD_NEGOTIATED_CREATE_SPEC OQ-3 | Gợi ý bên mua có cần hạn mức **còn lại** từng dòng không (`PAU_PARTICIPANT_LIST` không trả mức đã dùng) | Giả định: PREMISE G-20 |
| E-03 · TRD_AUCTION_HISTORY_SPEC OQ-2, OQ-3, OQ-5 | Phạm vi sự kiện (gộp `adjustment.approve` theo yêu cầu điều chỉnh, có hiện `guard.write_blocked` không), `LOT_SEARCH` khớp chính xác hay một phần | Giả định: PREMISE G-21 |
| E-03 · TRD_CONFIRM_TECH §4.2 (khóa `trades` FOR UPDATE) so với TRD_DB (quy tắc khóa), ADR-013 R5, ADJ_LOCKED_DAY_GUARD_TECH §4.3 (FOR NO KEY UPDATE) | Hai kiểu khóa hàng `trades` cho cùng nhóm RPC đổi trạng thái. Chưa có bằng chứng deadlock của riêng các RPC TRD | Để mở: ghi cả hai nguồn, chốt kiểu khóa ở #103, đồng bộ hợp đồng với E-04 |
| E-03 · TRD_NEGOTIATED_LOT_LIST_SPEC §4.2 D-1, api-list `LOT_SECTION_LIST`, TRD_QUANTITY_LIST (E-02 S-011) | S-014 tìm khớp một phần mã lot hoặc tên hàng (chữ Nhật, Việt); api-list ghi `q` là mã lot; S-011 chỉ tìm mã lot | Để mở: nghĩa của `q` theo từng màn chốt ở #63 (đã thêm dòng); #121 ghi đúng nghĩa của S-014 |
| E-03 · TRD_NEGOTIATED_CREATE_TECH §4.1, TRD_AUCTION_RECORD_TECH §4.1 so với S-015 E-10, S-019 E-8, TRD_DB §4.1 | TECH chỉ yêu cầu `unitPrice` là số nguyên lớn hơn 0 (không có trần) trong khi cột là INTEGER và SPEC chặn ở 2.147.483.647; giá lớn hơn sẽ thành lỗi ép kiểu DB (500) thay vì VALIDATION | Đã sửa thiết kế: PREMISE S-09 |
| E-03 · TRD_CONFIRMATION_LIST_SPEC (bảng trạng thái) so với D-1 và Event | Bảng trạng thái và ảnh chỉ có tab Chờ chốt và Đã từ chối hôm nay, còn D-1, §4.3 và Event M-3 có tab thứ ba Đã chốt hôm nay | Để mở: spec thiếu trạng thái và ảnh cho tab thứ ba; backlog theo D-1 (#126) |
| E-03 · TRD_NEGOTIATED_CREATE_TECH §4.2 #2 và §5 (bảng đồng thời) | "Hai lần gửi đua cùng khóa nối đuôi qua khóa lot" chỉ đúng khi cùng lot; cùng người và cùng khóa nhưng lot khác thì không nối đuôi và tranh UQ lúc INSERT (§5 đã ghi 23505 thành CONFLICT). Suy luận từ hợp đồng khóa … | Để mở: đã ghi vào DoD #110, #136, không đổi thiết kế; #110 ánh xạ đúng vi phạm UQ idempotency thành 409 CONFLICT và rollback giữ chỗ; ca kiểm ở #136 |
| E-03 · TRD_DB (`service_role`, phần thu quyền), ADJ_LOCKED_DAY_GUARD_TECH | TRD_DB giữ thu quyền truncate và delete khỏi `service_role` (từ prototype M5), nhưng chưa nói issue nào làm | Giả định: PREMISE G-22 |
| E-04 · README trade-adjustment, api-design/_index | API Design `{API_ID}_API.md` ghi "viết ở LAB-5", chưa có file | Đã sửa thiết kế: PREMISE S-01 |
| E-04 · ADJ_ADJUSTMENT_DECIDE_TECH §4.2 và api-list `ADJ_REQUEST_CREATE`, so với §4.7 #1 | Response tạo yêu cầu: §4.2 và api-list có `request_code`, §4.7 #1 chỉ ghi `{ok, id, status}`; TECH ghi chốt ở LAB-5 (DQ-4) | Để mở: chốt khóa response ở #139 |
| E-04 · ADJ_ADJUSTMENT_REQUEST_SPEC (thông báo cần thêm), Q34 (REQ-001 §8, đã chốt) | Q34 chặn điều chỉnh tiếp khi giao dịch đã đảo toàn bộ, nhưng chưa có mã thông báo `M_ADJ_*` riêng; TECH chỉ có INVALID_STATE chung | Để mở: chốt mã lỗi và thông báo ở #139; backlog dùng INVALID_STATE (#145) |
| E-04 · ADJ_ADJUSTMENT_DECIDE_TECH §4.1 #2, Q31 | Kiểm tiền tố đường dẫn chứng cứ còn `[ĐIỀN]` theo tên bucket, phụ thuộc Q31 (chính sách lưu trữ) | Để mở: chốt ở #139; Q31 chờ khách; FE không dọn tệp đã tải lên khi người dùng xóa dòng |
| E-04 · ADJ_ADJUSTMENT_DECIDE_TECH §4.3 (FOR NO KEY UPDATE), TRD_CONFIRM_TECH §4.2 (FOR UPDATE) | Hai kiểu khóa hàng `trades` cho các RPC đổi trạng thái; cùng chỗ hở số 11 của E-03 | Để mở: chốt ở #140 cùng #103; DoD #148, 03d dùng FOR NO KEY UPDATE theo TECH ADJ |
| E-04 · ADJ_ADJUSTMENT_DECIDE_TECH §4.4, E-02 (số dư lot) | Q36 đã chốt ở REQ-001 §8 (lot đã bán quay về công khai khi hoàn số lượng) nhưng TECH và LOT_DB còn ghi không có chiều này; riêng trần `initial_qty` khi F-009 cộng dương rồi hoàn chưa chốt (#99) | Đã sửa thiết kế: PREMISE S-10 |
| E-04 · ADJ_ADJUSTMENT_APPROVAL_SPEC OQ-4, OQ-5, OQ-6 (S-022 OQ-4) | Tải thêm bảng J (20 dòng), số dòng danh sách tối đa 100 không có Tải thêm, danh sách chỉ pending không có lịch sử | Giả định: PREMISE G-23 |
| E-04 · ADJ_ADJUSTMENT_APPROVAL_SPEC (G-4), api-list `ADJ_REQUEST_GET`, ADR-013 R7 | Cảnh báo 参加上限 ở màn duyệt: `impact.participation` dùng `participation_used_jpy` chưa gồm bút toán đang duyệt, cộng thêm `amount_delta`; chỉ cảnh báo, không chặn (ADR-013 R7). Công thức dùng chung với E-01, E-03 | Để mở: hợp đồng đã có; #146 dựa vào #106; chi tiết dạng khóa chốt ở #139 |
| E-04 · Q-status: ADJ_DB §8, SPEC OQ, REQ-001 §8 | Một số Q còn ghi `open` ở ADJ_DB và SPEC trong khi REQ-001 §8 đã `resolved` (Q6, Q14, Q18, Q20, Q33, Q34, Q47) | Để mở: lệch ghi chép, backlog theo REQ-001 §8 |
| E-04 · ADJ_LOCKED_DAY_GUARD_TECH §4.2, §4.3 | Trigger lớp 2 raise nên không ghi audit được (rollback); chỉ có log mức WARN. Hai trường hợp khác nhau cho giao dịch confirmed bị sửa số liệu: ngày reopened → DAY_LOCKED, ngày open → INVALID_STATE | Để mở: đã ghi vào DoD #144, #162, không đổi thiết kế; #144 (log `guard.trigger_blocked`, hai nhánh hint) và #162 |
| E-04 · ADJ_ADJUSTMENT_DECIDE_TECH §4.5 #3, #4, INC_POST_LOCK_DELTA_TECH §4.1 | Điều kiện tạo delta: "giao dịch có dòng original", không phải `is_post_lock`; ngày gốc reopened đã có original vẫn cần delta; logic delta thuộc E-06 | Để mở: đã ghi vào DoD #151, không đổi thiết kế; #151 (phụ thuộc E06-INC-DB, E06-INC-POST-LOCK-DELTA); thứ tự khóa advisory incentive sau ngày, trước audit |
| E-04 · TRD_DB (trigger `trades_guard_locked_day`), REQ-001 FR-TRD-007 AC7 và Q85, ADJ_LOCKED_DAY_GUARD_TECH §4.2 | TRD_DB chặn INSERT `trades` vào ngày `reopened` của hôm qua trở về trước (chỉ hôm nay được); GUARD §4.2 không liệt kê nhánh này | Đã sửa thiết kế: PREMISE S-11 |
| E-04 · REQUEST §4.2 (G-5, G-7), ADJ_DB §4.2 | Miền yêu cầu cho phép qty tới 10^9 và đơn giá tới 2.147.483.647, tích tới khoảng 2,1 nhân 10^18, vượt miền `amount_delta` NUMERIC(18,3) (phần nguyên tối đa khoảng 10^15) nên có thể thành 500 | Để mở: chốt cách xử lý ở #139 (không tự đặt trần mới); ca biên ở #145, #142 |
| E-04 · REQUEST §6 (J-1..J-8), APPROVAL §6 (D-1..D-11) | S-022 cần `requested_at` giảm dần, S-023 cần tăng dần; `originDayStatus=locked/open` là nhóm hai trạng thái; api-list chưa nêu thứ tự | Để mở: chốt ở #139; DoD ở #146, #157 |
| E-04 · ADJ_DB §4.1 (`request_code`) | Giá trị mặc định dùng `lpad(...,6,'0')` cắt số dài hơn 6 ký tự (1000000 thành 100000) trong khi mô tả nói thêm chữ số khi vượt 999999 | Đã sửa thiết kế: PREMISE S-12 |
| E-04 · LOT_DB §6 (`lot_release_qty`), E02-BE-08 so với ADJ_ADJUSTMENT_DECIDE_TECH §4.5 #2 | Helper ghi `p_qty = trades.qty` cho giao dịch pending; điều chỉnh gọi với `−qty_delta` hoặc `qty_before` của giao dịch confirmed | Đã sửa thiết kế: PREMISE S-13 |
| E-04 · ADJ_ADJUSTMENT_DECIDE_TECH §4.5, §4.7 so với INC_POST_LOCK_DELTA_TECH §4.5 | Response và audit duyệt: DECIDE ghi `incentive_delta_jpy`, response không có phần thưởng; DELTA ghi `incentive {status, incentive_jpy, rule_version_id}` và audit có `incentive_delta {…}`; cả hai cập nhật 14/10/2026 | Để mở: chốt ở #140; #151 trả kết quả có cấu trúc cho #150 |
| E-04 · ADJ_ADJUSTMENT_DECIDE_TECH §4.4, §4.5 #6 so với INC_POST_LOCK_DELTA_TECH (lỗi NO_OPEN_BUSINESS_DAY) | DECIDE chỉ trả object; DELTA ghi audit `guard.write_blocked` rồi trả object; entity là `adjustment_request` (DELTA) hay `trade_adjustment_request` (DECIDE) | Để mở: chốt ở #140 |
| E-04 · ADJ_LOCKED_DAY_GUARD_TECH §4.4, error-codes §1, ADJ_LOCKED_DAY_BLOCK_SPEC E-1, E-2 | `hint` không hợp lệ hoặc `details` không parse được: GUARD ghi 500 INTERNAL_ERROR; BLOCK ghi fallback ngày từ màn chủ khi params rỗng | Để mở: chốt ở #140 cùng E10-API-ERROR-MAPPING |
| E-05 · README daily-closing, api-design/_index | API Design `{API_ID}_API.md` ghi "viết ở LAB-5", chưa có file | Đã sửa thiết kế: PREMISE S-01 |
| E-05 · REQ-001 §8 Q32 (resolved, chờ khách xác nhận) so với CLS_DB §4.1 và "Câu hỏi mở", CLS_DISPUTE_LIST_SPEC §6 A1 và OQ-1, CLS_DISPUTE_DETAIL_SPEC §6 A2, F-2, F-3 | Q32 đã trả lời "gắn vào ngày mở kế tiếp, có tham chiếu giao dịch gốc". Spec vẫn thiết kế chặn tạo khi ngày hiện tại khóa (DAY_LOCKED), ghi Q32 còn `open`, và không có cột hay bảng tham chiếu giao dịch (đối tượng là văn bản tự do … | Tạo issue làm rõ #196 |
| E-05 · REQ-001 §8 Q21 (open, giao Tech Lead chốt ở LAB-5), ADR-015 §4, CLS_DAY_CLOSE_TECH | Cần cảnh báo "còn giao dịch chờ chốt, chưa chốt sổ" trước giờ chốt nhưng không có job, loại sự kiện hay màn nào định nghĩa | Tạo issue làm rõ #195 |
| E-05 · CLS_DAILY_RECONCILIATION_SPEC §4.3, §6 A1, `database-design/_index.md` §5 (`rpc_reconciliation_overview`) | Không có TECH riêng cho `rpc_reconciliation_overview`: quy tắc chọn ngày mặc định, tab, keyset, các khóa `summary` chỉ ở SPEC; khóa response là đề xuất (DQ-4, OQ-12) | Để mở: chốt hợp đồng ở #166; DoD #173, 02b lấy từ SPEC |
| E-05 · CLS_DAY_CLOSE_TECH 4.4, 4.5; CLS_DAY_REOPEN_TECH 4.6; CLS_DISPUTE_*_SPEC §4.3 (DQ-4) | Tên khóa response và request của 10 API đều là "đề xuất, chốt ở LAB-5" | Để mở: chốt ở #166, 01b, 01c |
| E-05 · S-025 OQ-1, OQ-6, OQ-9, OQ-10; CLS_DAY_CLOSE_TECH (Q14, Q21, Q22); CLS_DAY_REOPEN_TECH (Q1, Q14, Q22, Q23, Q-R3); S-027 OQ-6 | Còn ghi `open` hoặc "giả định" cho Q1, Q14, Q22, Q23, Q37, Q52 trong khi REQ-001 §8 đã `resolved` (chờ khách xác nhận): N = 3, giữ bản gốc cộng delta, đồng ý mở rộng loại sự kiện, ≥ 2 ROLE-005, mọi ROLE-007 active … | Để mở: lệch ghi chép, backlog theo REQ-001 §8 |
| E-05 · CLS_DAY_CLOSE_TECH §5 (RPC giao dịch khóa `trades` FOR NO KEY UPDATE) so với TRD_CONFIRM_TECH §4.2 (FOR UPDATE) | Nguồn thứ ba cho kiểu khóa hàng `trades` của nhóm RPC giao dịch, cùng chỗ hở số 11 của E-03 và số 5 của E-04. TECH chốt sổ nêu thứ tự khóa của các RPC giao dịch theo FOR NO KEY UPDATE | Để mở: chốt cùng ở #103 và #140; E05 không khóa `trades` (chỉ đếm), nên không bị ảnh hưởng trực tiếp |
| E-05 · ADR-015 R6, ADR-005 R9, Q23 (resolved) | Điều kiện nhân sự (≥ 2 ROLE-005, ≥ 1 ROLE-003 mỗi ca chốt) là điều kiện vận hành, hệ thống không tự kiểm | Để mở: không có hành vi phần mềm nên không thành issue; đưa vào rủi ro ở báo cáo tiến độ (ROLE-003 vắng thì không chốt được) |
| E-05 · CLS_DAILY_RECONCILIATION_SPEC OQ-7; CLS_DISPUTE_DETAIL_SPEC OQ-5 | Không có hộp thoại xác nhận khi duyệt 締め再開 (OQ-7) và khi đóng tranh chấp (OQ-5); chưa có mã message | Giả định: PREMISE G-24 |
| E-05 · CLS_DISPUTE_DETAIL_SPEC OQ-1, §6 "Khác LAB-1" | Có cần sửa nguyên nhân, người chịu trách nhiệm, ngày dự kiến sau khi tạo (LAB-1 A-1) | Giả định: PREMISE G-25 |
| E-05 · CLS_DISPUTE_DETAIL_SPEC (Q31), CLS_DB `evidence_paths` | Bucket, thời hạn lưu, lưu trữ lạnh chứng cứ chưa chốt (Q31); kiểm đường dẫn thuộc người gọi còn `[ĐIỀN]` | Để mở: cùng #139; ghi ở #168, #178 |
| E-05 · CLS_DAILY_RECONCILIATION_SPEC §2 (ảnh), §6 bảng trạng thái | Trạng thái `reopened` của S-025 không có ảnh wireframe; chỉ mô tả bằng bảng "Hiển thị theo trạng thái ngày" | Để mở: DoD #183 theo bảng spec; không ảnh để đối chiếu thị giác |
| E-05 · CLS_REOPEN_DECIDE (api-list 0.6.0 bỏ `DAY_REOPEN_NOT_ALLOWED`, 0.7.0 và 0.8.0 thêm lại) | Lịch sử sửa nguồn: bản 0.6.0 nói CLS_REOPEN_DECIDE không có mã này, nay có cho nhánh "ngày sau chưa open" (N vẫn không kiểm lại lúc duyệt) | Để mở: đã ghi vào DoD #167, #177, không đổi thiết kế; #177 và #167 ghi hai nhánh; không cần quyết định thêm |
| E-05 · CLS_DB §4.1, Trigger (`disputes_guard_closed`), CLS_DB §4.2 | `rpc_dispute_update` chèn vào `dispute_updates` mà không UPDATE `disputes`, nên trigger đóng trên bảng cha không chặn được update đua với close; CLS_DB chỉ nói "RPC chặn khi closed", không nêu cơ chế khóa | Đã sửa thiết kế: PREMISE S-14 |
| E-05 · CLS_DAILY_RECONCILIATION_SPEC §4.3 (H-12), §6 "Nội dung tab" | Chỉ tab trades có keyset theo id tăng dần; các tab deliveries, exceptions, disputes (tab 3 có hai bảng, mỗi bảng "Tải thêm") chưa nêu khóa sắp xếp và cursor riêng | Để mở: chốt ở #166; DoD #184 ghi cursor và nút riêng từng bảng |
| E-05 · OUTBOX_DB §4.1.1 (`dispute_opened`), CLS_DISPUTE_DETAIL_SPEC §6 A4 | Cờ Critical và lượt thử của `dispute_opened` phụ thuộc cấu hình thông báo (Critical thì 4, thường thì 1); spec tranh chấp không nêu | Để mở: ghi tường minh ở #178, chốt cùng E-08 |
| E-06 · README incentive, api-design/_index | API Design `{API_ID}_API.md` ghi "viết ở LAB-5", chưa có file | Đã sửa thiết kế: PREMISE S-01 |
| E-06 · REQ-001 §8 Q45 (resolved, chờ khách xác nhận: "không hiện dòng thưởng = 0, chỉ liệt kê giao dịch đủ điều kiện") so với INC_INCENTIVE_CALCULATE_TECH §4.4 bước 6, INC_DB §4.1, INC_CALCULATION_RESULT_SPEC (E-3, G-1, G-8, Q45 còn open), INC_POST_LOCK_DELTA_TECH §4.4 bước 3 và Q56 | Thiết kế ghi dòng `original` bằng 0 cho giao dịch không đúng hạn và hiện thẻ, chip lọc "Không đúng hạn"; Q56 (đã chốt) cần dòng `original` để ghi `delta` 0. Q45 hỏi hiển thị ở báo cáo, không quyết định bỏ lưu dòng 0 | Tạo issue làm rõ #230 |
| E-06 · REQ-001 §8 Q30 (resolved, chờ khách xác nhận: tham số vận hành 休市日 và N ngày 締め再開 tách riêng, không tính vào hạn mức 4 lần mỗi năm) so với INC_RULE_VERSIONING_TECH §5 (Q30 còn mở), S-030 H-3, H-4, A3, Q17 | Spec vẫn để `market_holidays` và `reopen_window_days` trong `params` của `market_rule` và đếm chung vào hạn mức | Tạo issue làm rõ #231 |
| E-06 · S-028 OQ-6, OQ-1..; INC_INCENTIVE_CALCULATE_TECH (Q14, Q25, Q26, Q45, Q46); INC_DB (Q14, Q25, Q26, Q33, Q56, Q46, Q45); S-029, S-030 (Q15, Q58, Q59) | Còn ghi `open` hoặc "chờ" cho `M_INC_016..019` (nay đã có ở error-codes), Q14, Q25, Q26, Q33, Q46, Q56, Q81, Q82, Q83, Q15, Q58, Q59 trong khi REQ-001 §8 đã `resolved` | Để mở: lệch ghi chép, backlog theo REQ-001 §8 |
| E-06 · CORE_DB §4.4 ("Trigger / hàm": `active_rule_version`, `job_rule_version_activate`, `rule_versions_guard`, hai chỉ mục) so với INC_RULE_VERSIONING_TECH §4.6, §4.7 | Hai nguồn cùng mô tả hàm tra phiên bản và job kích hoạt | Giả định: PREMISE G-26 |
| E-06 · INC_POST_LOCK_DELTA_TECH §4.5 so với ADJ_ADJUSTMENT_DECIDE_TECH §4.5, §4.7 | Response và audit duyệt: DELTA trả `incentive {status, incentive_jpy, rule_version_id}` và audit `incentive_delta {…}`; DECIDE ghi `incentive_delta_jpy` (cùng chỗ hở 21 của E-04) | Để mở: chốt ở #140 và #199; #209 trả kết quả có cấu trúc cho #150 |
| E-06 · S-028 OQ-5, G-11 | Wireframe hiện `qty × unit_price` lúc khóa nhưng `incentive_results` chỉ lưu `base_amount` | Giả định: PREMISE G-27 |
| E-06 · S-029 OQ-4, G-6 | Ngoài trục (chờ duyệt, bị từ chối) không có "Tải thêm"; bản `rejected` tích lũy | Giả định: PREMISE G-28 |
| E-06 · S-030 OQ-6, OQ-7, G-3, G-6, G-7; INC_RULE_VERSIONING_TECH §4.3 | Không có hộp xác nhận khi duyệt và khi hủy; rollback: S-030 chỉ cho từ bản `superseded` nhưng RPC chấp nhận `active` và `superseded` | Giả định: PREMISE G-29 |
| E-06 · INC_RULE_VERSIONING_TECH Q-RUL-T2 | Lịch dự phòng khi lần chạy 00:05 JST của job kích hoạt lỗi (chạy lại mỗi giờ?) còn mở; chỉ có cảnh báo `job_failed` | Để mở: chốt ở #200 |
| E-06 · S-028 Q-INC-R1 (REQ-001 Q81, resolved) | Sau chạy lại thành công phải nhắc ROLE-005 sinh lại báo cáo tay; chưa có mã message cho lời nhắc | Để mở: nội dung nhắc chốt ở #199, hiển thị ở #219 |
| E-06 · S-029 Q23, S-030 Q23 (resolved), ADR-003 | Số ROLE-006 tối thiểu mỗi ca để duyệt hai người là điều kiện vận hành, hệ thống không tự kiểm | Để mở: không có hành vi phần mềm nên không thành issue; đưa vào rủi ro ở báo cáo tiến độ. Lưu ý: Q23 (REQ-001) chỉ chốt ≥ 2 ROLE-005 và ≥ 1 ROLE-003 ở ca chốt sổ, chưa trả lời số ROLE-006 tối thiểu |
| E-06 · REQ-001 §8 Q90, Q91 (open) | Q90: làm tròn từng dòng hay tổng ở báo cáo (RPA_DB); Q91: phiên bản tỷ lệ và 業務規程 có phải loại bản ghi di trú | Để mở: thuộc E-09 và E-11, không thuộc E-06; nhưng Q91 ảnh hưởng việc nạp phiên bản trước go-live và 2 trong 4 lượt năm đầu nếu nhập tay, nên ghi ở rủi ro |
| E-06 · INC_INCENTIVE_CALCULATE_TECH §4.1, INC_DB (RLS) | Hàm `worker_incentive_run_begin`, `worker_incentive_run_fail` do worker (service role) gọi; ai viết vòng lặp worker (OUTBOX_DB, NTF) không nêu rõ | Giả định: PREMISE G-30 |
| E-06 · INC_RULE_VERSIONING_TECH §3, §4.4, FR-INC-002 AC4 | Một số bản `scheduled` bị hủy sau khi duyệt vẫn tính vào hạn mức (Q59); dễ gây hiểu nhầm là "trả lượt" ở màn | Để mở: đã ghi vào DoD #212, #232, không đổi thiết kế; DoD #212, #232 (hủy) ghi rõ; không cần quyết định thêm |
| E-06 · INC_CALCULATION_RESULT_SPEC §6 A2, INC_INCENTIVE_CALCULATE_TECH §4.1 bước 2b, INC_DB §4.2, REQ-001 Q82 | Điều kiện dòng `running` bị coi là treo: S-028 A2 ghi ngưỡng đề xuất 15 phút chỉ theo tuổi; TECH ghi quá 5 phút và outbox không còn `retry_wait`; INC_DB chỉ nêu tuổi; Q82 chỉ chốt con số 5 phút | Để mở: chốt một điều kiện dùng chung ở #199; BE-01a, BE-02, BE-03 dùng cùng điều kiện |
| E-06 · INC_POST_LOCK_DELTA_TECH §4.3 (bảng Error và Detail) | Bảng Error có điều kiện `confirmed_at` không muộn hơn `locked_at` của lần khóa gần nhất, bước Detail không ghi; giao dịch xác nhận sau lần khóa đó (ví dụ lúc ngày reopened) chưa có trạng thái | Để mở: chốt ở #199; ghi ở #209 |
| E-06 · INC_POST_LOCK_DELTA_SPEC E-5 và §6 A3, F-3 | E-5 \"thiếu tỷ lệ gốc\" đếm mọi bút toán không có delta, còn A3 và F-3 tách thiếu tỷ lệ khỏi chờ job bù (deferred) | Đã sửa thiết kế: PREMISE S-15 |
| E-06 · api-list INC_DELTA_LIST (query `dayId`) so với INC_POST_LOCK_DELTA_SPEC §4.2, §4.3 | api-list nhận `dayId`; S-031 không nhận ngày | Để mở: chốt API bỏ qua hay từ chối `dayId` ở #199 |
| E-06 · INC_RULE_VERSIONING_TECH §4.5, §5 (bảng đồng thời); INC_INCENTIVE_CALCULATE_TECH §4.7, §5 | Bảng đồng thời ghi bên sau `INVALID_STATE` cho duyệt đua với hủy và cho hai lần chạy lại, nhưng bảng lỗi cho phép hủy bản `scheduled` tương lai và cho chạy lại ở `rate_missing` | Để mở: ma trận theo thứ tự thao tác ở #228, chốt ở #199, 01b |
| E-06 · REQ-001 FR-INC-002 AC6, Q17 so với Q30 | REQ-001 tự mâu thuẫn: lịch 休市日 là tham số `market_rule` tiêu lượt (AC6, Q17) hay tách riêng không tiêu lượt (Q30) | Tạo issue làm rõ #231 |
| E-06 · INC_RATE_VERSION_DETAIL_SPEC H-5, INC_RULE_VERSIONING_TECH §5, CORE_DB | `default_participation_limit_jpy` cho phép null (không có mặc định) nhưng H-5 chỉ mô tả số nguyên không âm | Để mở: chốt cách nhập và hiển thị null (không đổi thành 0) ở #200 |
| E-06 · INC_RULE_VERSIONING_TECH §4.4 (CONFLICT `params`), error-codes M_INC_015 | `CONFLICT` từ chỉ mục duy nhất có `params` rỗng nhưng M_INC_015 cần hai tham số | Để mở: chốt message thay thế ở #200 |
| E-06 · ADR-002 R8 | Quyền thực thi của hàm worker và job (begin, fail, job tính, job kích hoạt) | Để mở: đã ghi vào DoD #204, #215, #226, #227, không đổi thiết kế; DoD #204, #215, #226, #227 |
| E-07 · README delivery, api-design/_index | API Design `{API_ID}_API.md` ghi "viết ở LAB-5", chưa có file | Đã sửa thiết kế: PREMISE S-01 |
| E-07 · REQ-001 §8 Q40 (resolved, chờ khách xác nhận: "giữ hiện tại, không tự đổi giao hàng, ROLE-004 đóng bằng ngoại lệ") so với DLV_DELIVERY_RECORD_TECH §4.5 bước 3, S-033 A8, DLV_DB §8, error-codes Q13 | Spec còn ghi Q40 `open` và "tạm"; hành vi thiết kế đã là phương án đã chốt | Để mở: lệch ghi chép, backlog theo REQ-001 §8 (không cần issue làm rõ) |
| E-07 · REQ-001 §8 Q92 (open) | Số lượng ngoại lệ (Q39 đã chốt) có bị chặn vượt phần còn lại hoặc buộc khớp theo loại; thiết kế chỉ kiểm lớn hơn 0 | Tạo issue làm rõ #254 |
| E-07 · api-list §1, DLV_PART_RECORD (QA-8, G24), DLV_DELIVERY_RECORD_TECH §5 và Q-DLV-T3 | Idempotency cho ghi lần giao chỉ là đề xuất, chưa có cột hay chỉ mục duy nhất; gửi lại sau timeout thành lần giao mới | Tạo issue làm rõ #255 |
| E-07 · DLV_EXCEPTION_FORM_SPEC OQ-2 so với DLV_DB 0.3.0 (§4.3 #5) | OQ-2 ghi độ dài `reason` còn đề xuất và "DB chưa có CHECK"; DLV_DB đã có CHECK tối đa 500 ký tự | Để mở: lệch ghi chép, backlog theo DLV_DB |
| E-07 · REQ-001 §8 Q31 (open), DLV_DB §4.3 `evidence_paths` | Bucket, thời hạn lưu, dọn tệp mồ côi chưa chốt; kiểm đường dẫn thuộc người gọi còn `[ĐIỀN]` | Để mở: cùng #139; ghi ở #235, #240 |
| E-07 · REQ-001 §8 Q5 (open), DLV_DELIVERY_LIST_SPEC OQ-3, DLV_DB §6 | Ngưỡng và đơn vị "giao hàng tồn đọng" chưa có; job `DLV_JOB_OVERDUE_SCAN` thuộc FR-NTF-001 | Giả định: PREMISE G-31 |
| E-07 · REQ-001 §8 Q29, Q41 (open), DLV_DB §7 | Header `deliveries.csv` và đợt di trú chưa biết nên chưa thể chốt mã giao hàng khi nạp | Để mở: thuộc E-11, ghi ở rủi ro; #2 chỉ định nghĩa mã sinh từ sequence |
| E-07 · DLV_SETTLEMENT_CROSSCHECK_SPEC OQ-3 | E-7 không hiện loại bút toán: `DLV_CROSS_REF` chỉ trả `adjustment_count`, `last_adjusted_at`; `DLV_GET` có `adjustments[]` nhưng ROLE-005 không gọi được | Giả định: PREMISE G-32 |
| E-07 · DLV_SETTLEMENT_CROSSCHECK_SPEC OQ-4, OQ-6 | Xem tệp chứng cứ từ màn tra cứu và nút "Tải thêm" cho lot hơn 20 giao dịch chưa có (wireframe thiếu View ID) | Để mở: DoD #248, 05b ghi là chờ quyết định; API đã có cursor |
| E-07 · DLV_EXCEPTION_FORM_SPEC OQ-3, A6 | Danh mục nhóm lý do theo loại (F-4) chưa có | Để mở: F-4 chỉ là trợ giúp nhập, không có cột; chờ khách |
| E-07 · DLV_DELIVERY_RECORD_SPEC OQ-3, A6 | Độ dài ghi chú lần giao 200 ký tự chốt ở spec, chưa có nguồn khách | Giả định: PREMISE G-33 |
| E-07 · DLV_DB §5, `_index` §5.2 | Policy SELECT của `lots` và `trades` phải thêm ROLE-004 cho màn giao hàng, nhưng hai bảng thuộc E-02 và E-03 | Giả định: PREMISE G-34 |
| E-07 · DLV_DB §4.1 #2, DLV_DELIVERY_RECORD_TECH §4.1 | Bảng thuộc E-07 nhưng INSERT nằm trong `rpc_trade_confirm` (E-03) | Để mở: đã ghi vào DoD #2, #115, không đổi thiết kế; #115 phụ thuộc #2; E-07 không có issue tạo giao hàng |
| E-07 · DLV_EXCEPTION_LIST_SPEC §4.1 E-1 so với §4.2 | E-1 ghi "mã giao dịch" (placeholder TX-…) nhưng dùng chung tham số `q` khớp cả mã giao hàng, mã giao dịch, mã lot | Để mở: ghi ở #234; #243 theo hành vi của `q` |
| E-07 · DLV_SETTLEMENT_CROSSCHECK_SPEC §4.3, §5 (D-3), G-1 so với api-list DLV_CROSS_REF, REQ-001 FR-DLV-004 AC3 | AC3 và api-list nói chung "không có liên kết thì rỗng"; SPEC phân biệt mã hoặc giao dịch không tồn tại (items rỗng) với giao dịch có nhưng chưa có giao hàng (`delivery` null, vẫn hiện thẻ giao dịch) | Để mở: chốt hai nhánh ở #234; DoD #241, #253 |
| E-07 · DLV_EXCEPTION_FORM_SPEC §5 (Error Handling của H-5) so với F-3, Q39 | Bảng lỗi chỉ nêu `fields.exceptionType`, `reason`, `evidencePaths`, thiếu `fields.qty` dù F-3 bắt buộc theo Q39 | Đã sửa thiết kế: PREMISE S-16 |
| E-07 · DLV_DELIVERY_RECORD_TECH §4.4 bước 3, §4.6 (trigger → 500) so với ADJ_LOCKED_DAY_GUARD_TECH §4.4 và bảng "Trigger anh em" | Lỗi trigger của `delivery_parts` và `delivery_exceptions`: TECH delivery ghi 500, TECH guard dùng chung hint và detail để ánh xạ 409 | Để mở: chốt ở #235 cùng E10-API-ERROR-MAPPING |
| E-07 · DLV_DELIVERY_RECORD_SPEC §4.3 (Data Mapping) so với DLV_DELIVERY_RECORD_TECH §4.2, §4.6 | SPEC ghi `qty` dạng số và `completed_at` là `now()`; TECH ghi chuỗi và `clock_timestamp()` | Để mở: theo TECH vì `completed_at` là mốc 完納 của E-06; ghi ở #235 |
| E-07 · DLV_DELIVERY_LIST_SPEC §4.1 F-5, DLV_DELIVERY_RECORD_SPEC §4.1 F-1 | Tiến độ chia cho `qty_effective`; với 逆仕訳 hoặc Q40 mẫu số có thể 0 (NaN, vô cực) | Để mở: chốt hiển thị ở #234; ghi ở #242, #4 |
| E-07 · DLV_DELIVERY_RECORD_TECH §4.3, §4.4 so với §4.6 bước 4 (thứ tự kiểm ngoại lệ) | Ngoại lệ dùng cùng bước 4.3, 4.4 nên tồn tại và trạng thái cuối được xét trước ngày | Để mở: đã ghi vào DoD #240, #251, không đổi thiết kế; DoD #240 viết rõ thứ tự, #251 kiểm ca giao hàng đã đóng và ngày khóa |
| E-07 · DLV_EXCEPTION_LIST_SPEC §4.2 (E-2) | Server từ chối status ngoài `waiting` và `in_progress` là ràng buộc của màn S-034, không phải của `DLV_LIST` (S-032 dùng bốn trạng thái) | Để mở: đã ghi vào DoD #234, không đổi thiết kế; ghi ở #234 |
| E-08 · README notifications-rules, api-design/_index | API Design `{API_ID}_API.md` ghi "viết ở LAB-5", chưa có file | Đã sửa thiết kế: PREMISE S-01 |
| E-08 · REQ-001 §8 Q3 (open) | Nhà cung cấp email, người nhận mặc định, loại Critical mặc định chưa có | Tạo issue làm rõ #286 |
| E-08 · REQ-001 §8 Q5 (open), NTF_CRITICAL_RETRY_TECH §4.5, DLV_DELIVERY_LIST_SPEC OQ-3 | Đơn vị của `threshold_days` cho `delivery_overdue`, ngưỡng `outbox_stale` (đề xuất 10 phút) và hành vi khi ngưỡng rỗng chưa có | Tạo issue làm rõ #285 |
| E-08 · REQ-001 §8 Q8, Q44 (open), NTF_DB §4.3, §4.4, S-037 OQ-7 | Thời hạn lưu `notifications` và `notification_send_logs`, quy tắc che email trong lịch sử | Tạo issue làm rõ #287 |
| E-08 · api-list §3 (`NTF_JOB_OUTBOX_DISPATCH`, FR-NTF-001, 002), OUTBOX_DB, ADR-007 R2, R3 so với khóa tạm `E10-OUTBOX (outbox và worker)` đã dùng ở E-01..E-07 | Worker gửi thuộc FR-NTF-001, 002 (E-08), còn bảng outbox và hàm phát thuộc E-10; E-06 chỗ hở 14 ghi "vòng lặp worker thuộc E-10" | Giả định: PREMISE G-35 |
| E-08 · api-list §3 (`DLV_JOB_OVERDUE_SCAN`, FR-NTF-001), DLV_DB §6 | Job quét giao hàng tồn đọng mô tả ở feature delivery nhưng thuộc FR-NTF-001 | Giả định: PREMISE G-36 |
| E-08 · NTF_DB §8 (Q22, Q24), NTF_CRITICAL_RETRY_TECH (Q68, Q-N3, Q-N4), README | Còn ghi `open` hoặc "ngoài phạm vi" cho Q22, Q68, Q77, Q79 trong khi REQ-001 §8 đã `resolved` (Q22, Q37, Q62, Q68, Q77, Q79) | Để mở: lệch ghi chép, backlog theo REQ-001 §8 |
| E-08 · S-037 OQ-4, NTF_CONFIG_SAVE | Đua ghi cấu hình khi hai ROLE-007 cùng sửa: không có `CONFLICT`, ghi sau thắng | Giả định: PREMISE G-37 |
| E-08 · S-037 OQ-9, NTF_DB §4.1 | DB không CHECK `send_time` thuộc {08:00, 17:00} và cặp (loại phát ngay, `send_time` rỗng); chỉ route kiểm | Để mở: chốt ở #258, #260 |
| E-08 · S-037 OQ-8, OUTBOX_DB §4.2 | Mức `severity` mặc định theo từng `alert_type` chưa chốt | Để mở: chốt ở #258 |
| E-08 · S-037 OQ-2, OQ-5, OQ-6 | Số người nhận tối đa mỗi loại, khoảng tối đa lọc lịch sử, có dialog khi xác nhận cảnh báo | Giả định: PREMISE G-38 |
| E-08 · NTF_CRITICAL_RETRY_TECH §3 (nhóm nội bộ) | Backoff 1 phút và 5 phút của sự kiện nội bộ là "đề xuất", chưa chốt | Để mở: chốt ở #259 |
| E-08 · ADR-007 R2, NTF_CRITICAL_RETRY_TECH §4.4 | Lịch `pg_cron` theo giây cần phiên bản từ 1.5, "kiểm ở spike LAB-5" | Để mở: đã ghi vào DoD #271, không đổi thiết kế; DoD #271 có ca spike |
| E-08 · NTF_DB §4.3 (`title`, `body`), S-037 | Mẫu câu chữ tiêu đề và nội dung thông báo còn `[ĐIỀN]` | Để mở: chốt ở #259 |
| E-08 · REQ-001 §8 Q4 (open), NTF_CRITICAL_RETRY_TECH | SFTP có chạy được trên Deno không (spike), host, tên tệp, lịch | Để mở: thuộc E-09; ghi ở #274 |
| E-08 · NTF_CRITICAL_RETRY_TECH §4.3 bước 3, NTF_DB §4.4, FR-NTF-002 AC2, AC5 | "Chỉ gửi người chưa success" không phân biệt kênh, trong khi log theo (kênh, người): in_app success sẽ chặn retry email | Giả định: PREMISE G-39 |
| E-08 · NTF_CRITICAL_RETRY_TECH §4.4 lỗi "không còn processing" | Không nhận diện kết quả muộn của lần claim cũ khi lần claim mới cũng đang processing | Giả định: PREMISE G-40 |
| E-08 · NTF_CRITICAL_RETRY_TECH §4.3 bước 4, INC_INCENTIVE_CALCULATE_TECH §4.1 (2a) | Handler `business_day_locked` mô tả cặp job, thiếu `worker_incentive_run_begin`/`fail` và nhánh bỏ qua job | Giả định: PREMISE G-41 |
| E-08 · NTF_CRITICAL_RETRY_TECH §4.4, §5 | Phép 260 giây giả định T là thời gian xử lý một attempt; chưa nói ngân sách khi nhiều người nhận hoặc 100 sự kiện | Để mở: chốt ngân sách mỗi attempt ở #259 |
| E-08 · S-037 Data Mapping NTF_OPS_ALERT_LIST | Tham số `acknowledged` vừa "false mặc định" vừa "bỏ trống = tất cả" | Giả định: PREMISE G-42 |
| E-08 · OUTBOX_DB §4.1 (`next_attempt_at`), NTF_CRITICAL_RETRY_TECH §4.4 | Backoff nội bộ [1,5,15] phút (OUTBOX_DB) lệch [1,5] phút với 3 lần thử (TECH) | Để mở: chốt một bảng ở #259 |
| E-08 · INC_INCENTIVE_CALCULATE_TECH §4.1 (bảng lỗi), NTF_CRITICAL_RETRY_TECH §4.2 | Hai nơi cùng được ghi là tăng `attempt_count` (`worker_outbox_result` và claim) | Đã sửa thiết kế: PREMISE S-17 |
| E-08 · NTF_CRITICAL_RETRY_TECH §3 (hạn 5 phút), §4.1 (dòng treo 2 phút) | Mốc treo 2 phút làm Critical mất callback ở lần cuối kết thúc muộn hơn 300 giây (ví dụ claim ở 220 giây, treo sau 340 giây) | Giả định: PREMISE G-43 |
| E-08 · NTF_CRITICAL_RETRY_TECH §4.4 | Hiệu lực của log kết quả stale khi tổng hợp và retry chưa quy định | Giả định: PREMISE G-44 |
| E-08 · S-037 Data Mapping, CORE_DB (RLS `business_days`) | Danh sách cảnh báo cần `business_date` nhưng ROLE-007 không có SELECT `business_days` | Giả định: PREMISE G-45 |
| E-09 · README reports-audit, api-design/_index | API Design `{API_ID}_API.md` ghi "viết ở LAB-5", chưa có file | Đã sửa thiết kế: PREMISE S-01 |
| E-09 · REQ-001 §8 Q4 (open), RPA_DB, FR-RPA-003 AC5 | SFTP: host, định dạng CSV RPT-06, mẫu tên tệp, định dạng batch code, lịch, sandbox, tệp cũ sau 締め再開 | Tạo issue làm rõ #330 |
| E-09 · REQ-001 §8 Q24 (open), ADR-008 R6 | Người nhận mốc băm audit ngoài ROLE-007 | Tạo issue làm rõ #333 |
| E-09 · RPA_DAILY_REPORTS_SPEC A4, RPA_MONTHLY_REPORTS_SPEC A4, REQ-001 Q90 (open), Q14 | Spec chỉ nêu nguồn chức năng của 11 báo cáo, không có cột CSV (chỉ RPT-06 có cột tối thiểu); nguồn "log trạng thái giao dịch" của RPT-02 không có bảng; SLA của RPT-09 (F-031 chưa phân tích) … | Tạo issue làm rõ #331 |
| E-09 · api-list QA-5, QA-10, REQ-001 Q31 (open), RPA_EXPORT_CENTER_SPEC OQ-2 | Thời hạn signed URL, quy tắc tên tệp, tải 12 báo cáo ra hai zip hay một | Tạo issue làm rõ #332 |
| E-09 · RPA_AUDIT_LOG_SEARCH_SPEC OQ-2, OQ-3 | Bảng 5 nhóm thao tác sang action; cách ghép mã giao dịch với bản ghi audit liên quan; độ dài tối đa mã giao dịch | Tạo issue làm rõ #334 |
| E-09 · RPA_DB §3, RPA_MONTHLY_REPORTS_SPEC A2, FR-RPA-002 AC1 | Lúc khóa ngày D chưa biết còn ngày nghiệp vụ nào sau D trong tháng (ngày nghỉ, ngày chưa mở), nên không xác định được "ngày nghiệp vụ cuối tháng" để sinh RPT-10..12 | Tạo issue làm rõ #335 |
| E-09 · AUDIT_DB, RPA_AUDIT_HASH_CHAIN_TECH (một TECH cho `write_audit` và `audit_verify_chain`), api-list §3 | Một function có hai thành phần; FR-RPA-004 và 007 cùng nằm ở feature báo cáo | Giả định: PREMISE G-46 |
| E-09 · api-list §3 `RPA_JOB_SFTP_PUSH`, `NTF_CRITICAL_RETRY_TECH` §4.3 | SFTP đẩy thuộc FR-RPA-003 (E-09) nhưng handler và lịch thử nằm ở worker E-08 | Giả định: PREMISE G-47 |
| E-09 · RPA_DB (10 bảng), api-list §3 (`RPA_MIGRATION_*`), README ("không có màn") | FR-RPA-008, ba bảng public `migration_*` và năm bảng staging nằm trong feature reports-audit | Giả định: PREMISE G-48 |
| E-09 · RPA_RATE_VERSION_HISTORY_SPEC A3, OQ-5, FR-RPA-006 AC3, api-list | AC3 yêu cầu cảnh báo vận hành khi không xác định phiên bản, nhưng chế độ `tradeCode` dùng hàm `stable` (không ghi được) và SPEC nói GET ghi `ops_alerts` mỗi lần tra (cần khóa chống trùng) | Giả định: PREMISE G-49 |
| E-09 · RPA_DAILY_REPORTS_SPEC E3, §4.2, api-list RPA_REPORT_LIST | `lockId` hoặc `dayId` sai hoặc không có trong 60 ngày: SPEC lúc ghi VALIDATION lúc ghi VALIDATION hoặc NOT_FOUND; api-list chỉ có VALIDATION | Để mở: chốt cặp mã ở #290 |
| E-09 · RPA_EXPORT_CENTER_SPEC (nút zip khóa khi còn `running`), api-list RPA_REPORT_DOWNLOAD_ALL | Spec chỉ nói FE khóa nút, API chưa nói rõ khi gọi lúc còn báo cáo `running` | Giả định: PREMISE G-50 |
| E-09 · RPA_AUDIT_LOG_SEARCH_SPEC OQ-6, OUTBOX_DB RLS | ROLE-005 không đọc `outbox_events` nên chỉ thấy đã tạo mốc, không biết email mốc đã gửi thành công | Để mở: không thêm API ngoài spec; ghi ở #312 |
| E-09 · REQ-001 §8 (Q14, Q16, Q22, Q26, Q43, Q51, Q64, Q65 resolved), RPA_DAILY_REPORTS_SPEC OQ, RPA_MONTHLY_REPORTS_SPEC F-2, RPA_AUDIT_LOG_SEARCH_SPEC, RPA_AUDIT_HASH_CHAIN_TECH, RPA_DB §8 | Còn ghi `open` hoặc "chờ Q43/Q51" cho các câu đã chốt (ví dụ F-4 ghi sinh lại chờ Q43 trong khi Q43 đã chốt không lưu lịch sử lượt lỗi) | Để mở: lệch ghi chép, backlog theo REQ-001 §8 |
| E-09 · FR-RPA-004 AC5, DR-RET-01 | Lưu audit online ít nhất 7 năm; E-09 không có issue riêng cho chính sách lưu | Để mở: thuộc nền tảng E-10 (retention, sao lưu); ghi ở `task-breakdown.md` mục 2 |
| E-09 · RPA_DAILY_REPORTS_SPEC A2, INC_INCENTIVE_CALCULATE_TECH §4.2, ADJ_DB, E05 đối soát | Báo cáo gắn `lock_id` nhưng nguồn có sẵn (view `trade_effective_values`, RPC đối soát) chỉ có giá trị hiện tại; nguồn theo mốc `locked_at` mới có ở bên thưởng | Giả định: PREMISE G-51 |
| E-09 · NTF_CRITICAL_RETRY_TECH §4.3, §4.4, DAILY A3 | Handler vừa "lỗi một báo cáo không chặn báo cáo khác" vừa "lỗi thì thử lại cả cặp"; chưa nói ranh giới giao dịch và kết quả trả về | Giả định: PREMISE G-52 |
| E-09 · NTF_CRITICAL_RETRY_TECH §4.4, RPA_DB §4.2 | Kết quả SFTP của lần thử cũ (đã bị claim lại) chưa bị chặn ở bảng `sftp_exports` | Giả định: PREMISE G-53 |
| E-09 · RPA_AUDIT_HASH_CHAIN_TECH §4.3, AUDIT_DB §4.2 | Dòng "đang chạy" và lượt chết giữa chừng không thể có nếu chèn run và kiểm nằm một giao dịch | Giả định: PREMISE G-54 |
| E-09 · RPA_MONTHLY_REPORTS_SPEC A2 và Element E-8 | A2 ghi báo cáo tháng cũ vẫn hiện khi ngày cuối tháng bị 締め再開, Element E-8 ghi ẩn ba dòng khi chưa khóa | Để mở: chốt ở #290; backlog hiện giữ bộ cũ kèm banner |
| E-09 · RPA_DB §4.1 (`report_runs`, khóa idempotent theo `lock_id`, `period_month`, `rule_version_id`) | Không có cột nào phân biệt thử lại cùng sự kiện với sự kiện mới (khóa lại, tháng chốt lại) cho cùng khóa idempotent | Đã sửa thiết kế: PREMISE S-18 |
| E-09 · NTF_CRITICAL_RETRY_TECH §4.2, §4.4 | Thu hồi dòng `processing` treo ở lần cuối chuyển thẳng sang `failed` mà không qua `worker_outbox_result`, nên các hiệu ứng kết thúc (alert, `sftp_exports`, `report_runs`) có thể thiếu | Giả định: PREMISE G-55 |
| E-10 · api-design/_index §1, api-list §2.1 | API Design `{API_ID}_API.md` cho `SYS_ME`, `SYS_EVIDENCE_UPLOAD_URL` ghi "viết ở LAB-5", chưa có file | Đã sửa thiết kế: PREMISE S-01 |
| E-10 · database-design/_index §5, ADR-001 §5, ARCH-01 §2 | Nhiều mục ghi "giữ nguyên prototype LAB-3" (`profiles` 7 cột, `today_tokyo`, `has_role`, `rpcToResponse`, `route-access-map`, `json-request`) nhưng `reference/lab-3-source/` không có trong repo này | Giả định: PREMISE G-56 |
| E-10 · REQ-001 §8 Q8 (open), ARCH-01 §4 | Vùng lưu dữ liệu, gói Supabase và Vercel, số môi trường, chu kỳ xoay vòng bí mật chưa có | Tạo issue làm rõ #370 |
| E-10 · REQ-001 §8 Q31 (open), api-list QA-5 | Bucket chứng cứ, thời hạn, chuyển lạnh sau 3 năm; 5 tệp, 10 MB, jpg, png, pdf mới là giả định LAB-1 | Tạo issue làm rõ #371 |
| E-10 · REQ-001 §8 Q5 (open), NFR-OPS-01 | Ngưỡng và người nhận cho 4 loại cảnh báo, người chịu trách nhiệm từng NFR, kênh cảnh báo sức khỏe hệ thống | Tạo issue làm rõ #372 |
| E-10 · CORE_DB §4.4 (Danh mục `params`), ADR-003 | Không có giá trị bản `market_rule` và `incentive_rate` đầu tiên (tỷ lệ thật chưa có); chưa nói bản đầu qua duyệt hai người hay nạp khi khởi tạo | Tạo issue làm rõ #373 |
| E-10 · error-codes (Q4), PAU_LOGIN_SPEC A-2 | Yêu cầu đổi ngôn ngữ JA và VI nhưng chuỗi tiếng Nhật của message chưa có | Tạo issue làm rõ #374 |
| E-10 · api-list §2.1 `SYS_ME` ("current_business_day() chỉ đọc trạng thái"), CORE_DB | `current_business_day()` là get-or-create (ghi), không thể gọi trong GET chỉ đọc | Giả định: PREMISE G-57 |
| E-10 · ARCH-05 §4, database-design/_index §5.2 (`get_my_role`), CORE_DB | Một mục (`get_my_role` có điều kiện `aal2`) nằm ở cả nền tảng và xác thực | Giả định: PREMISE G-58 |
| E-10 · OUTBOX_DB §4.1.1, NTF_CRITICAL_RETRY_TECH §3 | Đã kiểm: `max_attempts` nội bộ là 3 ở cả hai nguồn (SFTP 4); mâu thuẫn tôi ghi ở vòng nháp là sai | Để mở: đã ghi vào DoD #351, không đổi thiết kế; OUTBOX_DB là nguồn danh mục, ghi ở #351 |
| E-10 · CORE_DB (Q57), `current_business_day()` | Không đọc `market_holidays`, nên bản ghi tạo vào 休市日 vẫn rơi vào ngày đó | Để mở: đã ghi vào DoD #346, không đổi thiết kế; Q57 đã chốt, giữ hành vi, DB không chặn; ghi ở #346 |
| E-10 · FR-RPA-004 AC5, DR-RET-01 | Lưu audit online 7 năm; không có issue nào ở các epic khác giữ chính sách này | Để mở: đã ghi vào DoD #340, không đổi thiết kế; Giao #340 (sao lưu, lưu trữ, khôi phục) |
| E-10 · ADR-007 R2, NTF_CRITICAL_RETRY_TECH §4.2 | Lịch `pg_cron` theo giây cần phiên bản từ 1.5, "kiểm ở spike" | Để mở: đã ghi vào DoD #354, không đổi thiết kế; spike ở #354 (kết quả báo cho E-08) |
| E-10 · ADR-002 R1, PostgreSQL (quyền execute mặc định của PUBLIC) | Thu `execute` khỏi `anon` và `authenticated` chưa đóng quyền kế thừa từ `PUBLIC`; helper `outbox_emit`, `ops_alert_record` không có điều kiện cấm gọi trực tiếp | Giả định: PREMISE G-59 |
| E-10 · api-design/_index §2.2, error-codes §1.4 | Lỗi trigger có `hint` hợp lệ nhưng `details` hỏng: một nguồn ghi 500, một nguồn ghi vẫn trả `code` với `params` rỗng | Đã sửa thiết kế: PREMISE S-19 |
| E-10 · AUDIT_DB §4.1, RPA_AUDIT_HASH_CHAIN_TECH §5 | Cột băm NOT NULL không thêm nguyên trạng vào audit cũ; backfill bị trigger bất biến chặn | Giả định: PREMISE G-60 |
| E-10 · Supabase Storage (signed upload URL), api-list §2.1 | URL tải lên là quyền mang theo token, không gắn phiên người tạo; thời hạn do dịch vụ quy định | Để mở: ghi giới hạn và tách thời hạn tải lên khỏi tải xuống ở #337, #371 |
| E-11 · README reports-audit, api-design/_index | API Design `{API_ID}_API.md` ghi "viết ở LAB-5", chưa có file | Đã sửa thiết kế: PREMISE S-01 |
| E-11 · REQ-001 §8 Q9 (open), FR-RPA-008 AC6 | Nguồn thuộc baseline, khoảng lịch sử | Tạo issue làm rõ #399 |
| E-11 · REQ-001 §8 Q29 (open), RPA_MIGRATION_LOAD_TECH §4.1, §4.2 | Header và mã hóa tệp; tiêu chí gộp lot trùng "[ĐIỀN]"; cách ánh xạ trạng thái participant và giao dịch | Tạo issue làm rõ #400 |
| E-11 · REQ-001 §8 Q41 (open), ADR-014 §5 | Wave của `deliveries.csv`; cấu trúc `delivery_part`; quy tắc `delivery_code` | Tạo issue làm rõ #401 |
| E-11 · REQ-001 §8 Q67 (open) | Ngày cutover, giờ đóng băng, người ký go hoặc no-go | Tạo issue làm rõ #402 |
| E-11 · REQ-001 §8 Q91 (open), RPA_DB §8 | `entity_type` không có `lot_judgment` hay `rule_version`; phiên bản đầu do loader nạp hay ROLE-006 nhập | Tạo issue làm rõ #403, #373 |
| E-11 · api-list QA-4, PREMISE P14 | Ba API di trú không gắn màn nhưng ROLE-005 phải đọc, ký số tiền, xử lý loại trừ | Tạo issue làm rõ #404 |
| E-11 · RPA_MIGRATION_LOAD_TECH §3, §4.3 | TECH chỉ mô tả nạp theo ngày nghiệp vụ (`load_day`); Wave 1 (participant, căn cứ) không có ngày nghiệp vụ nhưng cũng phải nạp | Giả định: PREMISE G-61 |
| E-11 · RPA_MIGRATION_LOAD_TECH §4.5 (bước 2), danh sách `p_step` | Rollback lượt chưa nạp (`rolled_back`, xóa `stg_*`) mô tả nhưng không có bước RPC; `failed` không rõ ai đặt | Giả định: PREMISE G-62 |
| E-11 · RPA_DB §4.3 (`wave` 1..3), REQ-001 Q38 | Wave 3 (quyết toán, báo cáo) không còn nguồn nạp sau Q38 nhưng CHECK vẫn cho 3 | Để mở: đã ghi vào DoD #380, không đổi thiết kế; giữ CHECK theo spec, ghi ở #380 |
| E-11 · RPA_MIGRATION_LOAD_TECH (Q-N11), REQ-001 Q38, Q42, Q66, Q78 | Còn ghi `open` hoặc "giả định" cho các câu đã `resolved` ở REQ-001 §8 | Để mở: lệch ghi chép, backlog theo REQ-001 §8 |
| E-11 · api-list RPA_MIGRATION_BATCH_LIST, RPA_DB §4.4 | `raw_record` của dòng loại trừ chứa dữ liệu nguồn (có thể là dữ liệu cá nhân của participant) nhưng API trả `migration_rejected_records` | Giả định: PREMISE G-63 |
| E-11 · RFP 付録 C, quy tắc repo public | Fixture mẫu `actors.csv`... thuộc đề gốc, không được đưa lên repo | Để mở: đã ghi vào DoD #396, #400, không đổi thiết kế; fixture tự dựng ở #396, header theo khuôn chốt ở #400 |
| E-11 · RPA_MIGRATION_LOAD_TECH §4.1 (mỗi lượt một tệp), §4.3; RPA_DB §4.3; REQ-001 Q78 | Một ngày cần lot, giao dịch, giao hàng trước khi khóa nhưng mỗi lượt chỉ một tệp và Q78 cấm nạp bổ sung vào ngày đã khóa | Đã sửa thiết kế: PREMISE S-20 |
| E-11 · RPA_MIGRATION_LOAD_TECH §4.2 (bước 2) | Tham chiếu chéo chỉ tra link của Wave trước, trong khi lot và giao dịch cùng Wave 2 | Đã sửa thiết kế: PREMISE S-21 |
| E-11 · RPA_DB §4.3 (`rows_loaded` = số link), TECH §4.4 | Đơn vị đếm lệch: một dòng actors tạo hai link nên `rows_loaded` vượt `rows_total` | Đã sửa thiết kế: PREMISE S-22 |
| E-11 · TECH §4.1 (bước 3), §4.5 #3 | Production yêu cầu rehearsal đã ký cùng SHA-256, nhưng rehearsal ở staging (tệp đã che) còn production ở môi trường khác với tệp cuối có thể khác byte | Để mở: chốt bằng chứng rehearsal liên môi trường ở #379 (mặc định theo TECH khi cùng cơ sở dữ liệu) |
| E-11 · TECH §4.5, PAU_DB §4.4, ADR-014 §2 | Wave 1 đã commit mà chưa finalize không có audit; chưa có bước điều hòa sequence mã sau khi giữ mã nguồn | Giả định: PREMISE G-64 |
