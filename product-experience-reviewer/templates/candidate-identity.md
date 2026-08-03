# Candidate Identity Template (Core §5)

> 开始操作前必须如实填写。**任何字段为空即视为不可复现候选**，
> 必须给出 `Release Evidence Verdict = BLOCKED_NON_REPRODUCIBLE_CANDIDATE`。

---

```yaml
review_mode: <RELEASE_CANDIDATE_REVIEW | EXPLORATORY_PRODUCT_REVIEW | FOCUSED_RETEST | FULL_EXPERIENCE_REVIEW>
repository: <absolute path or url>
branch: <branch>
commit_sha: <full sha>
working_tree_status: <CLEAN | DIRTY | UNTRACKED | FROZEN>
candidate_app_or_package_or_url: <path or url>
candidate_sha256_or_deployment_id: <sha256 or deployment id, or N/A — SOURCE_RUN_ONLY>
build_command: <exact command line, or N/A — SOURCE_RUN_ONLY>
build_timestamp: <ISO8601, or N/A — SOURCE_RUN_ONLY>
os: <darwin | linux | windows | other>
architecture: <arm64 | x86_64 | other>
device: <model or VM id>
browser_or_runtime: <Electron X.Y.Z | Chrome X | Node X | …>
backend_version: <commit or tag, or N/A>
database_or_dataset_state: <sha or seed name>
model_or_provider: <provider / model / endpoint>
network_state: <OFFLINE | LOOPBACK | INTRANET | PUBLIC, with disclosure>
configuration_snapshot: <path or sha, or "current UI defaults">
previous_review: <path or url>
```

## Identity Gate Decision

```yaml
identity_gate: <PASS | DOWNGRADE>
downgrade_reason: <if DOWNGRADE, cite the missing field>
release_evidence_verdict: <RELEASE_EVIDENCE_READY | BLOCKED_NON_REPRODUCIBLE_CANDIDATE | BLOCKED_MISSING_ARTIFACT_HASH | BLOCKED_MISSING_BASELINE_PIN | BLOCKED_INCOMPLETE_EVIDENCE>
```

## Signed By

```
SIGNED_BY_REVIEWER: <id>
SIGNED_AT: YYYY-MM-DDTHH:MM:SSZ
```

— end of candidate identity —