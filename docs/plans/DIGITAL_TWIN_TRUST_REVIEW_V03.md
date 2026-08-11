# Digital Twin Trust & Decision Experience Review v0.3 Plan

> **Plan ID**: `DIGITAL-TWIN-TRUST-REVIEW-V03-R1`  
> **State**: `QUEUED / PLANNING_ONLY`  
> **Execution owner**: Product Experience Reviewer Skill Project PM  
> **Ecosystem authority**: `zhouzengrui369-commits/knowme-ecosystem@e46c4be501c465884486a4417adca2e158a58ccc`  
> **Ecosystem PR**: `knowme-ecosystem#17`  
> **Date**: 2026-08-11

---

## 1. Purpose

Add an opt-in, read-only **Digital Twin Trust & Decision Experience** extension for products that collect, infer, retrieve or act on personal knowledge.

The extension evaluates whether the product is not only technically correct, but also understandable, correctable, appropriately proactive, privacy-preserving and genuinely useful for decisions.

A digital-twin product fails experience review when it feels like surveillance, silently turns inferences into identity, hides data use, loses decision context, exaggerates autonomy or makes deletion/revocation difficult—even when its APIs and models work as designed.

---

## 2. Protected current truth

Before activation, the Reviewer Project PM must independently read:

- repository skill/governance entry and current release/status;
- open Spatial Experience Extension Draft PR #1 and its exact scope/tests;
- existing 21-part general Product Experience Reviewer baseline;
- current read-only/reviewer independence contracts;
- any newer merged or successor review extension.

Hard protection:

- this plan does not change or relabel Spatial Review PR #1;
- Geo/spatial review remains an independent optional extension;
- reviewer remains read-only and does not become product Project PM, implement fixes, deploy, merge, release or issue the Human Owner decision;
- no private real-user data is copied into the reviewer repository or public evidence;
- migration remains `QUEUED` until the Reviewer PM records an explicit transition from current extension work.

---

## 3. Invocation contract

The Digital Twin Trust extension is invoked by a consumer Project PM only after that PM freezes a reproducible product candidate and supplies:

```yaml
review_request:
  repository: owner/name
  project: string
  project_pm: role
  exact_source_sha: full-sha
  exact_candidate_or_runtime_id: string
  ecosystem_baseline_sha: full-sha
  shared_contract_version: optional
  claimed_features: []
  claimed_data_sources: []
  privacy_classes: [D0, D1]
  execution_ceiling: E0-E2
  real_vs_synthetic_data: string
  routes_or_entry_points: []
  evidence_manifest: ref
  protected_predecessor_evidence: []
  explicit_non_claims: []
```

The reviewer must fail closed when exact product/candidate/route identity is missing for a claimed real experience.

---

## 4. Review principles

### 4.1 Helpful, not surveillant

The product must communicate why data collection and proactive behavior benefit the user. Background operation without visible controls, purpose or recent-activity history is a product blocker even if legally consented.

### 4.2 Inspectable belief

The user can distinguish:

- explicit user statement;
- device observation;
- external fact;
- system inference;
- temporary hypothesis;
- expired or disputed knowledge.

The product exposes source, time, confidence and review state at the point of consequence, not only in a developer log.

### 4.3 Correctable identity

The user can correct, dispute, supersede, delete or scope a personal-model claim. A correction must propagate truthfully across cards, search, graph, dialogue, recommendations and future context.

### 4.4 Proactive value must exceed interruption cost

A proactive suggestion must make “why now” understandable, respect quiet/fatigue rules and offer direct feedback such as wrong context, too sensitive or too frequent.

### 4.5 Decision continuity

The journey must preserve:

```text
question/trigger
→ context
→ evidence
→ options and risk
→ recommendation
→ action or draft
→ result
→ feedback/reflection
```

Opening evidence, switching views, going back or relaunching must not silently lose or fork the decision state.

### 4.6 Permission and execution truth

Users understand the difference between:

- collecting;
- retrieving;
- cloud/model processing;
- Agent reading;
- Agent writing;
- drafting;
- executing;
- irreversible action.

A product must not imply autonomy above its accepted E0–E5 level.

---

## 5. Review dimensions

### DT-TRUST-01 — Product purpose and user control

Inspect:

- whether the user understands what the digital twin is for;
- what is currently connected/collected;
- visible pause-all and emergency lock;
- granular authorization and processing location;
- ability to use partial authorization;
- no coercive consent or hidden feature degradation unrelated to the denied permission.

P0 examples:

- no way to stop collection/Agent access;
- broad permission silently enables cloud/write/execution;
- sensitive data appears after permission was revoked.

### DT-TRUST-02 — Fact, observation and inference semantics

Inspect:

- labels and visual hierarchy;
- source/time/confidence;
- review/proposed/disputed/expired status;
- wording avoids treating inference as identity fact;
- high-impact decisions revalidate uncertain assumptions.

P0 examples:

- system-generated relationship/value/health claim shown as confirmed fact;
- decision recommendation relies on disputed/expired data without disclosure.

### DT-TRUST-03 — Provenance and evidence navigation

Inspect:

