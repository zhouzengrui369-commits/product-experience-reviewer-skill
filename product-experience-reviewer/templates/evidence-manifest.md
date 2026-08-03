# Evidence Manifest Template (Core §20)

> 报告末尾必须挂载的证据索引。
> 任何核心结论若不在本索引中，视为证据缺失。

---

```yaml
report: <path-to-report>
candidate_identity: <path-to-candidate-identity.md>
stage_a_frozen_output: <path-to-frozen-output.md>
blind_user_reviewer_transcript: <path-to-blind-reviewer-transcript>
screenshots:
  - path: <path>
    step: <step id / name>
    candidate_commit: <sha>
    timestamp: <ISO8601>
recordings:
  - path: <path>
    duration_s: <int>
    step: <step id / name>
logs:
  - path: <path>
    candidate_commit: <sha>
artifacts:
  - path: <path>
    sha256: <hex>
    description: <one-line>
templates_used:
  - <template-name>: <path>
prior_report: <path-or-N/A>
```

## Hashing Discipline

- 每个 evidence 文件必须记录其 SHA-256；
- 报告自身与 evidence manifest 的 SHA-256 必须可被 owner 独立核验；
- 不得引用未在本清单中的证据。

## Forbidden Content

- 真实用户数据、真实笔记、真实凭据、真实 API key；
- 任何 secret 形态（见 Core §10 / Skill safety boundaries）；
- 公开或共享证据中的私有绝对路径。若本地候选身份必须记录真实路径，
  只保留在未发布身份清单中，并在公开版本中脱敏。

— end of evidence manifest —
