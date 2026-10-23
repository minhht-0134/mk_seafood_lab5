#!/usr/bin/env python3
"""Sinh task-breakdown.md. Chạy tại gốc repo sau build-premise.py: python3 scripts/docs/build-task-breakdown.py"""
import re, sys, collections
sys.path.insert(0, 'scripts/docs')
from docs_data import BACKLOG, ISSUES, NUM, EPIC_NUM, special_value, nums, num_text, keys_in, table, cut, REPORT
from premise_rows import GAPS, classify, build, body
import importlib.util
_s = importlib.util.spec_from_file_location('b2g', 'scripts/github/backlog-to-github.py'); _m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)

leaves = {k: v for k, v in ISSUES.items() if v['leaf']}
parents = {k: v for k, v in ISSUES.items() if not v['leaf']}
types = collections.Counter(v['type'] for v in leaves.values())
out = []
out.append(f'''# Break task: epic → issue → sub-issue

Backlog gồm **11 epic, {len(parents)} issue cha và {len(leaves)} issue lá** (404 mục trên GitHub Project, số issue từ #1 đến #404). Cột `#N` là số issue trên Project. Nguồn chia việc là thiết kế chi tiết LAB-4 cộng với `PREMISE.md`.

## 1. Nguyên tắc chia task

**Độ hạt.** Một issue là một màn hình FE (một `SCREEN_ID`) hoặc một RPC/job BE (một `FUNC_ID`). Issue quá lớn hoặc mơ hồ thì tách sub-issue; ngưỡng là khoảng ba ngày công (một ngày công = 7 giờ). Chỗ hay phải tách: migration nhiều bảng, RPC có chuỗi khóa, ca kiểm hai phiên PostgreSQL, màn nhiều trạng thái. Hai issue gộp thành một khi cùng bảng, cùng quyền và cùng bộ kiểm thử (cặp LIST + GET của cùng tài nguyên). Ngoài việc làm theo màn và RPC, có thêm ba loại: `doc` (soạn API Design cho epic), `qa` (kiểm đầu cuối theo luồng) và `clarify` (làm rõ một câu hỏi mở). Số issue lá theo loại: ''' +
           ', '.join(f'{t} {n}' for t, n in sorted(types.items(), key=lambda x: -x[1])) + '.' + '''

**Định nghĩa xong (DoD).** Mỗi issue có: mục tiêu một dòng; phạm vi và ngoài phạm vi (ngoài phạm vi trỏ về epic); DoD là danh sách đánh dấu quan sát được; tham chiếu spec chỉ bằng mã (`FR-`, `ADR-`, `SCREEN_ID`, `FUNC_ID`), không chép nguyên văn; phụ thuộc bằng số issue; nhãn nhóm đặc thù khi thuộc mục 3. Điều kiện chấp nhận lấy từ AC của FR và quy tắc R1..Rn của ADR. Một issue chỉ xong khi mọi dòng DoD tick được; không có dòng "làm xong phần việc" chung chung.

**Cách dùng epic → issue → sub-issue trên Project.**
- *Epic* là một issue loại `epic` (11 issue, #1, #6, #60, #100, #137, #164, #197, #256, #288, #336, #376). Epic có `Mã backlog` `E-NN`, danh sách ngoài phạm vi, và không tự chấm điểm: điểm bằng tổng con.
- *Issue cha* là issue có sub-issue (nhãn `issue-cha`); điểm và giờ bằng tổng con, không khai phụ thuộc.
- *Issue lá* là đơn vị chấm điểm, giao việc và đưa vào sprint. Quan hệ cha-con dùng sub-issue gốc của GitHub.
- Trường trên Project: `Status` (Todo, In Progress, Blocked, Done), `Iteration` (Sprint 1, Sprint 2), `Assignees`, `Người phụ trách (giả định)`, `point` (chỉ SWP), `Giờ ước lượng`, và các trường lọc `Loại`, `Epic`, `Nhóm đặc thù`, `Mã backlog`.
- Phụ thuộc giữa issue lá khai trong thân issue và đã kiểm tự động: không vòng, không khóa lạ ({sum(len(v.get('depends', [])) for v in leaves.values())} cạnh).

## 2. Spec → issue
'''.replace('{sum(len(v.get(\'depends\', [])) for v in leaves.values())}', str(sum(len(v.get('depends', [])) for v in leaves.values()))))

