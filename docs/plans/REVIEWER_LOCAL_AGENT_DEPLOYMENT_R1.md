# REVIEWER_LOCAL_AGENT_DEPLOYMENT_R1

> Repository: `zhouzengrui369-commits/product-experience-reviewer-skill`  
> Visibility: `public`  
> Executor: `OWNER_DESIGNATED_LOCAL_AGENT`  
> Program: `ECOSYSTEM-CODEX-HARNESS-R1`  
> State: `QUEUED / PLANNING_ONLY`  
> Owner: Product Experience Reviewer Skill Project PM

## 1. Goal

Use an Owner-designated local Agent for Reviewer source/fixture/test execution and, under a separate consumer Product PM authority, exact Candidate local deployment support.

```text
Reviewer or consumer Parent PM exact task
→ LocalAgentDeploymentRequest
→ fresh local checkout/worktree/task/evidence roots
→ selected local Agent
→ technical LocalAgentExecutionReceipt
→ real browser/App/device tools where required
→ independent reviewer judgment
```

No Self-hosted Runner is registered for this public repository.

## 2. Protected lanes

Read live before activation:

- Reviewer Core/release/profiles;
- Spatial PR #1;
- Digital Twin Trust PR #2;
- Harness PR #4 / Issue #5;
- report/developer-fix/focused-retest contracts;
- consumer Project PM ownership;
- historical reports/evidence.

## 3. Role boundary

### Local Agent may

- run Reviewer schema/unit/fixture tests;
- build a Reviewer test artifact;
- reconcile candidate/evidence identities;
- prepare read-only evidence indexes/draft findings;
- deploy/launch an exact consumer Candidate only through that Product PM's separate deployment request;
- return sanitized technical receipts.

### Local Agent may not

- claim browser/App/device interaction it did not perform;
- claim trusted keyboard from synthetic events;
- mutate consumer product source during deployment;
- decide Product Experience or Human Owner PASS;
- merge/release consumer products.

## 4. Agent policy

Default Reviewer analysis:

```text
MODEL=Sol/xhigh
SANDBOX=read-only
SILENT_FALLBACK=FORBIDDEN
```

A product deployment support task may use an explicitly selected deployment Agent. If Codex is selected for deployment, use Luna/xhigh; independent product experience still uses Sol/xhigh.

Default deployment:

```text
SOURCE_MUTATION=NO
LOCAL_REPAIR=NO
PUSH=NO
MERGE=NO
CONSUMER_MUTATION=NO
```

## 5. Activation prerequisites

- [ ] live Reviewer Core/PR #1/#2/#4 truth restored;
- [ ] explicit transition/non-conflicting Goal;
- [ ] repository visibility freshly verified public;
- [ ] repository-local GOAL/TASK/PLAN/RESULT/EVIDENCE/commands.log;
- [ ] exact Reviewer task or complete consumer Candidate deployment request;
- [ ] pinned LocalAgentProfile;
- [ ] complete candidate/artifact/runtime/test-data identity;
- [ ] real product tool identified when product operation is claimed;
- [ ] redaction and zero consumer mutation;
- [ ] rollback.

## 6. Milestones

### RLA0 — Current truth and task type

Restore Core/extensions/contracts and classify the task as Reviewer test or consumer Candidate deployment support.

### RLA1 — Reviewer source/fixture Gate

Fresh exact-SHA checkout, synthetic fixtures, identity/claim/redaction negatives, no consumer mutation and terminal receipt.

### RLA2 — Candidate deployment receipt mapping

For a Product PM-frozen Candidate, create a separate exact deployment task with fresh App/Runtime identity and deployment/health receipt only.

### RLA3 — Real product-tool boundary trial

Real browser/App/device tools perform the journey. Final report distinguishes:

- Local Agent deployment evidence;
- tool observations/screenshots;
- reviewer judgment.

### RLA4 — Failure handback and rollback

Agent returns first blocker. Web Parent PM creates GitHub successor. No local repair or source mutation.

### RLA5 — Multi-product cold-start and Owner Reviewer Gate

Trial KnowMe, one of Copilot/Lingxi/AOG and a mixed/incomplete identity negative fixture. Require no consumer mutation and Human Owner Reviewer Extension decision.

## 7. Evidence invariants

```text
LOCAL_AGENT_EVENT != REAL_PRODUCT_INTERACTION
SYNTHETIC_KEY != TRUSTED_NATIVE_KEYBOARD
LOCAL_AGENT_DEPLOYMENT_PASS != PRODUCT_EXPERIENCE_PASS
REVIEWER_PASS != HUMAN_OWNER_PASS
```

## 8. Evidence receipt

Required:

- visibility/request/profile hashes;
- Reviewer or consumer source SHA/tree;
- Agent identity/version/model/profile;
- artifact/runtime/test-data identity;
- fresh checkout/task/evidence IDs;
- commands/tests/deployment receipt;
- real tool observation references when required;
- redaction/no-mutation/process/source pre/post state;
- first blocker, claim layer and next authority.

## 9. Claim ceiling

```text
PLANNING_ONLY
SELF_HOSTED_RUNNER=FORBIDDEN_FOR_THIS_REPOSITORY
CURRENT_REVIEWER_PR1_PR2_GATE_CHANGE=NO
LOCAL_AGENT_DEPLOYMENT=NOT_STARTED
CONSUMER_PRODUCT_MUTATION=NO
REAL_PRODUCT_OPERATION_PROOF=NO
PRODUCT_EXPERIENCE_PASS=NO
HUMAN_OWNER_PRODUCT_VERDICT=NO
AUTO_MERGE_RELEASE=NO
REVIEWER_PM_ACTIVATION_REQUIRED
```

## 10. First takeover output

```text
REVIEWER_LOCAL_AGENT_TAKEOVER_COMPLETE
CURRENT_REVIEWER_CORE_SHA=
CURRENT_PR1_SHA=
CURRENT_PR2_SHA=
REPOSITORY_VISIBILITY=public
EXECUTOR=LOCAL_AGENT
LOCAL_AGENT_PROFILE=
FIRST_USE_CASE=
FROZEN_PRODUCT_CANDIDATE=
LOCAL_AGENT_DEPLOYMENT_RECEIPT=
REAL_PRODUCT_TOOL_REQUIRED=YES
CONSUMER_MUTATION=NO
LOCAL_AGENT_STATE=QUEUED|ACTIVATED|BLOCKED
CURRENT_FIRST_BLOCKER=
NEXT_AUTHORITY=
HUMAN_OWNER_PRODUCT_VERDICT=NO
```
