# Báo cáo tiến độ: Sprint 1

**Iteration:** Sprint 1, từ 02/11/2026 đến 13/11/2026 (hai tuần, 10 ngày làm việc).
**Lưu ý:** đây là sprint **giả lập** để minh họa theo dõi tiến độ; ngày tháng và kết quả do kịch bản đặt ra, không phải số liệu dự án thật. Số issue, điểm và giờ lấy trực tiếp từ GitHub Project của dự án.

**Cách đọc số liệu.** *SWP* là điểm khối lượng công việc chuẩn (một điểm khoảng nửa ngày công, 3,5 giờ). Dự án có 350 đầu việc, tổng 1.647 điểm, khoảng 5.764,5 giờ. Nhóm làm việc giả định gồm bốn người (hai backend, một giao diện, một kiểm thử); sức chứa mỗi sprint khoảng 224 giờ, tức khoảng 64 điểm.

## 2. Trạng thái

**Sprint 1: cam kết 20 đầu việc, 51 điểm (178,5 giờ). Đã xong 15 đầu việc, 29 điểm (57%).**

| Trạng thái | Số issue | Tổng SWP | Tổng giờ (kế hoạch) | Ghi chú |
|---|---|---|---|---|
| Done | 15 | 29 | 101,5 | Gồm 11 câu hỏi làm rõ nghiệp vụ, tài liệu thiết kế API của giao dịch, khung dự án và quy trình phát hành (#338), cấu trúc dữ liệu nền đầu tiên (#343) và một thành phần giao diện dùng chung |
| In Progress | 1 | 5 | 17,5 | Cấu trúc dữ liệu nền thứ hai: hàm dùng chung cho các thao tác (#344); còn khoảng 2 ngày công |
| Blocked | 1 | 3 | 10,5 | Một câu hỏi làm rõ đang chờ khách hàng trả lời |
| Todo | 3 | 14 | 49,0 | Chưa bắt đầu vì phải chờ cấu trúc dữ liệu nền xong: bảng ngày nghiệp vụ (#345), bảng nhật ký kiểm toán (#348), mở rộng bảng tài khoản (#7) |
| **Cộng Sprint 1** | **20** | **51** | **178,5** |  |

**Toàn dự án (350 đầu việc).** Xong 15 (29 điểm, 1,8% tổng điểm), đang làm 1, bị chặn 1, còn lại chưa bắt đầu. Sprint 2 đã xếp 13 đầu việc mới (30 điểm), ngoài năm đầu việc chuyển tiếp từ Sprint 1 (22 điểm). 317 đầu việc chưa xếp vào sprint nào.

**Các hạng mục nghiệp vụ đặc thù đang ở đâu.**

| Hạng mục | Số đầu việc | Xong | Đang làm / bị chặn | Chưa làm | Vị trí |
|---|---|---|---|---|---|
| 完納奨励金 (thưởng thanh toán đủ đúng hạn) | 27 | 0 | 0 | 27 | chưa xếp sprint nào |
| 業務規程 có phiên bản | 9 | 0 | 0 | 9 | chưa xếp sprint nào |
| 許可 và 承認 | 17 | 0 | 0 | 17 | chưa xếp sprint nào |
| 参加上限 (hạn mức mua trong ngày) | 15 | 0 | 0 | 15 | chưa xếp sprint nào |
| 締め (chốt sổ) và không chốt khi còn pending | 7 | 0 | 0 | 7 | chưa xếp sprint nào |
| 締め再開 hai người duyệt | 5 | 0 | 0 | 5 | đã xếp: 1 ở Sprint 1 |
| Sửa sau chốt | 12 | 0 | 0 | 12 | chưa xếp sprint nào |
| Audit bất biến | 11 | 0 | 0 | 11 | đã xếp: 1 ở Sprint 1 |
| Offline | 18 | 0 | 0 | 18 | chưa xếp sprint nào |
| Outbox và worker | 29 | 0 | 0 | 29 | chưa xếp sprint nào |
| MFA | 37 | 0 | 1 | 36 | đã xếp: 1 ở Sprint 1 |
| Di trú dữ liệu | 13 | 0 | 0 | 13 | chưa xếp sprint nào |

Phần lớn hạng mục đặc thù chưa bắt đầu vì dựa trên nền tảng chung (bảng dữ liệu, kiểm soát truy cập, ghi nhật ký) mà Sprint 1 chỉ mới xong một phần. Đây là thứ tự làm có chủ đích, không phải chậm trễ riêng của từng hạng mục.

## 3. Burndown (điểm còn lại của Sprint 1)

Đường kế hoạch giảm đều từ 51 điểm xuống 0 sau 10 ngày. Số "còn lại" tính từ ngày hoàn thành từng đầu việc trong nhật ký giả lập, đối chiếu với trạng thái trên Project (tổng điểm xong khớp: 29).

| Ngày | Kế hoạch còn | Thực tế còn | Xong trong ngày |
|---|---|---|---|
| 02/11 | 45,9 | 50 | 1 |
| 03/11 | 40,8 | 42 | 8 |
| 04/11 | 35,7 | 41 | 1 |
| 05/11 | 30,6 | 39 | 2 |
| 06/11 | 25,5 | 33 | 6 |
| 09/11 | 20,4 | 33 | — |
| 10/11 | 15,3 | 29 | 4 |
| 11/11 | 10,2 | 23 | 6 |
| 12/11 | 5,1 | 22 | 1 |
| 13/11 | 0,0 | 22 | — |

```text
02/11 | █████████████████| còn 50 (kế hoạch 46)
03/11 | ██████████████   | còn 42 (kế hoạch 41)
04/11 | ██████████████   | còn 41 (kế hoạch 36)
05/11 | █████████████    | còn 39 (kế hoạch 31)
06/11 | ███████████      | còn 33 (kế hoạch 26)
09/11 | ███████████      | còn 33 (kế hoạch 20)
10/11 | ██████████       | còn 29 (kế hoạch 15)
11/11 | ████████         | còn 23 (kế hoạch 10)
12/11 | ███████          | còn 22 (kế hoạch 5)
13/11 | ███████          | còn 22 (kế hoạch 0)
```


**Lệch kế hoạch ở đâu.** Hai ngày đầu tiến độ sát kế hoạch vì chủ yếu là câu hỏi làm rõ và tài liệu, việc nhỏ và ít phụ thuộc. Từ 04/11 đường thực tế tụt dần: các việc nền tảng lớn phải làm nối tiếp nhau, và khung dự án với quy trình phát hành (5 điểm) làm quá giờ khoảng 30% nên chỉ xong ngày 06/11, trong khi các cấu trúc dữ liệu nền phải chờ nó. Khoảng cách rộng nhất ở cuối sprint: còn 22 điểm chưa xong gồm cấu trúc dữ liệu nền thứ hai còn dở, ba đầu việc chưa bắt đầu và một câu hỏi làm rõ bị chặn chờ khách hàng.

**Dự báo.** Tốc độ Sprint 1 là 29 điểm. Phần chưa xong không phải do thiếu người mà do việc phía sau chưa mở khóa (nhóm giao diện gần như không có việc: chỉ 10,5 giờ trong Sprint 1). Nếu từ Sprint 2 đạt sức chứa khoảng 64 điểm mỗi sprint, 1.618 điểm còn lại cần khoảng 25 sprint, tức khoảng 12 tháng. Con số này dài hơn lịch chín tháng phát triển ở bản ước lượng đầu; xem rủi ro 4.

## 4. Rủi ro trễ

| Rủi ro | Issue | Ảnh hưởng tới mốc nào | Hành động | Ai làm, khi nào |
|---|---|---|---|---|
| 1. Cấu trúc dữ liệu nền chưa xong, ba đầu việc phụ thuộc chưa bắt đầu | #344 (đang làm), #7, #345, #348 | Mốc bắt đầu làm nghiệp vụ đầu tiên (đăng nhập, quản lý người tham gia): lùi khoảng một sprint nếu không xử lý | Hoàn tất phần nền thứ hai trong tuần đầu Sprint 2; hai backend làm song song các phần độc lập nhau | BE-1 và BE-2, hạn 18/11/2026 |
| 2. Một câu hỏi làm rõ bị chặn chờ khách hàng | #331 | Các báo cáo và xuất tệp (epic Báo cáo, 32 đầu việc phía sau): không chặn ngay nhưng sẽ chặn khi tới lượt | Nhắc khách trả lời; hết hạn thì làm theo phương án đề xuất ghi trong đầu việc và ghi rõ là giả định | PL-1, nhắc ngay 16/11, hạn 20/11/2026 |
| 3. Nhóm giao diện thiếu việc (10,5 giờ trên 56 giờ trong Sprint 1, 0 giờ trong Sprint 2) | Các màn hình của mọi epic | Hiệu suất nhóm: khoảng 100 giờ giao diện chưa dùng trong hai sprint đầu; màn hình dồn về sau | Cho giao diện dựng khung dùng chung và màn hình theo thiết kế bằng dữ liệu mẫu, rồi nối vào hợp đồng API khi sẵn sàng (cần đổi quy tắc phụ thuộc) | PL-1 và FE-1, quyết định khi lập kế hoạch Sprint 2 ngày 13/11/2026 |
| 4. Tổng thời gian dài hơn lịch ban đầu (khoảng 26 sprint so với chín tháng) | Toàn dự án | Mốc go-live giả định 01/08/2027 của lịch ban đầu | Trình khách ba phương án: thêm một backend, giảm phạm vi (hoãn một số báo cáo), hoặc dời mốc go-live | PL-1, trình khách trước 27/11/2026 (hết Sprint 2) |
| 5. Nhiều câu hỏi làm rõ chưa có quyết định | 18 câu hỏi chưa xong (trong 29) | Các đầu việc phụ thuộc chỉ chấm điểm theo giả định, có thể phải chấm lại | Gửi khách danh sách câu hỏi theo thứ tự ưu tiên; mỗi câu ghi phương án đề xuất để khách chỉ cần xác nhận | QA-1 soạn, PL-1 gửi, hạn trả lời 27/11/2026 |
| 6. Ước lượng điểm chưa kiểm chéo toàn bộ | Nhóm đầu việc có tranh khóa đồng thời (chuỗi khóa, ca đua) | Độ chính xác của tổng điểm; dự báo số sprint có thể lệch | Kiểm chéo khoảng 35 đầu việc (10%) bằng người ước lượng khác, lệch từ một bậc trở lên thì chấm lại cả nhóm cùng cơ chế | PL-1 chỉ định, xong trước Sprint 3 (27/11/2026) |
