# Issue Contract Template (Core §14)

> 每个 P0 / P1 / 关键 P2 必须使用本模板。**不得只写“建议优化”。**

---

```markdown
## <Issue ID> / <Title>

Severity: <P0 | P1 | P2 | P3>
Journey: <Project Profile §3 旅程 id>
User Promise Violated: <从 Profile §1 / §3 引用>
Observed Behavior: <一次或多次真实操作的客观描述，含失败 / 不一致 / 缺失>
Expected Behavior: <按 Profile §1 / §3 的承诺，用户应当感受到 / 看到什么>
Evidence:
  - <path-to-screenshot-or-recording>
  - <path-to-log>
  - <path-to-artifact>
  - <candidate commit / sha256>
Likely User Impact: <真实用户后果，不写“可能影响体验”这种空话>
Current Scope: <IN_CURRENT_RELEASE_SCOPE | OUT_OF_CURRENT_RELEASE_SCOPE | AMBIGUOUS_SCOPE>
Required Behavior: <关闭问题后必须满足的具体行为>
Acceptance Criteria:
  - <可重放步骤 + 期望状态>
  - <可重放步骤 + 期望状态>
Focused Retest Steps:
  - <step>
  - <step>
Required Retest Evidence:
  - <截图 / 录屏 / 日志 / 产物 清单>
Regression Risk:
  - <相关旅程>
  - <潜在冲突>
```

## 关闭条件

- Acceptance Criteria 全部满足；
- Retest Evidence 完整；
- 没有引入新 P0 / 关键 P1；
- 评审官独立复现，而非开发者口述。

— end of issue contract —