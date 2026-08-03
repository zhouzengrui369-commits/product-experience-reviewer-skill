# Full Experience Review Template (Core §20)

> 完整重评使用。FOCUSED_RETEST 请使用 `templates/focused-retest.md`。

```text
reports/product-review/YYYY-MM-DD-<project>-product-experience-review.md
reports/product-review/YYYY-MM-DD-<project>/evidence/
```

---

## 1. Owner Decision Brief

```yaml
review_mode: <…>
candidate: <…>
commit: <…>
artifact_sha256_or_deployment_id: <…>
product_experience_verdict: <…>
release_evidence_verdict: <…>
prototype_concept_verdict: <…>
prototype_to_runtime_parity: <…>
core_promise: <…>
core_promise_holds: <YES | NO | PARTIAL | N/A>
prior_p0_status:
  - <issue>: <OPEN | PARTIALLY_FIXED | CLOSED | REGRESSED | N/A_CURRENT_SCOPE | BLOCKED>
new_p0:
  - <id / one-line>
  - <id / one-line>
top_positive_signals:
  - <one-line evidence>
  - <one-line evidence>
  - <one-line evidence>
dev_thread_must_finish:
  - <id / one-line>
  - <id / one-line>
  - <id / one-line>
next_round_focused_retest_only:
  - <id / one-line>
  - <id / one-line>
  - <id / one-line>
owner_recommendation:
  - [ ] 放行
  - [ ] 修复后定向复验
  - [ ] 继续探索，不进入发布候选
  - [ ] 退回重新定义
```

## 2. Candidate Identity

`templates/candidate-identity.md` 的完整内容。

## 3. Review Mode

引用 Core §4。

## 4. Stage A Frozen Output

`templates/frozen-output.md` 的冻结字节（SHA-256 必须可核验）。

## 5. Stage B Positioning Reconciliation

引用 Core §7，列出 5 项并给出明确结论。

## 6. Scope & N/A

| Journey / Dimension | Status | Reason |
|---|---|---|
| … | IN_CURRENT_RELEASE_SCOPE / OUT_OF_CURRENT_RELEASE_SCOPE / AMBIGUOUS_SCOPE | … |

## 7. Runtime User Journey Walkthrough

每条旅程使用：

```text
Journey: <name>
Steps:
  - step | expected | actual | user_feeling | evidence_path | candidate_version | timestamp
Verdict: <PASS | FAIL | N/A>
IssueRefs: [<issue ids>]
```

## 8. Prototype Review (if any)

独立 lane。明确 `Prototype Concept Verdict` 与证据。

## 9. Prototype-to-Runtime Parity

| Experience | Where |
|---|---|
| In Runtime | … |
| Only in Prototype | … |
| Divergent | … |
| Not yet productized | … |

## 10. Inheritance Matrix

| Issue | Prior | Current | Evidence | Closed? | Regressed? |
|---|---|---|---|---|---|

## 11. Runtime Scoring

每条使用 Core §12 模板：

```text
Dimension: <…>
Score: <1-5>
Applicable: <YES | N/A — OUT_OF_CURRENT_SCOPE | AMBIGUOUS_SCOPE>
Evidence: <path>
Reason: <one-line>
```

## 12. Issues P0–P3

每条 P0 / P1 / 关键 P2 使用 `templates/issue-contract.md`。

## 13. Acceptance Criteria & Focused Retest Steps

每个 P0 写明：可重放步骤、Acceptance Criteria、Retest Steps、Retest Evidence 要求、Regression Risk。

## 14. Four Verdicts

| Verdict | Value | Reason |
|---|---|---|
| Product Experience Verdict | … | … |
| Release Evidence Verdict | … | … |
| Prototype Concept Verdict | … | … |
| Prototype-to-Runtime Parity | … | … |

## 15. Human Owner Gate

`HUMAN_OWNER_GATE_REQUIRED` (P0=0 时) 或 `HUMAN_OWNER_GATE_NOT_ELIGIBLE`（P0>0）。

## 16. Evidence Index

`templates/evidence-manifest.md`。

— end of full review template —