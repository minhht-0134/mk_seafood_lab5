"""Phân loại bảng chỗ hở và đánh số dòng PREMISE (S-xx sửa/thêm, G-xx giả định) dùng cho PREMISE.md và task-breakdown.md."""
import json, re
from docs_data import cut, keys_in, num_text, NUM, EPIC_NUM

GAPS = json.load(open('scripts/docs/gaps.json', encoding='utf-8'))
NON_GAP = {('E-04', '7'), ('E-04', '9'), ('E-04', '13'), ('E-04', '15'), ('E-05', '8')}  # ghi nhận "không phải chỗ hở"
D8_ROWS = {(g['epic'], g['n']) for g in GAPS if g['epic'] and g['n'] == '1' and 'mục Thêm' in g['xl']}
PREFIX = re.compile(r'^(\*\*[^*]*\*\*\s*)?(Dự kiến sửa thiết kế|Đã sửa thiết kế|Giả định|Tạo issue làm rõ|Để mở và vì sao|Để mở)'
                    r'\s*(\([^)]*\))?\s*[:,]?\s*')


def body(s):
    return num_text(PREFIX.sub('', s, count=1).strip()) or num_text(s)


def classify(g):
    k = g['kind']
    if (g['epic'], g['n']) == ('E-04', '6'):
        return 'fix'
    if k == 'other':
        return 'skip' if (g['epic'], g['n']) in NON_GAP else 'dod'
    return k


def build():
    """Trả về (sửa, giả định, chỉ mục) với chỉ mục (epic, n) -> (loại, mã PREMISE hoặc None)."""
    fixes, assumes, index = [], [], {}
    sid = gid = 1
    for g in GAPS:
        key = (g['epic'], g['n']); kind = classify(g)
        if key in D8_ROWS:
            index[key] = ('fix', 'S-01'); continue
        if kind == 'fix':
            sid += 1; code = f'S-{sid:02d}'; fixes.append((code, g)); index[key] = ('fix', code)
        elif kind == 'assume':
            code = f'G-{gid + 6:02d}'; gid += 1; assumes.append((code, g)); index[key] = ('assume', code)
        else:
            index[key] = (kind, None)
    return fixes, assumes, index