rows = []
for ek, b in BACKLOG.items():
    e = b['epic']
    for sp in e['specs']:
        base = re.split(r'\.\.| ', sp)[0]
        if re.match(r'^(FR|ADR|NFR)-[A-Z]+-\d+', base): base = re.sub(r'-\d+$', '', base)
        if sp.startswith('design/'):
            cell, note = f'toàn bộ {sum(1 for v in leaves.values() if v["epic"] == ek)} issue lá của epic', 'Không. Mỗi `SCREEN_ID_SPEC` thành issue FE, mỗi `FUNC_ID_TECH` thành issue BE'
        else:
            m = [v['n'] for v in leaves.values() if v['epic'] == ek and any(base in x for x in v['specs'])]
            cell = f'{len(m)} issue: ' + nums(m, 10) if m else 'phủ gián tiếp qua spec con của feature'
            note = '—' if m else 'Chưa có issue dẫn riêng mã này; việc nằm trong các issue theo màn và RPC của epic'
        rows.append((sp, f'#{EPIC_NUM[ek]} — {e["title"]}', cell, note))
rows.append(('FR-NTF-004', f'#{EPIC_NUM["E-08"]} — E-08 (ghi chú), #{EPIC_NUM["E-06"]} — E-06', 'không có issue riêng', 'FR-NTF-004 đã gộp vào FR-INC-002 theo P7 (gộp F-033 vào F-023), nên thành một chức năng ở E-06; E-08 chỉ ghi nhận'))
rows.append(('ADR-012', '—', 'không có issue', 'Quy ước trình bày tài liệu LAB-4, không có việc phát triển'))
rows.append(('FR-RPA-008, ADR-014, P17', f'#{EPIC_NUM["E-11"]} — E-11 Di trú dữ liệu', f'{sum(1 for v in leaves.values() if v["epic"] == "E-11")} issue lá', 'Không. FR này ngoài phạm vi LAB-1 nhưng LAB-4 đưa vào'))
out.append(table(['Spec', 'Epic', 'Issue/sub-issue', 'Phần spec chưa thành issue và vì sao'], rows))

out.append('\nCả 47 FR của REQ-001 §4, 42 màn (S-001 đến S-042), 132 API và 15 ADR đều có issue, trừ hai ngoại lệ ở cuối bảng (kiểm bằng script lúc rà cuối: không có FR, màn, API nào bị bỏ sót).\n\n## 3. Hạng mục chịu ràng buộc đặc thù của đề\n')
out.append('Mỗi hạng mục dưới đây có issue riêng, không nằm lẫn trong issue CRUD, và được gắn trường `Nhóm đặc thù` trên Project để lọc. Một issue có thể chạm nhiều nhóm; trường `Nhóm đặc thù` ghi nhóm chính, còn cột Issue liệt kê theo nội dung (từ khóa trong nhãn đặc thù của issue).\n')
KW = {  # ràng buộc → (từ khóa trong special, giải thích vì sao tách)
    '完納奨励金 (thưởng thanh toán đủ đúng hạn), tỷ lệ có phiên bản': (['完納奨励金'], 'Tỷ lệ đổi theo phiên bản 業務規程, tính khi khóa ngày và sinh delta khi sửa sau chốt; gộp F-033 vào F-023 (P7, ADR-003). Sai ở đây là sai tiền thưởng, nên tính, vòng đời phiên bản và delta tách ba nhóm việc riêng'),
    '業務規程 có phiên bản': (['業務規程'], 'Một chợ, quy tắc theo phiên bản có hiệu lực theo ngày (P1, ADR-003). Mọi nghiệp vụ đọc tham số từ một nguồn; nhúng vào từng issue sẽ rải hằng số khắp nơi'),
    '許可 và 承認 (gỡ tạm dừng có điều kiện, 再審査)': (['許可/承認', '失効', 'căn cứ chờ'], 'Hai khái niệm khác nhau, hai trạng thái và luật chuyển khác nhau cho 仲卸 và 売買参加者 (P3, P24, ADR-004, BP-a); có job hết hạn hằng ngày'),
    '参加上限 (hạn mức mua trong ngày)': (['参加上限'], 'Kiểm hai lần, lúc tạo và lúc chốt giao dịch, trong cùng chuỗi khóa (P4, P16, ADR-013); sai thì vượt hạn mức hoặc chặn nhầm'),
    '締め (chốt sổ) và không chốt khi còn giao dịch pending': (['締め chốt sổ'], 'Khóa ngày kéo theo nhiều bảng; điều kiện không còn `pending` phải kiểm trong cùng giao dịch (P5, P19, ADR-005, ADR-015)'),
    '締め再開 hai người duyệt, chỉ ngày gần nhất trong N ngày': (['締め再開'], 'Hai người khác nhau duyệt, giới hạn cửa sổ ngày (P5, P25, ADR-005); luồng riêng với chốt sổ vì quyền, trạng thái và tham số khác'),
    'Sửa sau chốt chỉ bằng 逆仕訳 hoặc 差額記録': (['sửa sau chốt'], 'Không ghi đè dữ liệu đã khóa (P6, ADR-006); bút toán và giá trị hiệu lực là một thiết kế riêng'),
    'Audit bất biến: trigger chặn sửa/xóa, hash-chain, job kiểm tra hằng ngày': (['audit bất biến'], 'Nền tảng chung cho mọi nghiệp vụ (P11, ADR-008); chuỗi băm và job kiểm tra không thể làm kèm trong issue nghiệp vụ'),
    'Offline chỉ cho F-006 và F-007; giao dịch và chốt sổ bắt buộc online': (['offline'], 'Chỉ hai chức năng được phép offline (P10, ADR-009): hàng đợi, đồng bộ, FIFO, xung đột; phần còn lại cố ý chặn khi mất mạng'),
    'Outbox + worker (thông báo, SFTP CSV, retry cho Critical)': (['outbox'], 'Gửi tin và xuất tệp tách khỏi giao dịch nghiệp vụ (P12, P23, ADR-007); retry, claim, kết quả muộn là bài toán riêng'),
    'MFA bắt buộc cho ROLE-005, 006, 007': (['MFA'], 'Mức xác thực aal2 áp lên nhiều RPC và màn (P9, ADR-010); đăng nhập, đăng ký yếu tố, khôi phục thành issue riêng, các màn khác chỉ dùng guard chung'),
    'Di trú dữ liệu ban đầu (rehearsal, đối chiếu, rollback)': (['di trú'], 'Ngoài phạm vi LAB-1; có diễn tập, đối chiếu và rollback (P17, ADR-014); rủi ro cao nhất khi go-live nên có epic riêng E-11'),
    'Khóa ngày hai lớp (bổ sung ngoài đề)': (['khóa ngày hai lớp'], 'Chặn ghi vào ngày đã khóa bằng hàm kiểm và trigger, dùng bởi nhiều RPC; tách để một nơi giữ luật'),
}
rows = []
for name, (kws, why) in KW.items():
    ids = sorted(v['n'] for v in leaves.values() if v.get('special') and any(k.lower() in v['special'].lower() for k in kws))
    by = collections.Counter(v['epic'] for v in leaves.values() if v['n'] in ids)
    rows.append((name, f'{len(ids)} issue lá ({", ".join(f"{e} {c}" for e, c in sorted(by.items()))}): ' + nums(ids, 12), why))
