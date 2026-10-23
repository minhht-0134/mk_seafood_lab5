# Quy trình triage một tệp kết quả review

Đầu vào: tệp kết quả của reviewer (ví dụ `notes/<đối-tượng>-codex-review-result.md`). Đầu ra: tệp phản hồi `notes/<đối-tượng>-codex-review-response[-roundN].md`, các sửa đã áp dụng, một dòng nhật ký.

## 1. Lập bảng phát hiện

Đọc toàn bộ tệp kết quả, rồi lập bảng làm việc, mỗi phát hiện một dòng:

| ID | Mức (reviewer nêu) | Khẳng định | Nguồn được trích | Loại kiểm | Kết quả kiểm | Nhãn |
|---|---|---|---|---|---|---|

- **Khẳng định**: nêu lại thành một câu có thể đúng hoặc sai ("DoD của X ghi A, spec Y ghi B").
- **Loại kiểm**: `grep` (tìm được trong tệp), `đọc` (cần đọc đoạn spec), `tính` (có số), `quyết định` (thuộc người dùng hoặc khách).
- Phát hiện không trích nguồn: tự tìm nguồn; không tìm được thì nhãn **Chưa đủ dữ liệu**.

## 2. Kiểm chứng

Làm theo thứ tự rẻ đến đắt, và ghi lệnh hoặc đoạn đã mở vào cột "Kết quả kiểm":
1. `grep` hoặc script có sẵn của dự án.
2. Mở đúng dòng hoặc mục được trích (không đọc cả tệp lớn).
3. Phát hiện có số: tính lại bằng mã, so với số của reviewer. Lệch thì nêu số của bạn.

Quy tắc chống nhượng bộ:
- Không nhận phát hiện chỉ vì reviewer nêu với giọng chắc chắn.
- Reviewer đề nghị một cách sửa không có nghĩa cách sửa đó đúng; kiểm xem cách sửa có tạo lỗi mới không (xem mục 4).
- Phát hiện reviewer dựa trên giả định về nguồn (ví dụ "TECH mới hơn DB") thì kiểm giả định đó bằng dữ liệu (ngày, dòng), không suy diễn.

## 3. Nhãn

| Nhãn | Nghĩa | Bắt buộc ghi |
|---|---|---|
| Đồng ý | Khẳng định đúng và cách xử lý hợp lý | Bằng chứng đã mở; cách sửa |
| Một phần | Đúng một phần hoặc đúng nhưng cách sửa khác | Phần đúng, phần không, vì sao |
| Bác | Khẳng định sai | Bằng chứng ngược (trích dòng, kết quả lệnh) |
| Chưa đủ dữ liệu | Không kiểm được trong phạm vi hiện tại | Còn thiếu gì, ai hoặc cái gì giải quyết |

Phát hiện loại `quyết định`: nhãn **Chưa đủ dữ liệu** kèm câu hỏi cho người dùng; không tự sửa.

## 4. Sửa và rủi ro hồi quy

Trước khi sửa mỗi phát hiện đã nhận, trả lời bằng một dòng: *sửa này còn chạm chỗ nào khác?* (nơi gọi, nơi tham chiếu, số liệu tổng, tài liệu liên quan). Ghi các chỗ đó vào tệp phản hồi. Đây là bước chặn loại lỗi "sửa gây lỗi mới".

Sau khi sửa xong: chạy script kiểm của dự án.

## 5. Tệp phản hồi

```text
# Phản hồi review <đối tượng> (vòng N)
Tóm tắt: X phát hiện; Đồng ý a, Một phần b, Bác c, Chưa đủ dữ liệu d. Tỷ lệ đồng ý: a/X.
Bảng phát hiện (mục 1, đủ cột).
Các sửa đã áp dụng: danh sách tệp và mục.
Chỗ chạm theo mục 4.
Câu hỏi cho người dùng: (các phát hiện loại quyết định).
Lệnh đã chạy: (grep, script kiểm).
```

Cuối cùng ghi nhật ký (`scripts/log-round.py`) với số lượng khớp bảng, trong đó `--caused-by-fix` là số phát hiện mà nguyên nhân là lượt sửa trước (đối chiếu với tệp phản hồi vòng trước).
