# CODEX_HARNESS_REVIEW_ADAPTER_R1

> Repository: `zhouzengrui369-commits/product-experience-reviewer-skill`  
> Visibility: `public`  
> Program: `ECOSYSTEM-CODEX-HARNESS-R1`  
> State: `QUEUED / PLANNING_ONLY`  
> Owner: Product Experience Reviewer Skill Project PM  
> Local deployment plan: [`REVIEWER_LOCAL_AGENT_DEPLOYMENT_R1.md`](./REVIEWER_LOCAL_AGENT_DEPLOYMENT_R1.md)

## 1. Purpose

Use Codex Harness as opt-in read-only support for source/static review, exact Candidate identity reconciliation, evidence indexing and findings drafts.

Because this repository is public, source/test/deployment support uses an Owner-designated Local Agent. No Self-hosted Runner may be registered here.

## 2. Three-layer boundary

```text
Local Agent
  = Reviewer source/test execution or Product PM-authorized Candidate deployment support

Codex Harness
  = Sol/xhigh read-only source/evidence analysis, or Luna/xhigh deployment task when explicitly selected

Real product tools
  = actual browser/App/device journey
```

Neither Local Agent nor Harness may claim product interaction it did not perform.

## 3. Protected lanes

Read live before activation:

- Reviewer Core/release/profiles;
- Spatial PR #1;
- Digital Twin Trust PR #2;
- planning PR #4 and Local Agent tracker;
- consumer Parent PM ownership;
- historical reports/evidence.

## 4. Policy

```text
DEFAULT_REVIEW_MODEL=Sol/xhigh
DEPLOYMENT_IF_CODEX=Luna/xhigh
SANDBOX=read-only
SILENT_FALLBACK=FORBIDDEN
SOURCE_MUTATION_DURING_DEPLOYMENT=NO
CONSUMER_MUTATION=NO
D2_D3_PUBLIC_EVIDENCE=NO
```

## 5. Allowed

- Reviewer schema/unit/fixture tests;
- exact Candidate/evidence identity reconciliation;
- sanitized evidence indexing;
- draft findings/checklists;
- separately authorized Candidate deployment/launch support;
- technical receipts.

## 6. Forbidden

- Self-hosted Runner registration;
- consumer source mutation;
- synthetic event as real product interaction;
- synthetic key as trusted native keyboard;
- deployment PASS as Product Experience PASS;
- Reviewer PASS as Human Owner PASS;
- D2/D3 public evidence;
- merge/release.

## 7. Milestones

```text
RH0 current truth/profile
RH1 read-only review envelope
RH2 evidence identity/index
RH3 findings draft
RH4 Local Agent/real-product boundary trial
RH5 multi-product cold-start/Owner Reviewer Gate
```

Failure returns terminal evidence to Web ChatGPT Parent PM; no local repair.

## 8. Claim ceiling

```text
PLANNING_ONLY
SELF_HOSTED_RUNNER=FORBIDDEN
CURRENT_REVIEWER_PR1_PR2_GATE_CHANGE=NO
LOCAL_AGENT_DEPLOYMENT=NOT_STARTED
CODEX_HARNESS_REVIEW_ADAPTER=NOT_STARTED
CONSUMER_PRODUCT_MUTATION=NO
REAL_PRODUCT_OPERATION_PROOF=NO
PRODUCT_EXPERIENCE_PASS=NO
HUMAN_OWNER_PRODUCT_VERDICT=NO
AUTO_MERGE_RELEASE=NO
REVIEWER_PM_ACTIVATION_REQUIRED
```