- answer/card/graph/recommendation links to sources;
- source opens at the relevant section/time;
- returning preserves state;
- missing/unknown information is explicit;
- model-generated narrative is separable from source facts.

P1/P2 examples:

- citation exists but cannot be opened;
- source route loses the decision journey;
- visually authoritative summary has weak or stale evidence.

### DT-TRUST-04 — Correction, dispute and forgetting

Inspect:

- editing/correction workflow;
- conflict and supersession visibility;
- delete/forget scope and lifecycle status;
- propagation across projections;
- retained audit/tombstone does not expose deleted content;
- failure is truthful and retry/recovery is clear.

P0 examples:

- UI says deleted while graph/vector/recommendation still exposes content;
- correction changes a card but dialogue/proactive engine still uses old value.

### DT-TRUST-05 — Proactive timing and interruption

Inspect:

- why-now explanation;
- current context freshness;
- goal relevance;
- public/private display context;
- frequency, quiet, snooze and dismiss controls;
- no repeated nagging after rejection;
- useful feedback options and behavior change.

P0/P1 examples:

- private relationship/health/work detail shown on a public lock screen;
- high-risk recommendation triggered by a low-confidence inferred activity;
- repeated suggestion after user chose too sensitive/stop.

### DT-TRUST-06 — Decision quality and uncertainty

Inspect:

- options and trade-offs;
- goals/constraints used;
- risks and confidence;
- recommendation rationale;
- what could change the answer;
- preparation/draft vs execution distinction;
- outcome and later reflection.

P1 examples:

- only one option presented as inevitable;
- confidence is always high or lacks rationale;
- personal preference overrides safety/legal/financial evidence without warning.

### DT-TRUST-07 — Action authority and recovery

Inspect:

- E0–E5 level is visible in behavior;
- preview and confirmation where required;
- target/amount/time/recipient binding;
- reversibility/undo;
- full exit/relaunch and receipt durability;
- failure/partial state does not appear as success;
- standing approval is inspectable and revocable.

P0 examples:

- consequential action executes from a suggestion without transaction confirmation;
- failed/partial action displays success and updates knowledge as completed.

### DT-TRUST-08 — Agent and model transparency

Inspect:

- which Agent/model/provider was used;
- what knowledge scope/context was supplied;
- local vs cloud truth and no silent fallback;
- read vs write scope;
- write proposal/review/rollback;
- recent access receipts understandable to the user.

P0 examples:

- D3/private content sent to cloud without valid explicit authority;
- an external Agent can read unfiltered physical database tables.

### DT-TRUST-09 — 2D/3D/Wiki/search/dialogue identity parity

Inspect:

- stable object ID and consistent title/type/status;
- source/review/privacy state consistent across views;
- 3D relation meaning and uncertainty;
- no visual distance/size/color presented as causal certainty;
- return path to card/source;
- changes/deletion propagate.

P1/P2 examples:

- 3D node exists but cannot be inspected/corrected;
- graph shows a relationship hidden from the card's privacy scope;
- same concept forks into incompatible identities.

### DT-TRUST-10 — Accessibility, mobile and degraded modes

Inspect:

- keyboard/focus/screen-reader path;
- 2D/list fallback for 3D/WebGL;
- mobile viewport and touch targets;
- performance and reduced-motion behavior;
- offline/shared-engine unavailable state;
- important controls do not require hover/precise pointer.

P1 examples:

- user cannot revoke permission or inspect evidence via keyboard/mobile;
- 3D is the only access path to a relationship.

### DT-TRUST-11 — Third-party privacy and social context

Inspect:

- relationship/contact/communication minimization;
- another person's private information not treated as the user's unrestricted property;
- share/export/public display boundary;
- organization/work vs personal namespace;
- public-context redaction.

P0 examples:

- private third-party communications used in a public presentation or recommendation without a scoped decision;
- enterprise/AOG data silently trains/updates personal relationship/value models.

### DT-TRUST-12 — Long-term learning and identity drift

Inspect:

- repeated behavior vs explicit preference;
- one-off edits do not become permanent rules;
- model changes and rationale are visible;
- stale information is down-ranked/revalidated;
- feedback such as rejection is interpreted carefully;
- user can reset a domain/model.

P1 examples:

- past role or preference permanently dominates current decisions;
- rejecting one recommendation is stored as a broad permanent value judgment.

---

## 6. Product-specific profiles

### KnowMe profile

Mandatory dimensions: all DT-TRUST-01 through 12.

Additional journeys:

- 2D Knowledge Card → source → correction → dialogue uses correction;
- passive decision journey;
- one proactive why-now journey;
- permission pause/revoke/emergency lock;
- full quit/relaunch and outcome persistence;
- 3D only when claimed.

### Copilot profile

Focus:

- source/import/review/search/Wiki/graph continuity;
- Agent/model access transparency;
- backup/export/delete/restore;
- local/cloud truth;
- physical-schema bypass negative test.

Copilot is not penalized for lacking KnowMe proactive behavior unless it claims it.

### Lingxi Presentation profile

Focus:

- source/design-language evidence;
- explicit vs inferred style;
- excluded/deleted source propagation;
- local/cloud/provider clarity;
- real import and HTML/PPTX/PDF output;
- sensitive knowledge at presentation/public-display boundaries.

