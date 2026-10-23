#!/usr/bin/env python3
"""Ghép kết quả chấm của 5 lô + dữ liệu issue thành payload nội bộ cho tkm:sun-estimate.
Dùng: python3 scripts/swp/build-payload.py  → scripts/swp/work/payload.json (+ báo lỗi kiểm)"""
import json, glob, collections
W = 'scripts/swp/work/'
sel = json.load(open(W + 'select-out.json'))
asm = {}
for f in sorted(glob.glob(W + 'out-*.json')):
    for a in json.load(open(f))['assessments']:
        k = (a['sourceType'], a['issueRef'])
        assert k not in asm, k
        asm[k] = a
# Hiệu chỉnh sau review của Codex (notes/swp-codex-review-result.md, B01–B16): (Scope, Complexity, chữ ký thêm, chữ ký bỏ, ghi chú)
CX = {113: (3, 3, ['concurrency'], [], 'B01'), 116: (3, 3, ['concurrency'], [], 'B02'), 117: (3, 3, ['concurrency'], [], 'B03'),
      29: (2, 3, ['concurrency'], [], 'B04'), 70: (2, 3, ['concurrency'], [], 'B05'), 79: (3, 3, ['concurrency'], [], 'B06'),
      80: (2, 3, ['concurrency'], [], 'B07'), 179: (2, 3, ['concurrency'], [], 'B08'), 180: (2, 3, ['concurrency'], [], 'B09'),
      232: (2, 3, ['concurrency'], [], 'B10'), 240: (3, 3, ['concurrency'], [], 'B11'), 307: (3, 3, ['concurrency'], [], 'B12'),
      340: (3, 3, ['operational-safety'], [], 'B13'), 369: (3, 3, ['operational-safety'], [], 'B14'),
      383: (3, 1, [], [], 'B15'), 5: (3, 2, [], ['concurrency'], 'B16')}
CV = ['routine', 'stateful', 'concurrency', 'migration', 'external-integration', 'legacy-unknown', 'operational-safety', 'algorithmic']
rows, miss = [], []
for it in sel['selectedIssues']:
    a = asm.get((it['sourceType'], it['issueRef']))
    if not a: miss.append(it['issueRef']); continue
    r = {k: v for k, v in it.items()}
    r.update({k: a[k] for k in ('primaryDiscipline', 'workType', 'scopeSignature', 'complexitySignature', 'initialScope',
              'initialComplexity', 'initialSWP', 'confidence', 'evidenceStatus', 'rationale', 'assumptions', 'gaps',
              'supportingEvidence', 'splitRecommended', 'splitReason')})
    if r['primaryDiscipline'] == 'Unknown':  # schema: Unknown bắt buộc confidence thấp
        if r['workType'] == 'documentation':  # tài liệu API Design → API; MIG-0x → Migration
            r['primaryDiscipline'] = 'Migration' if '[E11-DOC-0' in r['title'] and 'API Design' not in r['title'] else 'API'
        else:  # issue làm rõ: chưa có quyết định của khách, giữ Unknown + thấp
            r.update(confidence='low', evidenceStatus='AMBIGUOUS')
            r['gaps'] = r['gaps'] or ['Chờ quyết định của khách hàng hoặc Tech Lead']
    n = int(it['issueRef'].split('#')[1])
    if n in CX:
        sc, cx, add, drop, tag = CX[n]
        r['initialScope'], r['initialComplexity'] = sc, cx
        r['initialSWP'] = {(3, 3): 6, (2, 3): 4, (3, 1): 4, (3, 2): 5}[(sc, cx)]
        sig = (set(r['complexitySignature']) | set(add)) - set(drop) - {'routine'}
        r['complexitySignature'] = [v for v in CV if v in sig] or ['routine']
        r['rationale'] = r['rationale'][:150].rstrip() + f' [Chỉnh theo review Codex {tag}]'
    if n == 98:  # B17: bằng chứng cho mức 8 do người dùng chốt
        r['rationale'] = 'Người dùng chốt 8 SWP: cần khảo sát trình duyệt và tablet thực tế, ma trận môi trường và khả năng offline trước khi hỏi khách; loại trừ QA mất mạng của #96.'
        r['scopeSignature'], r['complexitySignature'] = ['multi-component'], ['stateful']
        r['gaps'] = ['Chờ quyết định của khách hàng hoặc Tech Lead', 'DoD gốc chưa nêu đầu ra khảo sát']
    rows.append(r)
extra = set(asm) - {(i['sourceType'], i['issueRef']) for i in sel['selectedIssues']}
print('lô:', len(asm), 'dòng:', len(rows), 'thiếu:', miss[:5], 'thừa:', list(extra)[:5])
payload = {'schemaVersion': '2.0', 'scoringModel': 'standard-work-point', 'scoringModelVersion': 'swp-matrix-v2',
  'run': {'sourceFamily': 'github', 'sourceLabel': 'minhht-0134/mk_seafood_lab5 · Project #1', 'sourceUrl': 'https://github.com/users/minhht-0134/projects/1',
          'project': '1', 'period': None, 'generatedAt': '2026-10-22T00:00:00Z', 'calibrationStatus': 'pending',
          'selection': sel['selection']},
  'issues': rows, 'parents': sel['selectedParents'], 'representatives': [], 'corrections': [], 'calibrationRules': [],
  'caveats': ['Takumi composition: confidence=composed; ask-expert=not-needed',
              'Nguồn là Project #1 (404 mục); chấm 350 issue lá, 54 issue cha lấy tổng con.',
              'Trạng thái kiểm tra estimate có sẵn: không khả dụng (không dùng KPI Insight), chấm toàn bộ issue lá đang mở.',
              'Bằng chứng chấm là phần thân issue (mục tiêu, DoD, tham chiếu spec); chưa đọc nguyên văn spec LAB-4 từng issue.']}
json.dump(payload, open(W + 'payload.json', 'w'), ensure_ascii=False)
