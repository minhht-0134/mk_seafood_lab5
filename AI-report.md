# Báo cáo dùng AI

Công cụ chính: Claude Code (một agent chính, kèm các agent phụ khi chấm SWP) và Codex (do người làm bài chạy riêng để review chéo). Người làm bài quyết định các điểm rẽ nhánh, chạy Codex, kiểm mẫu SWP và duyệt trước mọi thao tác ghi lên GitHub.

## 1. Đã dùng skill nào, viết prompt thế nào cho từng việc

| Việc | Skill / agent | Prompt và cách làm |
|---|---|---|
| Break task (11 epic) | Claude Code đọc spec; script kiểm do AI tự viết; Codex review | Làm lần lượt từng epic. Lệnh của người làm bài ngắn ("hãy triển khai E-11"), phần chỉ dẫn nằm sẵn trong `CLAUDE.md` và các quyết định đã chốt (độ hạt, loại issue, phụ thuộc). Mỗi epic: (1) AI đọc đúng các tài liệu của feature (FR, ADR, TECH, SPEC, DB, danh sách API, bảng câu hỏi) rồi gom chỗ hở trước khi viết; (2) ghi epic thành JSON (khóa, loại, mục tiêu, phạm vi, DoD, tham chiếu spec bằng mã, phụ thuộc); (3) chạy script kiểm: khóa duy nhất, cha-con đối xứng, phụ thuộc có thật, không vòng; (4) viết prompt review cho Codex; (5) người làm bài chạy Codex; (6) AI đối chiếu từng phát hiện với nguồn spec rồi sửa; (7) lặp lượt 2, 3 cho tới khi hết điểm nghiêm trọng. |
| Prompt cho Codex | Claude Code viết prompt, Codex chạy | Prompt độc lập, không dựa vào hội thoại: nêu bối cảnh, thứ tự các tệp cần đọc, các việc cần kiểm (DoD khớp AC, phụ thuộc, phủ spec, chỗ hở), định dạng kết quả (bảng mức Chặn/Quan trọng/Nhỏ kèm bằng chứng), ràng buộc chỉ đọc và không đề xuất sửa công thức. Kết quả ghi vào tệp để AI đọc lại. |
| Đưa lên GitHub | Claude Code + `gh` | Người làm bài đồng ý trước repo, Project và quyền `project`. Script đọc JSON, chạy thử 5 issue, kiểm trên Project rồi mới chạy 388 issue còn lại; nối sub-issue, điền trường Mã backlog, Loại, Epic, Nhóm đặc thù. Script chạy lại an toàn. |
| Chấm SWP | Skill `tkm:sun-estimate` | Lệnh: "hãy chạy B5". Skill đọc chính Project (chỉ đọc, qua cổng kiểm thao tác), chia 350 issue lá thành 5 lô, mỗi lô 70 issue giao cho một agent chấm theo một brief chung (công thức, từ vựng đóng, mỏ neo để các lô nhất quán). Người làm bài kiểm 5 issue mẫu skill chọn (hai vòng: mức độ khó, rồi điểm cụ thể). |
| Ghi SWP lên Project | Agent + `gh` | Người làm bài chốt tổng, tự ghi tay 11 epic; AI viết script ghi nốt `point` cho 393 mục còn lại (GraphQL, 20 mục mỗi lần, thử lại khi lỗi 5xx), rồi đọc ngược theo id từng mục để đối chiếu với báo cáo: 404 trên 404 khớp. Chỉ ghi sau khi người làm bài đồng ý. |
| Quy ra giờ | Claude Code | Lệnh: "hãy đề xuất quy ước cho tôi duyệt trước". AI tính hệ số từ LAB-1 (3,53 giờ/SWP phần dựng, 3,27 phần QA) và ước trực tiếp tám issue mốc (trung bình ~3,2), nêu hai hạn chế và hệ quả lịch rồi hỏi duyệt; người làm bài chọn 1 SWP = 3,5 giờ. Script ghi trường `Giờ ước lượng`. |
| Sprint giả lập | Claude Code | Lệnh: "hãy tiếp theo bước B7". AI xếp sprint bằng script theo đồ thị phụ thuộc thật và sức chứa; kịch bản kết quả Sprint 1 (một việc quá giờ, một câu hỏi chờ khách) do AI đặt, người làm bài duyệt trước khi ghi Iteration, người phụ trách, trạng thái. |
| Skill review (tự viết) | Claude Code | Sau khi thấy vòng review lặp lại ở 11 epic, SWP và tài liệu, người làm bài hỏi có nên làm skill không; AI tư vấn phạm vi (ba bước `prompt`, `triage`, `regress`; v1 nhỏ) và soạn `skills/review-loop/`: quy trình, khung prompt, ba danh sách kiểm (backlog, SWP, tài liệu), giao thức triage và script ghi nhật ký. Thử script bằng ca đúng và ca lệch số; chưa chạy thử cả vòng thật. |
| Báo cáo tiến độ và các tệp Markdown | Claude Code | Các tệp sinh bằng script đọc từ Project, báo cáo SWP và nhật ký giả lập để số liệu khớp nhau giữa README, `estimate.md`, `progress-report.md`; phần văn viết tay do AI soạn, người làm bài đọc duyệt. Prompt: "hãy bắt đầu viết các file Markdown (B8–B9)". |

