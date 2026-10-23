---
name: review-loop
description: "Vòng review chéo có kỷ luật giữa AI viết và một reviewer độc lập (ví dụ Codex): sinh prompt review, kiểm chứng từng phát hiện với nguồn trước khi nhận, rồi soi lại đúng phần vừa sửa. Dùng khi người dùng nói 'viết prompt review cho Codex', 'kiểm tra kết quả review', 'review vòng 2', hoặc đưa tệp kết quả review để đối chiếu."
argument-hint: "<prompt|triage|regress> <đối tượng review> [--round N]"
metadata:
  version: "1.0.0"
triggers: ["review codex", "kết quả review", "review vòng 2", "prompt review", "đối chiếu phát hiện"]
---

# Review loop

Mục đích: biến vòng lặp "viết prompt → reviewer chạy → đối chiếu → sửa → soi lại" thành một quy trình có luật, để không tốn công viết lại từ đầu và không nhượng bộ reviewer một cách vô thức.

Vai trò: **AI viết** (bạn, agent) không tự review sản phẩm của mình. **Reviewer** là công cụ hoặc người khác (Codex do người dùng chạy). Người dùng quyết điều thuộc về họ (phạm vi, khách hàng, đánh đổi); skill không quyết thay.

## Ba bước

| Bước | Khi nào | Việc | Đọc |
|---|---|---|---|
| `prompt` | Cần reviewer đọc một sản phẩm | Sinh prompt độc lập, ghi vào tệp | `templates/prompt-base.md`, một tệp trong `templates/checklists/` |
| `triage` | Người dùng đưa tệp kết quả review | Kiểm chứng từng phát hiện, phân loại, sửa, ghi tệp phản hồi | `references/triage-protocol.md` |
| `regress` | Đã sửa xong | Chạy script kiểm, sinh prompt vòng sau chỉ nhắm phần vừa sửa, quyết định dừng hay tiếp | mục "Điều kiện dừng" bên dưới |

Sau mỗi bước ghi một dòng nhật ký bằng `scripts/log-round.py`. Nhật ký là nguyên liệu cho báo cáo dùng AI, không phải việc phụ.

## Bước 1: prompt

1. Xác định **loại sản phẩm** (backlog, chấm điểm, tài liệu) và chọn danh sách kiểm tương ứng ở `templates/checklists/`. Chưa có loại phù hợp thì dùng `docs.md` và ghi chú phần thiếu.
2. Điền các chỗ trống của `prompt-base.md`: sản phẩm cần review, nguồn sự thật để đối chiếu (đường dẫn cụ thể), thứ tự đọc, các điểm cần kiểm, tệp kết quả, những điều cấm.
3. Prompt phải **độc lập**: reviewer không thấy hội thoại. Chỉ gửi đường dẫn tệp, không dán nội dung dài. Không đưa kết luận của bạn vào prompt (reviewer dễ xác nhận kết luận có sẵn).
4. Vòng 2 trở đi: ghi rõ phần vừa sửa (danh sách tệp, dòng, mục) và yêu cầu **soi riêng phần đó trước**, rồi mới quét phần còn lại. Không nêu phát hiện vòng trước là "đã đúng".
5. Ghi prompt ra tệp (`notes/<đối-tượng>-review-prompt[-roundN].md`) và nói cho người dùng biết tệp kết quả cần đặt ở đâu.

Không tự chạy reviewer. Người dùng chạy và trả tệp kết quả.

## Bước 2: triage

Đọc `references/triage-protocol.md` rồi làm theo. Tóm tắt luật cứng:
- Mọi phát hiện phải được **mở nguồn được trích** trước khi phân loại. Không có ngoại lệ cho lý do "nghe hợp lý".
- Phát hiện có số liệu thì tính lại bằng mã, không bằng suy nghĩ.
- Phân loại chỉ có bốn nhãn: **Đồng ý**, **Một phần**, **Bác**, **Chưa đủ dữ liệu**. Hai nhãn sau bắt buộc có lý do và bằng chứng.
- Điều kiểm được bằng `grep` hoặc script thì làm trước, ghi lệnh đã chạy.
- Điều cần quyết định của người dùng hoặc khách thì **không tự sửa**: nêu trong tệp phản hồi, hỏi người dùng.

## Bước 3: regress

1. Chạy script kiểm cố định của dự án (xác nhận tên script với người dùng ở lần đầu, ghi vào nhật ký).
2. Lập danh sách phần đã sửa (từ `git diff` hoặc từ tệp phản hồi). Lỗi do chính lượt sửa trước gây ra là loại lỗi hay gặp nhất: đổi bên nhận quên bên gọi, thêm lời gọi làm phụ thuộc ngược chiều, sửa số ở một nơi mà nơi khác còn số cũ.
3. Sinh prompt vòng sau (bước 1, mục 4).
4. Quyết định dừng theo mục dưới.

### Điều kiện dừng

Dừng khi **cả hai** đúng: vòng vừa rồi không có phát hiện mức nghiêm trọng, và script kiểm cố định chạy sạch. Tối đa 3 vòng cho một sản phẩm; vòng 3 vẫn còn nghiêm trọng thì dừng và báo người dùng, không tự chạy tiếp. Nếu reviewer chỉ nêu điểm nhỏ ở vòng 2, ghi lại rồi dừng, không kéo dài.

## Nhật ký

```text
python3 skills/review-loop/scripts/log-round.py --file notes/ai-work-log.md --subject "E-05" --round 2 \
  --found 12 --agree 10 --partial 1 --reject 0 --pending 1 --caused-by-fix 3 --note "ví dụ ngắn"
```
Ghi đủ: số phát hiện, đồng ý, một phần, bác, chưa đủ dữ liệu, và **bao nhiêu phát hiện do lượt sửa trước gây ra**. Số này cho biết vòng sau có đáng chạy không.

## Cảnh báo về nhượng bộ

Nếu một vòng mà bạn đồng ý với hơn 90% phát hiện, dừng lại và tự hỏi: có phát hiện nào bạn nhận mà chưa mở nguồn không? Có điểm nào reviewer chỉ nêu cảm nhận không kèm bằng chứng không? Báo người dùng tỷ lệ đồng ý trong tệp phản hồi để họ cũng thấy.
