# Focused Retest Template (Core §19.1)

> 优先于 Full Review。仅复验上轮明确问题 + 检查回归。
> 不重写完整长报告。

---

```yaml
review_mode: FOCUSED_RETEST
candidate: <…>
commit: <…>
artifact_sha256_or_deployment_id: <…>
prior_report: <path-to-previous-review>
retest_target_issues:
  - <issue id>
  - <issue id>
isolation_status: <BLIND_TEST | PRIMED_COGNITIVE_WALKTHROUGH>
```

## 1. Owner Decision Brief (compressed)

```yaml
product_experience_verdict: <…>
release_evidence_verdict: <…>
prototype_concept_verdict: <…>
prototype_to_runtime_parity: <…>
prior_p0_status:
  - <issue>: <OPEN | PARTIALLY_FIXED | CLOSED | REGRESSED | N/A_CURRENT_SCOPE | BLOCKED>
new_p0:
  - <id / one-line>
dev_thread_must_finish:
  - <id / one-line>
  - <id / one-line>
owner_recommendation:
  - [ ] 放行
  - [ ] 修复后定向复验
  - [ ] 继续探索，不进入发布候选
  - [ ] 退回重新定义
```

## 2. Candidate Identity (delta only)

仅记录与上轮相比的变化（commit、working tree、artifact SHA、构建命令、运行时、provider、网络、配置）。其余字段引用上轮并显式声明 no-change。

## 3. Retest Steps per Issue

```yaml
issue: <id>
acceptance_criteria_replayed:
  - step | expected | actual | evidence
closed: <YES | NO>
regression: <NONE | DETECTED: <id>>
new_evidence: <path>
```

## 4. Regression Sampling (P1)

- 列出本轮主动复验的 P1（仅声明需要复验的，不要全旅程）。
- 每条按 §3 格式记录。

## 5. Verdict Diff vs Prior

| Verdict | Prior | Current | Reason |
|---|---|---|---|
| Product Experience | … | … | … |
| Release Evidence | … | … | … |

## 6. Human Owner Gate

`HUMAN_OWNER_GATE_REQUIRED` 或 `HUMAN_OWNER_GATE_NOT_ELIGIBLE`。

## 7. Evidence Index

`templates/evidence-manifest.md`。

— end of focused retest template —