# CODEX_HARNESS_REVIEW_ADAPTER_R1

> Repository：`zhouzengrui369-commits/product-experience-reviewer-skill`  
> Program：`ECOSYSTEM-CODEX-HARNESS-R1`  
> State：`QUEUED / PLANNING_ONLY`  
> Execution owner：Product Experience Reviewer Skill Project PM  
> Central capability：`zhouzengrui369-commits/knowme-ecosystem@8ccb543804a7881fd37b31e1ce35085ca7285a76`  
> Central Draft PR：`knowme-ecosystem#21`  
> Reference Gateway plan：`chatgpt-parent-pm#12`  
> Creation base：`chatgpt/v03-digital-twin-review-plan-r1@39c63bdf94587c488cf48a7e7269694e6b4064d0`

## 1. Purpose

Add an opt-in, read-only Codex Harness support adapter for Product Experience Reviewer workflows.

The adapter may help with:

- source/static review;
- candidate/artifact/runtime/test-data identity reconciliation;
- evidence manifest indexing;
- review checklist generation;
- findings and report drafts;
- protected evidence hash/index maintenance;
- resumable read-only review sessions.

It cannot substitute for:

- real browser, App or device operation;
- native file picker/filesystem/process behavior;
- actual PPTX/PDF export;
- trusted native keyboard input;
- physical mobile/watch evidence;
- product source repair;
- product deployment;
- Human Owner value decision.

## 2. Current protected lanes

Before activation, the Reviewer PM must re-read live GitHub truth for:

- general Reviewer Core, profiles, report/developer-fix/focused-retest contracts;
- Spatial Experience Extension PR #1;
- Digital Twin Trust Review PR #2;
- current release/version/fixtures/tests;
- consumer Project PM invocation and exact candidate requirements;
- central capability and Parent PM Gateway readiness.

This plan does not modify or relabel PR #1/#2, consumer products or historical reports.

## 3. Role and sandbox policy

```text
REVIEW_PROFILE=Sol/xhigh
SANDBOX=read-only
SILENT_FALLBACK=FORBIDDEN
CONTRACT_LABEL_strongest=FORBIDDEN
CONSUMER_PRODUCT_MUTATION=NO
LOCAL_DEPLOYMENT=NO
HUMAN_OWNER_PRODUCT_VERDICT=NO
```

Sol/xhigh availability must be discovered before execution. If unavailable, return a blocker rather than substitute another model/profile.

## 4. Allowed R1 inputs

- public/source code and repository docs;
- exact candidate/PR/SHA metadata;
- sanitized evidence manifests;
- synthetic D0/D1 fixtures;
- redacted screenshots and product observations;
- artifact/runtime hashes and normalized receipts;
- consumer Project Profile and review request.

## 5. Forbidden R1 inputs/actions

- consumer product source edits;
- deployment/start/stop of product Runtime unless performed by a separate authorized tool/worker outside the Reviewer Harness session;
- full D2/D3 or production PII content in ordinary prompts/evidence;
- unredacted credentials/cookies/private files;
- using App Server event simulation as real product interaction;
- claiming trusted keyboard/device behavior from synthetic dispatch;
- replacing or rewriting historical review reports;
- merge/release or Human Owner decisions.

## 6. Evidence-layer boundary

The adapter must classify evidence as:

```text
PLANNING
SOURCE_STATIC
TEST_BUILD
LOCAL_RUNTIME
PRODUCT_EXPERIENCE
HUMAN_OWNER
MERGE_RELEASE
```

The Harness can directly support the first three layers and index evidence from higher layers. It cannot create a higher-layer PASS merely by reading or summarizing a receipt.

Required invariants:

```text
HARNESS_SOURCE_REVIEW_PASS != PRODUCT_RUNTIME_PASS
APP_SERVER_EVENT != REAL_BROWSER_OR_APP_INTERACTION
SYNTHETIC_KEY_EVENT != TRUSTED_NATIVE_KEYBOARD
REVIEWER_PASS != HUMAN_OWNER_PASS
```

## 7. Activation prerequisites