### AOG profile

Focus:

- confirmed source/import fidelity/review semantics;
- PII and organization/personal isolation;
- domain recommendation authority;
- production-data truth;
- optional KnowMe influence transparency.

### ebook profile

Focus:

- explicit capture and content-license boundaries;
- spoiler/source correctness;
- reading history privacy;
- grounded QA;
- optional insight contribution to KnowMe;
- mobile/offline behavior.

---

## 7. Evidence hierarchy

### Strong evidence

- exact native/mobile/browser candidate and Runtime identity;
- real interaction with approved data/content;
- OS/device permission state;
- full process exit/relaunch;
- network/provider observation;
- durable receipts and artifact hashes;
- inspectable source/correction/deletion propagation;
- target-device accessibility/mobile behavior.

### Supporting evidence only

- unit/integration tests;
- API responses;
- fixtures;
- browser harnesses that replace native/OS behavior;
- static screenshots without route/runtime identity;
- schema validation;
- source/CI PASS.

The reviewer must state what evidence cannot prove.

---

## 8. Severity and verdict

### P0

A critical trust, privacy, execution or truth failure that makes the candidate unsafe or fundamentally deceptive.

### P1

A major journey failure, inaccessible control or high-probability harmful misunderstanding.

### P2

A material experience/trust gap that blocks Human Owner readiness even if core functions work.

### P3

Minor quality/polish issue that does not block the claimed scope.

Verdicts:

```text
PRODUCT_EXPERIENCE_V03_PASS
PRODUCT_EXPERIENCE_V03_PASS_WITH_NOTES
PRODUCT_EXPERIENCE_V03_BLOCKED
PRODUCT_EXPERIENCE_V03_NOT_TESTABLE_<CAUSE>
```

Default release/Owner eligibility rule:

```text
P0=0
P1=0
P2=0 unless Human Owner explicitly accepts named residual risk
exact candidate/runtime identity present
claimed real-device/runtime journeys actually tested
```

Reviewer PASS is necessary evidence, not the Human Owner product-value decision.

---

## 9. Required report structure

1. Candidate/runtime identity and claim ceiling
2. Product profile and tested journeys
3. Data sources/privacy/execution scope
4. Evidence inventory and limitations
5. Findings table: ID/severity/dimension/evidence/impact/reproduction/expected
6. Facts vs inferences/provenance summary
7. Permission/cloud/Agent/action summary
8. Decision continuity and proactive experience summary
9. 2D/3D/accessibility/mobile summary
10. Correction/deletion/long-term learning summary
11. Regression/non-regression scope
12. P0/P1/P2/P3 totals
13. Verdict and exact next owner
14. Immutable receipt reference

---

## 10. Milestone plan

### R0 — Activation and current baseline mapping

- read current skill and Spatial PR #1;
- create Goal/TASK/PLAN/RESULT/EVIDENCE/commands.log;
- pin ecosystem commit and general reviewer version;
- preserve all existing extension fixtures/tests;
- define opt-in trigger and backward compatibility.

### R1 — Review schema and prompt extension

- machine-readable request/report fields;
- dimension applicability logic;
- severity and not-testable behavior;
- claim/evidence ceiling;
- product profiles.

### R2 — Deterministic fixtures

Positive/negative cases for:

- fact vs inference;
- correction propagation;
- false delete success;
- proactive public-context privacy;
- silent cloud fallback;
- Agent physical-schema access;
- 2D/3D identity mismatch;
- inaccessible revoke/quiet control;
- product-specific applicability.

### R3 — Reviewer workflow and tool guidance

- exact-candidate bootstrap;
- browser/native/mobile evidence collection;
- safe screenshot/redaction rules;
- no real D2/D3 in public artifacts;
- source/runtime distinction;
- report and handback protocol.

### R4 — Regression and cold-start trials

- preserve general and spatial reviewer behavior;
- run exact examples against at least KnowMe and one other product candidate/fixture;
- verify reviewer stays read-only and returns findings to Project PM;
- Human Owner accepts reviewer extension release.

---

## 11. Non-goals

The reviewer extension does not:

- design product strategy or prioritize Goals;
- implement or patch source;
- mutate knowledge, permissions or user data;
- run deployment as the product worker;
- accept license/security architecture on behalf of owners;
- merge/release products;
- issue the Human Owner customer-value verdict.

---

## 12. Project PM first action

Return:

```text
REVIEWER_CURRENT_ACTIVE_GOAL=
CURRENT_SKILL_SHA=
SPATIAL_EXTENSION_PR_STATE=
CURRENT_GATE=
CURRENT_BLOCKER=
V03_MIGRATION_STATE=QUEUED|ACTIVATED|BLOCKED
ACTIVATION_PREREQUISITE=
PINNED_ECOSYSTEM_SHA=e46c4be501c465884486a4417adca2e158a58ccc
NEXT_REPOSITORY_LOCAL_GOAL=
BACKWARD_COMPATIBILITY_PLAN=
```

No implementation begins until this snapshot agrees with current repository truth and the reviewer governance lock.
