# Frozen Output Template (Stage A output)

> 由 Blind User Reviewer 在隔离状态下完成。
> **进入 Stage B 之前必须冻结**。冻结后任何字节变更视为流程违规，
> 必须在报告中显式声明并降级 Verdict。

---

## Frozen At

```yaml
frozen_at: YYYY-MM-DDTHH:MM:SSZ
isolation_status: <BLIND_TEST | PRIMED_COGNITIVE_WALKTHROUGH>
reviewer_role: <target user identity>
candidate_entry: <URL | path | app id>
hash_of_brief: <sha256 of blind-brief.md used>
```

## Required Answers (each ≤ 80 words)

1. 我认为这是什么产品？
2. 它解决什么问题？
3. 我是否始终知道下一步？（什么时候知道 / 不知道）
4. 哪一刻让我信任它？
5. 哪一刻让我困惑或出戏？
6. 我是否理解系统状态？
7. 我是否愿意继续使用或交付真实数据？
8. 它表现出怎样的产品人格？

## One-line Verdict (≤ 200 字)

> 仅根据实际使用，我认为该产品是 ……

## Evidence Index (Stage A only)

- `<path-to-screenshot-or-recording-1>`
- `<path-to-screenshot-or-recording-2>`
- …

## Freeze Declaration

```
SIGNED_BY_REVIEWER: <id>
NO_STAGE_B_READ_BEFORE_THIS_LINE: <timestamp>
NO_MODIFICATION_AFTER_FREEZE: <sha256 of this file at freeze time>
```

— end of frozen output —