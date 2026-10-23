# Khung prompt review độc lập

Điền các `{…}` rồi ghi thành tệp. Prompt gửi cho reviewer **không chứa kết luận của bạn** và **không dán nội dung dài**, chỉ đường dẫn.

```text
Bạn là người review độc lập cho {SẢN PHẨM}. Chỉ ĐỌC, không sửa bất kỳ tệp nào ngoài tệp kết quả ở cuối. Trả lời bằng {NGÔN NGỮ}, giữ nguyên mã định danh ({CÁC MÃ}).

## Bối cảnh
{2–5 câu: sản phẩm là gì, ai viết, dùng để làm gì, ràng buộc chính. Nêu rủi ro lớn nhất bạn lo (ví dụ lô này chấm lệch lô kia).}

## Đọc theo thứ tự này
1. {nguồn sự thật chính, đường dẫn}
2. {luật hoặc rubric áp dụng}
3. {sản phẩm cần review, đường dẫn}
4. {dữ liệu hỗ trợ: kết quả script kiểm, thống kê}
Khi cần kiểm chứng một chỗ, mở đoạn tương ứng của nguồn theo mã tham chiếu; không quét cả cây.

## Việc cần làm
{Dán danh sách kiểm từ templates/checklists/<loại>.md, đánh số A, B, C…}

## Phần vừa sửa (chỉ vòng 2 trở đi)
{Danh sách tệp, mục, dòng vừa sửa. Soi riêng phần này TRƯỚC, đặc biệt lỗi do chính lượt sửa gây ra: đổi bên này quên bên kia, số liệu tổng không khớp, phụ thuộc ngược chiều. Rồi mới quét phần còn lại.}

## Định dạng kết quả
Ghi vào {TỆP KẾT QUẢ}, các mục:
1. Tóm tắt (≤ 10 dòng): kết luận có đủ tin cậy chưa, ba vấn đề nặng nhất.
2. Bảng vấn đề: ID · Mức (Chặn / Quan trọng / Nhỏ) · Vị trí · Hiện tại → đề nghị · Bằng chứng (trích tệp và dòng hoặc mã tham chiếu) · Cách xử lý.
3. Số liệu đã tính và cách chạy lại.
4. Việc chưa kiểm được và vì sao.
Mỗi vấn đề phải có bằng chứng trích nguồn; vấn đề chỉ là cảm nhận thì ghi riêng, đánh dấu "cảm nhận".

## Cấm
{Ví dụ: không đề nghị sửa công thức; không đề xuất ghi lên hệ thống bên ngoài; không đọc hay nhắc secret; không chép nguyên văn tài liệu gốc.}
```

## Lưu ý khi điền

- Không viết "tôi nghĩ phần X đã đúng"; để reviewer tự kết luận.
- Nêu **rủi ro cụ thể** ở mục Bối cảnh; reviewer có định hướng sẽ tìm sâu hơn là danh sách kiểm chung.
- Giới hạn số phát hiện (ví dụ "tối đa 25 vấn đề, ưu tiên theo mức") để khỏi nhận bảng dài vô ích.
