# Developer Fix Contract Template (Handoff back to dev thread)

> 评审官写完报告后，把本契约交给开发线程作为下一轮的唯一入口。
> 不在此处要求或暗示修改 Core / Profile。

---

```yaml
to_dev_thread: <thread id / handle>
review_mode: <FOCUSED_RETEST | FULL_EXPERIENCE_REVIEW | …>
candidate_commit: <sha>
artifact_sha256_or_deployment_id: <…>
prior_report: <path>
issues_to_fix:
  - id: <issue id>
    severity: <P0 | P1 | P2>
    acceptance_criteria: <list>
    retest_evidence_required: <list>
regression_must_not_break:
  - <issue id or journey>
new_p0_introduced_this_round:
  - <issue id>
forbidden_changes:
  - <不要做的具体事>
  - <不要做的具体事>
next_round:
  mode: <FOCUSED_RETEST | FULL_EXPERIENCE_REVIEW>
  priority_issues: <ids>
  candidate_identity_required_fields: <list>
```

## Handoff Discipline

- 评审官**不**替开发线程提交产品变更；
- 评审官**不**直接修复问题；
- 评审官**不**改 Core / Profile；改章程需要走 Core §21.4；
- 开发线程交付后，评审官按本契约独立复验，不依赖开发者描述。

## Re-entry Criteria for Next Round

- candidate commit / artifact SHA 必须独立可获取；
- Acceptance Criteria 全部被可重放步骤覆盖；
- Retest Evidence 清单具体到文件名 / 路径；
- 若 issue 在 Profile 之外，需先升级 Profile 再复验。

— end of developer fix contract —