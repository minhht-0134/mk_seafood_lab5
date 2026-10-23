#!/usr/bin/env python3
"""Kiểm phụ thuộc toàn bộ backlog (E-01..E-11): phân giải khóa tạm theo bảng ánh xạ ở
notes/cross-epic-keys.md, rồi kiểm (1) khóa không tồn tại hoặc chưa phân giải, (2) vòng phụ thuộc
(gồm cạnh container→con). Thoát mã 1 khi có khóa chưa phân giải hoặc có vòng.
Dùng: python3 scripts/backlog/check-cross-epic-cycles.py [--selftest]"""
import glob, json, re, sys

# Tiền tố khóa tạm (khớp theo tiền tố dài nhất) → khóa thật
ALIAS = {
    'E02-LOT-JUDGMENT-QUEUE': ['E02-BE-02'],
    'E02-LOT-OFFLINE-QUEUE': ['E02-FE-01'],
    'E03-TRD-CREATE': ['E03-BE-02'],
    'E03-TRD-DB': ['E03-DB-01'],
    'E03-TRD-LIMIT-USAGE': ['E03-BE-07'],
    'E03-TRD-LIST': ['E03-BE-08'],
    'E04-ADJ-DB': ['E04-DB-02', 'E04-DB-03'],
    'E04-ADJ-DECIDE': ['E04-BE-03'],
    'E04-ADJ-LOCKED-DAY-BLOCK': ['E04-FE-03'],
    'E04-ADJ-LOCKED-DAY-GUARD': ['E04-DB-04'],
    'E04-ADJ-REQUEST-LIST': ['E04-BE-02'],
    'E05-CLS-DAY-LIST': ['E05-BE-01'],
    'E05-CLS-DAY (': ['E05-BE-03'],
    'E05-CLS-REOPEN': ['E05-BE-04', 'E05-BE-05'],
    'E06-INC-DB': ['E06-DB-01'],
    'E06-INC-POST-LOCK-DELTA': ['E06-BE-04'],
    'E06-INC-RULE-VERSION-LIST': ['E06-BE-09'],
    'E06-INC-RULE-VERSION (': ['E10-DB-05'],
    'E07-DLV-LIST': ['E07-BE-01'],
    'E08-NTF-CONFIG': ['E08-DB-01'],
    'E08-NTF-CRITICAL': ['E08-BE-08b', 'E08-BE-08c'],
    'E08-NTF-INBOX': ['E08-BE-06', 'E08-BE-07'],
    'E08-NTF-OPS-ALERT-LIST': ['E08-BE-03'],
    'E09-WORKER': ['E09-BE-05', 'E09-BE-06', 'E09-DB-02', 'E09-DOC-01b'],
    'E10-CORE-DB (nền tảng chung)': ['E10-DB-01', 'E10-DB-02'],
    'E10-CORE-DB (business_days': ['E10-DB-03', 'E10-DB-04', 'E10-DB-05'],
    'E10-AUDIT-WRITE': ['E10-AUD-02'],
    'E10-OUTBOX': ['E10-OBX-01', 'E10-OBX-02', 'E10-OBX-03'],
    'E10-AUTH-GUARD': ['E10-DB-02'],
    'E10-SYS-EVIDENCE': ['E10-SYS-02'],
    'E10-SYS-ME': ['E10-SYS-01'],
    'E10-PROXY-GUARD': ['E10-PRX-01', 'E10-PRX-02', 'E10-API-01'],
    'E10-API-ERROR-MAPPING': ['E10-API-02'],
    'E10-STORAGE': ['E10-STO-01'],
    'E11-DB (migration_record_links': ['E11-DB-03'],
}
# Khóa tạm E07-DLV-DB: khóa thật phụ thuộc bên gọi (cross-epic-keys.md, phần E-07)
DLV_BY_CALLER = {
    'E03-BE-04c': ['E07-DB-01'], 'E04-BE-03a': ['E07-DB-01'],
    'E05-BE-02a': ['E07-DB-01'], 'E05-BE-02b': ['E07-DB-01', 'E07-DB-02', 'E07-DB-03'],
    'E06-BE-01b': ['E07-DB-01'], 'E06-BE-03': ['E07-DB-01'], 'E06-QA-01': ['E07-BE-03'],
}


def pref(d):
    m = re.match(r'(E\d\d-[A-Z]+-\d+[a-z]?)', d)
    return m.group(1) if m else d


def resolve(caller, dep, real):
    if dep.startswith('E07-DLV-DB'):
        return DLV_BY_CALLER.get(caller)
    hits = [a for a in ALIAS if dep.startswith(a)]
    if hits:
        return ALIAS[max(hits, key=len)]
    for cand in (pref(dep), dep):
        if cand in real:
            return [cand]
    return None


def check(G, cont, real):
    edges, missing = {}, []
    for k, ds in G.items():
        out = []
        for d in ds:
            r = resolve(k, d, real)
            if r is None:
                missing.append((k, d))
                continue
            bad = [x for x in r if x not in real]
            if bad:
                missing.append((k, d + ' -> ' + ','.join(bad)))
                continue
            out += r
        edges[k] = out + cont.get(k, [])
    state, cycle = {}, []

    def dfs(u, path):
        state[u] = 1
        for v in edges.get(u, []):
            if state.get(v) == 1:
                cycle.append(path + [u, v]); return True
            if state.get(v) is None and dfs(v, path + [u]):
                return True
        state[u] = 2
        return False
    for k in list(edges):
        if state.get(k) is None and dfs(k, []):
            break
    return missing, cycle


def selftest():
    real = {'A', 'B', 'E10-DB-01', 'E10-DB-02'}
    m, c = check({'A': ['B'], 'B': ['A']}, {}, real)
    assert c, 'phải thấy vòng'
    m, c = check({'A': ['E99-XYZ-1'], 'B': []}, {}, real)
    assert m and not c, 'phải báo khóa chưa phân giải'
    m, c = check({'A': ['E10-CORE-DB (nền tảng chung)'], 'B': []}, {}, real)
    assert not m and not c, 'alias hợp lệ'
    m, c = check({'A': ['B'], 'B': []}, {'A': []}, real)
    assert not m and not c, 'đồ thị sạch'
    print('selftest đạt')


def main():
    if '--selftest' in sys.argv:
        selftest(); return 0
    G, real, cont = {}, set(), {}
    for f in sorted(glob.glob('scripts/backlog/e-[0-9]*.json')):
        for i in json.load(open(f, encoding='utf-8'))['issues']:
            real.add(i['key']); G[i['key']] = list(i.get('depends', [])); cont[i['key']] = i.get('parent_of', [])
    missing, cycle = check(G, cont, real)
    for k, d in missing:
        print('CHƯA PHÂN GIẢI:', k, '->', d)
    for c in cycle:
        print('VÒNG:', ' -> '.join(c))
    print('issue', len(real), '| chưa phân giải:', len(missing), '| vòng:', bool(cycle))
    return 1 if (missing or cycle) else 0


if __name__ == '__main__':
    sys.exit(main())
