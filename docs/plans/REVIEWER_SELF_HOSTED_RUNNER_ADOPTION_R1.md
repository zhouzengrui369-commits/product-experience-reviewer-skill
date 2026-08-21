# REVIEWER_SELF_HOSTED_RUNNER_ADOPTION_R1

> Repository: `zhouzengrui369-commits/product-experience-reviewer-skill`  
> Program: `ECOSYSTEM-CODEX-HARNESS-R1`  
> Capability: `github-self-hosted-runner@0.1.0-proposed`  
> State: `QUEUED / PLANNING_ONLY`  
> Owner: Product Experience Reviewer Skill Project PM  
> Central capability: `zhouzengrui369-commits/knowme-ecosystem@fd01ef7619a31b7ffca5dd2205a2e31a96fac834`  
> Parent PM execution plane: `chatgpt-parent-pm#12` / `chatgpt-parent-pm#14`  
> Harness review plan: [`CODEX_HARNESS_REVIEW_ADAPTER_R1.md`](./CODEX_HARNESS_REVIEW_ADAPTER_R1.md)

## 1. Goal

Add a read-only Reviewer adapter to the Parent PM central GitHub Self-hosted Runner Local Execution Plane for:

1. Reviewer source/fixture/test Gates;
2. separate launch/deployment support for a product Parent PM-frozen exact Candidate, after which real browser/App/device tools perform the product journey.

The Runner does not perform reviewer judgment and cannot substitute for real product operation.

## 2. Protected lanes

The Reviewer PM must restore live GitHub truth for:

- Reviewer Core, current release and profiles;
- Spatial Experience Extension PR #1;
- Digital Twin Trust Review PR #2;
- Harness Review Adapter PR #4 / Issue #5;
- report/developer-fix/focused-retest contracts;
- historical reports and consumer Project PM ownership;
- central Runner/Gateway state.

This plan does not modify or relabel PR #1/#2, consumer product source or historical reports.

## 3. Role boundary

### Runner may

- run Reviewer unit/fixture/schema tests;
- build/publish a Reviewer test artifact;
- validate candidate/evidence identity fixtures;
- launch a frozen product Candidate under a separate product-local deployment authority;
- upload sanitized deployment/health receipts.

### Runner may not

- claim real browser/App/device interaction merely from process events;
- claim trusted native keyboard from synthetic dispatch;
- modify consumer product source;
- generate product findings without actual observed evidence;
- decide Product Experience or Human Owner PASS;
- merge/release consumer products.

## 4. Activation prerequisites

- [ ] live Reviewer Core/PR #1/#2/#4 truth restored;
- [ ] explicit transition or non-conflicting successor Goal;
- [ ] central Runner registration topology accepted;
- [ ] Parent PM dispatcher/schemas/security Pilot accepted;
- [ ] fresh Runner health receipt;
- [ ] repository-local GOAL/TASK/PLAN/RESULT/EVIDENCE/commands.log;
- [ ] exact read-only Reviewer task or exact consumer Candidate deployment request;
- [ ] consumer Project PM ownership and complete Candidate identity;
- [ ] real product-operation tool/worker identified when claimed;
- [ ] redaction and no-consumer-mutation contract.

Until then:

```text
REVIEWER_RUNNER_STATE=QUEUED
```

## 5. Fixed policy

```text
MODEL=Sol/xhigh
SANDBOX=read-only
SILENT_FALLBACK=FORBIDDEN
CONSUMER_SOURCE_MUTATION=NO
D2_D3_PUBLIC_EVIDENCE=NO
REAL_PRODUCT_TOOL_REQUIRED_WHEN_CLAIMED=YES
RUNNER_EVENT_IS_PRODUCT_INTERACTION=NO
REVIEWER_PASS_IS_OWNER_PASS=NO
```

## 6. Milestones

### RR0 — Current truth and role boundary

- live Core/PR #1/#2/#4 snapshot;
- central capability pin;
- reviewer source/test versus product deployment task separation;
- first trial Candidate and real tool boundary;
- activation or blocker.

### RR1 — Reviewer test/fixture Runner Gate

- exact Reviewer SHA/tree;
- read-only or bounded repository-owned test/build request;
- synthetic D0/D1 fixtures;
- candidate identity/mixed-SHA/claim-layer negatives;
- complete source/test/build receipt;
- no consumer product mutation.

### RR2 — Candidate identity and deployment receipt mapping

For a product PM-frozen Candidate:

- exact repository/PR/SHA/tree/artifact/runtime/test-data identity;
- separate product-local deployment LocalExecutionRequest;
- fresh worktree/App/Runtime identity;
- deployment/health receipt only;
- no Reviewer PASS claim.

### RR3 — Real product-tool boundary trial

- Runner launches or verifies the exact Candidate;
- real browser/App/device tooling performs the journey;
- observations/screenshots/references are added separately;
- Reviewer final report distinguishes Runner deployment evidence, tool observations and reviewer judgment;
- no synthetic input is presented as native trusted input.

### RR4 — Multi-product cold-start and Owner Reviewer Gate

Trial at least:

- KnowMe;
- one of Copilot/Lingxi/AOG;
- one incomplete/mixed identity negative fixture.

Prove no consumer mutation, exact Sol/xhigh, rollback and Human Owner Reviewer Extension acceptance.

## 7. Codex Harness relationship

The Reviewer Harness adapter may help index evidence and draft findings inside Runner authority, but remains read-only:

```text
Runner request
→ Sol/xhigh read-only Harness session
→ source/evidence index/draft
→ real product tool observations
→ independent reviewer disposition
```

Harness cannot widen the Runner request or repair Runner failures automatically.

## 8. Evidence contract

Required:

- central Runner/Harness pins;
- RunnerProfile/request hashes;
- Reviewer or consumer exact SHA/tree;
- artifact/runtime/test-data identity;
- workflow run/job/attempt;
- fresh worktree/task/evidence roots;
- source/test/deployment receipt;
- real tool observation references where required;
- redaction/no-mutation/process results;
- evidence-layer and claim ceiling;
- first blocker and next authority.

## 9. Claim ceiling

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

## 10. First takeover output

```text
REVIEWER_SELF_HOSTED_RUNNER_TAKEOVER_COMPLETE
CURRENT_REVIEWER_CORE_SHA=
CURRENT_PR1_SHA=
CURRENT_PR2_SHA=
CENTRAL_CAPABILITY_SHA=
PARENT_PM_LOCAL_EXECUTION_PLANE_STATE=
REVIEWER_RUNNER_STATE=QUEUED|ACTIVATED|BLOCKED
FIRST_USE_CASE=
FROZEN_PRODUCT_CANDIDATE=
RUNNER_CANDIDATE_DEPLOYMENT_RECEIPT=
REAL_PRODUCT_TOOL_REQUIRED=YES
MODEL_PROFILE=Sol/xhigh
CONSUMER_MUTATION=NO
CURRENT_FIRST_BLOCKER=
NEXT_GOAL=
NEXT_AUTHORITY=
HUMAN_OWNER_PRODUCT_VERDICT=NO
```
