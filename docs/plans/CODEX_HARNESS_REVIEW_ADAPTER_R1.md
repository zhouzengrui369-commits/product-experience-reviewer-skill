# CODEX_HARNESS_REVIEW_ADAPTER_R1

> Repository: `zhouzengrui369-commits/product-experience-reviewer-skill`  
> Program: `ECOSYSTEM-CODEX-HARNESS-R1`  
> State: `QUEUED / PLANNING_ONLY`  
> Owner: Product Experience Reviewer Skill Project PM  
> Central capability: `zhouzengrui369-commits/knowme-ecosystem@fd01ef7619a31b7ffca5dd2205a2e31a96fac834`  
> Central PR: `knowme-ecosystem#21`  
> Parent PM Gateway/Runner: `chatgpt-parent-pm#12` / `chatgpt-parent-pm#14`  
> Runner plan: [`REVIEWER_SELF_HOSTED_RUNNER_ADOPTION_R1.md`](./REVIEWER_SELF_HOSTED_RUNNER_ADOPTION_R1.md)

## 1. Purpose

Add an opt-in, read-only Codex Harness support adapter for source/static review, candidate/evidence identity reconciliation, evidence indexing, checklist/findings drafts and resumable read-only sessions.

It cannot substitute for real browser/App/device operation, native filesystem/process behavior, actual export, trusted keyboard, product repair/deployment or Human Owner judgment.

## 2. Execution-plane boundary

```text
GitHub Self-hosted Runner
  = Reviewer source/test execution or separately authorized frozen-Candidate deployment support

Codex Harness
  = optional Sol/xhigh read-only source/evidence analysis inside Runner authority

Real product tool
  = actual browser/App/device journey
```

Neither Runner nor Harness may claim a product journey it did not perform.

## 3. Protected lanes

Before activation, re-read live GitHub truth for:

- Reviewer Core/profiles/release/contracts;
- Spatial PR #1;
- Digital Twin Trust PR #2;
- Harness PR #4 / Issue #5;
- consumer Project PM invocation and exact Candidate requirements;
- central Runner/Gateway readiness.

This plan changes no consumer source or historical report.

## 4. Fixed policy

```text
REVIEW_PROFILE=Sol/xhigh
SANDBOX=read-only
SILENT_FALLBACK=FORBIDDEN
CONTRACT_LABEL_strongest=FORBIDDEN
CONSUMER_PRODUCT_MUTATION=NO
D2_D3_PUBLIC_EVIDENCE=NO
REAL_PRODUCT_TOOL_REQUIRED_WHEN_CLAIMED=YES
REVIEWER_PASS_IS_OWNER_PASS=NO
RUNNER_REQUEST_REQUIRED=YES
```

## 5. Allowed R1 inputs

- public/source code and docs;
- exact candidate/PR/SHA metadata;
- sanitized evidence manifests;
- synthetic D0/D1 fixtures;
- redacted screenshots/observations;
- artifact/runtime hashes and normalized receipts;
- consumer Project Profile and Review Request.

## 6. Forbidden R1 inputs/actions

- consumer source edits;
- product Runtime start/stop except a separate product-local deployment request;
- D2/D3/production PII in ordinary prompts/evidence;
- unredacted secrets/private files;
- App Server or Runner event presented as real product interaction;
- synthetic key presented as trusted native keyboard;
- historical report rewrite;
- merge/release or Human Owner decision.

## 7. Evidence-layer boundary

```text
PLANNING
SOURCE_STATIC
TEST_BUILD
LOCAL_RUNTIME
PRODUCT_EXPERIENCE
HUMAN_OWNER
MERGE_RELEASE
```

Harness directly supports the first three and indexes higher-layer evidence. Runner may provide a technical deployment/health receipt. Neither creates a higher-layer PASS automatically.

Required invariants:

```text
HARNESS_SOURCE_REVIEW_PASS != PRODUCT_RUNTIME_PASS
RUNNER_DEPLOYMENT_PASS != PRODUCT_EXPERIENCE_PASS
APP_SERVER_EVENT != REAL_BROWSER_OR_APP_INTERACTION
SYNTHETIC_KEY_EVENT != TRUSTED_NATIVE_KEYBOARD
REVIEWER_PASS != HUMAN_OWNER_PASS
```

## 8. Activation prerequisites

- [ ] live PR #1/#2/#4 and Reviewer Core restored;
- [ ] explicit transition/non-conflicting Goal;
- [ ] central Runner registration topology/Gateway accepted;
- [ ] stable Codex Binary/Protocol Lock and Sol/xhigh;
- [ ] complete opt-in Review Request/Candidate identity;
- [ ] repository-local GOAL/TASK/PLAN/RESULT/EVIDENCE/commands.log;
- [ ] read-only path/network/data policy;
- [ ] redaction/no-consumer-mutation proof;
- [ ] real product tool/worker identified when required.

Until then:

```text
REVIEWER_HARNESS_STATE=QUEUED
```

## 9. Milestones

### RH0 — Current truth and profile mapping

Map central Runner/Harness contracts to existing Reviewer Request/Profile without weakening exact Candidate or evidence requirements.

### RH1 — Read-only Review Envelope

Validate exact repository/project/goal/branch/Candidate/artifact/runtime/test-data, review mode, protected evidence, Sol/xhigh, read-only sandbox, network policy, claim ceiling and next authority.

### RH2 — Evidence identity reconciliation

Prove rejection of mixed/stale/predecessor evidence, source-to-Runtime claim escalation, missing artifact/runtime/test-data identity and unredacted private content.

### RH3 — Findings-draft support

Harness may draft issue/severity/expected/actual/evidence/reproducibility/Candidate/claim-layer/focused-retest fields. Actual observations require a human/independent reviewer or real product tool.

### RH4 — Runner/real-product boundary trial

Runner provides source/test or frozen-Candidate deployment receipt; real tools operate the journey; final report distinguishes deployment evidence, tool observations and reviewer judgment.

### RH5 — Multi-product cold-start and Owner Reviewer Gate

Trial KnowMe, one of Lingxi/AOG/Copilot and a prohibited/incomplete identity fixture. Require no consumer mutation, exact Sol/xhigh, rollback and Human Owner Reviewer Extension decision.

## 10. Required blockers

- incomplete/mixed/stale Candidate evidence;
- source/test or Runner deployment presented as product PASS;
- synthetic event as product interaction;
- D2/D3/PII without Gate;
- consumer mutation;
- non-read-only sandbox;
- Sol/xhigh unavailable/silent fallback;
- Reviewer presented as Product PM/Human Owner;
- real operation required but no tool evidence.

## 11. Evidence contract

Record central Runner/Harness pins, RunnerProfile/request hashes, Binary/Schema/model, Reviewer source/final SHA, Review Request/Task hashes, Candidate/artifact/runtime/test-data, evidence layer/index hashes, redaction/no-mutation, Runner deployment receipt, real product-tool references, findings draft versus final disposition, process terminal state, first blocker and next authority.

## 12. Claim ceiling

```text
PLANNING_ONLY
CURRENT_REVIEWER_PR1_PR2_GATE_CHANGE=NO
RUNNER_ADAPTER=NOT_STARTED
CODEX_HARNESS_REVIEW_ADAPTER=NOT_STARTED
CONSUMER_PRODUCT_MUTATION=NO
REAL_PRODUCT_OPERATION_PROOF=NO
PRODUCT_EXPERIENCE_PASS=NO
HUMAN_OWNER_PRODUCT_VERDICT=NO
AUTO_MERGE_RELEASE=NO
REVIEWER_PM_ACTIVATION_REQUIRED
```