## 2. Đã review output của AI ra sao

Người làm bài review ở các bước: chọn phương án ở mỗi điểm rẽ (độ hạt, epic, quy giờ, sprint), chạy và đọc kết quả Codex, kiểm 5 issue mẫu SWP, duyệt kịch bản sprint, duyệt hệ số quy giờ, và đồng ý trước mỗi lần ghi lên GitHub.

| Bước | Ai review gì | Vấn đề phát hiện trong output của AI | Xử lý |
|---|---|---|---|
| Backlog 11 epic | Codex đọc từng epic, lượt 1 cho tổng cộng 171 phát hiện, sau đó 1 đến 2 lượt nữa cho 9 epic | Lỗi thật của AI: DoD ghi hành vi trái TECH (bác 再審査 về 一時停止 thay vì 失効), giao việc ghi nhật ký cho job trong khi TECH cấm, thu quyền thực thi khỏi `anon` và `authenticated` mà quên `PUBLIC`, retry gom theo "có log success" thay vì theo (người nhận, kênh), số trạng thái giao diện lấy từ số tệp ảnh. Nhiều lỗi do chính lượt sửa trước gây ra (đổi bên nhận nhưng quên bên gọi, thêm lời gọi giữa hai issue làm phụ thuộc ngược chiều) | AI đối chiếu bằng chứng nguồn cho từng điểm rồi sửa; thêm lượt review sau mỗi lần sửa nghiêm trọng; script kiểm được bổ sung (đối xứng cha-con, vòng qua issue cha, khóa không tồn tại) và thử bằng ba lỗi cố ý |
| Backlog toàn bộ | Script rà cuối | 143 issue còn phụ thuộc bằng khóa tạm giữa các epic | Script thay khóa thật; đồ thị trước và sau cùng 1.447 cạnh, 0 vòng, 0 khóa lạ |
| Chỗ hở của spec | AI rà bằng script, Codex nhận xét từng dòng | AI từng nghi hai chỗ lệch mà kiểm lại hóa ra không phải lỗi (lệnh `ls` hiển thị lẫn, FR đã hủy) | Kiểm lại bằng `find` và `grep` trước khi ghi thành chỗ hở; ghi 210 chỗ hở vào `task-breakdown.md` |
| Chấm SWP, kiểm kỹ thuật | Script kiểm của skill | 38 issue gán discipline `Unknown` nhưng độ tin cậy cao, trái hợp đồng; agent chấm kiểu `sun-estimate-worker` không có công cụ đọc ghi tệp nên không chạy được | Gán discipline theo nội dung cho 9 issue tài liệu, giữ `Unknown` và độ tin cậy thấp cho 29 issue làm rõ; đổi sang agent có công cụ tệp |
| Chấm SWP, kiểm mẫu | Người làm bài kiểm 5 issue mẫu | #98 được nâng từ 1 lên 8 SWP; nếu lan sang nhóm tương tự sẽ nâng 26 issue từ 1 lên 8 và mâu thuẫn với #55 cùng nhóm đã chốt 1 | AI chỉ ra mâu thuẫn và số hệ quả (+178 SWP) trước khi khóa; người làm bài chọn chỉ riêng #98 |
| Chấm SWP, review độc lập | Codex đọc 5 lô, thống kê theo loại, lô, epic | 8 issue gắn chữ ký đồng thời nhưng chấm C2 trong khi 49 issue cùng chữ ký chấm C3; #383 có 5 bảng chấm như 1 bảng; #5 nhận độ khó của backend; #98 không có DoD giải thích mức 8 | AI đối chiếu từng issue với nội dung, sửa 16 issue (tổng 1.633 lên 1.647), ghi các giữ nguyên có lý do (#26, #72, #75, #264) |
| Ghi Project | AI đọc ngược theo id mục | Danh sách `gh project item-list` và truy vấn phân trang đôi khi trả thiếu mục (lần đầu thiếu #357, sau đó chỉ về 100 trên 404) nên đối chiếu theo danh sách sẽ báo sai | Đối chiếu bằng truy vấn theo id từng mục; thêm thử lại khi lỗi 502 |
| Quy giờ | Người làm bài duyệt trước khi ghi | AI nêu rõ rằng hệ số lấy từ LAB-1 nên so sánh với LAB-1 chỉ đúng ở phân bổ giữa epic, và tổng giờ kéo dài khoảng 26 sprint so với 9 tháng của lịch ban đầu | Ghi hai điều này vào `estimate.md` và `progress-report.md` thay vì trình bày như kiểm chứng độc lập |
| Báo cáo tiến độ | AI soát lại câu chữ với số liệu | Bản nháp viết "nửa đầu sprint bám sát hoặc nhanh hơn kế hoạch" trong khi bảng cho thấy tụt từ ngày 04/11; tên cấu trúc dữ liệu trong ghi chú không khớp tiêu đề issue | Sửa câu chữ theo số liệu và tiêu đề thật |

## 3. Điểm đặc biệt trong cách dùng AI

**Chỗ tin là hiệu quả**
- *Kiểm bằng mã trước khi nhờ người hay AI khác.* Script kiểm backlog và script đối chiếu Project bắt được lỗi cấu trúc mà đọc bằng mắt bỏ sót; điều kiểm được bằng `grep` thì kiểm trước khi hỏi Codex.
- *Hai AI khác nhau viết và review.* Codex bắt được nhiều lỗi mà agent viết không tự thấy, nhưng chỉ hiệu quả khi có spec nguồn để đối chiếu và chạy thêm lượt sau mỗi lần sửa nghiêm trọng.
- *Chia lô song song để chấm SWP* rẻ hơn nhiều so với chấm tuần tự, miễn là có brief chung với mỏ neo và có bước thống kê chéo sau đó.
- *Đóng gói vòng review thành skill* (`skills/review-loop/`): luật chống nhượng bộ, bước soi riêng phần vừa sửa và nhật ký tỷ lệ đồng ý biến thói quen thành quy trình lặp lại được; mới ở bản v1, chưa qua một vòng review thật.
- *Sinh các tệp nộp từ cùng một nguồn dữ liệu* (Project, báo cáo SWP, nhật ký sprint) làm số liệu khớp nhau giữa các tệp.

**Chỗ chưa tốt, cần cải thiện khi làm thật**
- AI đồng ý gần như mọi điểm Codex nêu. Điều đó vừa cho thấy Codex thường đúng, vừa cho thấy rủi ro AI dễ nhượng bộ; chưa có người thứ ba hay người nghiệp vụ kiểm lại các điểm đã đồng ý.
- Điểm SWP do năm agent chấm riêng không có kiểm chéo mù; lượt review độc lập chỉ là đọc lại, không phải chấm lại. Cần chấm mù lại khoảng 35 issue (10%) và so lệch từng trục trước khi dùng cho cam kết với khách. Điểm tập trung ở 3 đến 6 SWP (82%) nên cần thử thêm bằng man-day thật.
- Điểm chấm dựa vào thân issue, chưa đọc lại nguyên văn spec cho từng issue; sai lệch dễ ở các RPC có tranh khóa.
- Hệ số 3,5 giờ/SWP hiệu chuẩn từ chính LAB-1 nên phần so sánh với LAB-1 có tính vòng tròn; cần ít nhất một sprint thật để lấy năng suất thực.
- Sprint 1 là giả lập: kịch bản do AI đặt, người làm bài chỉ duyệt; số burndown minh họa cách theo dõi, không phải bằng chứng về năng suất.
- Công suất và token: mỗi epic cần 2 đến 3 vòng viết, review, sửa; làm cho 11 epic tốn nhiều thời gian và ngữ cảnh. Nhật ký làm việc dài phải ghi ra tệp để tiếp tục sau khi ngữ cảnh bị nén.
- 75 chỗ hở đang để mở và 29 câu hỏi làm rõ chờ khách; AI không tự quyết thay khách, nhưng đã đặt giả định để backlog đi tiếp.

**Chưa có ý tưởng**
- Cách đo độ đúng của phần "vì sao" trong PREMISE (nguồn mâu thuẫn spec) mà không cần đọc lại toàn bộ 400 tệp spec.
- Cách để agent chấm SWP tự phát hiện tranh khóa mà không cần người liệt kê dấu hiệu ở brief.