- [ ] live PR #1/#2 and current Reviewer Core truth restored;
- [ ] explicit transition or non-conflicting successor Goal;
- [ ] central capability/Gateway/Binary/Protocol Lock accepted for Pilot;
- [ ] exact Sol/xhigh profile available;
- [ ] opt-in consumer review request with complete candidate identity;
- [ ] repository-local GOAL/TASK/PLAN/RESULT/EVIDENCE/commands.log;
- [ ] read-only path/network/data policy;
- [ ] redaction and no-consumer-mutation proof;
- [ ] real product-operation tool/worker identified when required.

Until then：`REVIEWER_HARNESS_STATE=QUEUED`.

## 8. Milestones

### RH0 — Current truth and profile mapping

Restore Reviewer Core/PR #1/#2/fixtures/release truth. Map the central Task Envelope and Model Profile to existing Review Request/Profile contracts without weakening exact candidate or evidence requirements.

### RH1 — Read-only Harness Review Envelope

Implement/validate:

- exact repository/project/goal/branch/candidate SHA;
- artifact/runtime/test-data identity;
- review mode/scope/protected evidence;
- model `Sol/xhigh`;
- read-only sandbox;
- no network unless exact local product/evidence endpoint;
- claim ceiling and next authority.

Incomplete identity fails closed.

### RH2 — Evidence index and identity reconciliation

Use synthetic/previous public-safe fixtures to prove:

- mixed SHA evidence rejected;
- predecessor evidence rejected for successor claims;
- source/static receipt not promoted to Runtime;
- missing artifact/runtime/test-data identity blocks corresponding claims;
- hashes and file indexes are deterministic;
- redaction removes private content.

### RH3 — Findings-draft support

The Harness may produce a draft finding with:

- issue ID/severity;
- expected/actual;
- source/evidence references;
- reproducibility;
- candidate identity;
- claim layer;
- proposed focused retest scope.

A human/independent reviewer or authorized product-operation tool must confirm actual product observations. Draft findings are not automatically accepted.

### RH4 — Real product-operation boundary trial

Run at least one trial where:

- Harness indexes source/evidence and prepares review scope;
- real browser/App/device tools perform the product journey;
- observations/screenshots are added separately;
- Harness does not claim operation it did not perform;
- final report distinguishes source analysis, tool observations and reviewer judgment.

### RH5 — Multi-product cold-start and Human Owner Reviewer Gate

Trial on at least:

- KnowMe;
- one of Lingxi/AOG/Copilot;
- a negative fixture with incomplete identity or prohibited data.

Required:

- no consumer product mutation;
- Sol/xhigh exact profile;
- independent review semantics preserved;
- rollback/uninstall;
- Human Owner Reviewer Extension decision.

## 9. Required blockers

- incomplete candidate/artifact/runtime/test-data identity;
- mixed or stale evidence;
- source/test evidence presented as Runtime/Product PASS;
- synthetic event presented as real product interaction;
- D2/D3/PII content without review-data Gate;
- consumer source mutation attempt;
- non-read-only sandbox;
- Sol/xhigh unavailable or silent fallback;
- Reviewer presented as Product PM or Human Owner;
- product operation required but no real tool/worker evidence exists.

## 10. Required evidence

- central/Gateway/Binary/Schema/Model pins;
- Reviewer source/final SHA;
- Review Request/Task Envelope hashes;
- candidate/artifact/runtime/test-data identities;
- evidence layer/index hashes;
- redaction scan;
- no-consumer-mutation proof;
- real product-operation references where required;
- findings draft and final human/independent disposition separation;
- process terminal state, blocker, claim ceiling and next authority.

## 11. Claim ceiling

```text
PLANNING_ONLY
CURRENT_REVIEWER_PR1_PR2_GATE_CHANGE=NO
CODEX_HARNESS_REVIEW_ADAPTER=NOT_STARTED
CONSUMER_PRODUCT_MUTATION=NO
REAL_PRODUCT_OPERATION_PROOF=NO
HUMAN_OWNER_PRODUCT_VERDICT=NO
AUTO_MERGE_RELEASE=NO
REVIEWER_PM_ACTIVATION_REQUIRED
```