out.append(table(['Ràng buộc', 'Issue', 'Vì sao tách riêng'], rows))

out.append('\n\n## 4. Chỗ hở và mâu thuẫn của spec LAB-4 phát hiện khi break\n')
fixes, assumes, index = build()
kinds = collections.Counter(); rows = []
for g in GAPS:
    key = (g['epic'], g['n']); kind, code = index[key]
    if kind == 'skip': continue
    gap = cut(num_text(g['gap']), 230)
    if kind == 'fix': xl = f'Đã sửa thiết kế: PREMISE {code}'
    elif kind == 'assume': xl = f'Giả định: PREMISE {code}'
    elif kind == 'clarify':
        ks = [k for k in keys_in(g['xl']) if '-CLR-' in k] or keys_in(g['xl']); xl = 'Tạo issue làm rõ ' + (', '.join(f'#{NUM[k]}' for k in ks[:2]) or '(xem epic)')
    elif kind == 'dod':
        ks = keys_in(g['xl']); xl = 'Để mở: đã ghi vào DoD ' + (nums([NUM[k] for k in ks], 4) or 'của issue liên quan') + ', không đổi thiết kế; ' + cut(re.sub(r'^(Đã phản ánh vào DoD|Đã phản ánh|Phản ánh vào|Giữ nguyên theo SPEC)[:\s]*', '', body(g['xl'])), 150)
    else: xl = 'Để mở: ' + cut(body(g['xl']), 260)
    kinds[kind] += 1
    rows.append((f"{g['epic']} · {g['spec']}", gap, xl))
out.append(f'Ghi nhận **{len(rows)} chỗ hở** ({kinds["fix"]} đã sửa thiết kế, {kinds["assume"]} giả định, {kinds["clarify"]} tạo issue làm rõ, {kinds["open"] + kinds["dod"]} để mở). Cột "Xử lý" trỏ tới dòng `PREMISE.md` (S-xx là sửa/thêm, G-xx là giả định) hoặc số issue làm rõ. Ghi chú: có 5 dòng khi rà chỉ ghi nhận quyết định đã chốt, không phải chỗ hở thật nên không liệt kê.\n')
out.append(table(['Spec', 'Chỗ hở/mâu thuẫn', 'Xử lý'], rows))
text = '\n'.join(out) + '\n'
open('task-breakdown.md', 'w', encoding='utf-8').write(text)
print('task-breakdown.md', len(text), 'ký tự |', len(rows), 'dòng chỗ hở', dict(kinds))
