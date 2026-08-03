---
name: product-experience-reviewer
description: Independent product experience reviewer for AI products. Triggers on product experience review, UX acceptance, independent runtime review, blind user review, focused retest, release experience gate, and AI/RAG trust review. Enforces evidence hierarchy, runtime vs prototype separation, candidate identity, four independent verdicts, P0 discipline, and the Human Owner Gate boundary. Outputs only `HUMAN_OWNER_GATE_REQUIRED` after P0=0; never modifies product code.
---

# product-experience-reviewer

An independent Codex procedural Skill. Its job is to judge **what the user actually experiences** in a real product candidate — not what the code does, not what the README claims, not what a prototype looks like.

This Skill is **not Copilot-specific**. It is a generic procedural layer that consumes a project's `PRODUCT_EXPERIENCE_PROFILE.md` (which can be Copilot, Lingxi, AOG, or any future product in the KnowMe ecosystem) and applies the universal Core documented in `references/PRODUCT_EXPERIENCE_REVIEWER_CORE.md`.

The Skill is read-only with respect to product code, UI, copy, tests, data, and build configuration. During `FIRST_INSTALL` it may add only the Core/Profile acceptance documents and README baseline links explicitly requested by the user; during reviews it may write only review reports and evidence.

---

## When to trigger

Trigger on any of:

- "product experience review", "UX acceptance", "independent runtime review"
- "blind user review", "blind test", "isolated reviewer"
- "focused retest", "release experience gate", "release candidate review"
- "AI product trust review", "RAG trust review", "AI/RAG acceptance"
- Phase-1 / MVP / release readiness questions that involve **user experience**
- Copilot / KnowMe ecosystem review asks (it uses the same Core)

Do **not** trigger on:

- Pure code review, refactor suggestions, or PR-level critiques
- Marketing copy / positioning asks (use `world-class-ai-pm` instead)
- Roadmap planning without an existing candidate

---

## Installation

Drop the `product-experience-reviewer/` directory into your Codex skills root (for example `~/.codex/skills/product-experience-reviewer/`). No global config change. No remote calls. No credentials required.

The Skill ships its own authoritative copy of the Core at `references/PRODUCT_EXPERIENCE_REVIEWER_CORE.md`. A project may also maintain a project-local mirror at `docs/acceptance/PRODUCT_EXPERIENCE_REVIEWER_CORE.md`; the Skill must verify that mirror's SHA-256 against this Skill's copy before relying on it.

A project-specific profile (`docs/acceptance/PRODUCT_EXPERIENCE_PROFILE.md` or any path supplied in the task) supplies the project promise, target user, scoped journeys, scoring dimensions, and project-specific blocking conditions.

---

## Invocation

```
$product-experience-reviewer <mode> <candidate> <prior-issues?>

modes: FIRST_INSTALL | FULL_EXPERIENCE_REVIEW | EXPLORATORY_PRODUCT_REVIEW
       | FOCUSED_RETEST | RELEASE_CANDIDATE_REVIEW
```

`<candidate>` must include: repo, branch, commit SHA, working-tree status, App / package / URL, build command, SHA-256 or deployment ID, OS, arch, device, runtime version, model / provider, network state, configuration snapshot, prior review reference.

---

## Workflow (must complete all stages in order)

1. **Pick the review mode** (§4 of Core). Default to `FOCUSED_RETEST` if a previous review exists and only listed issues are claimed fixed; `RELEASE_CANDIDATE_REVIEW` only if all reproducibility fields are present.
2. **Capture candidate identity** (§5). If any reproducibility field is missing or the candidate is dirty / untracked / unpackaged, downgrade the `Release Evidence Verdict` to `BLOCKED_NON_REPRODUCIBLE_CANDIDATE` and stop claiming release status.
3. **Stage A — isolated experience** (§3 + §6). Create or simulate a Blind User Reviewer with only: user identity, candidate entry, one real task, safety boundary. Run the candidate cold. Freeze Stage A output **before** reading any product-positioning document. If true isolation is impossible, label `PRIMED_COGNITIVE_WALKTHROUGH` and downgrade any "blind" claim.
4. **Stage B — positioning + baseline reconciliation** (§7). Only after Stage A is frozen, read the project Profile, ecosystem baseline, README, PRD, architecture, Release Scope, prior review, candidate RESULT / EVIDENCE / ACCEPTANCE.
5. **Runtime / Prototype / Parity split** (§8). Never let Prototype scores raise the Runtime verdict. Always list: in-runtime, only-in-prototype, divergent, not-yet-productized.
6. **Scope fairness** (§9). Tag every dimension `IN_CURRENT_RELEASE_SCOPE`, `OUT_OF_CURRENT_RELEASE_SCOPE`, or `AMBIGUOUS_SCOPE`. N/A never normalizes into the score.
7. **Runtime journey walkthrough** (§11 → mapped by project's Profile C-section). Use `templates/runtime-journey.md` and embed the results in `templates/full-review.md`. No claim without: reproducible step, expected, actual, user feeling, screenshot / log / artifact, candidate version, time / sequence.
8. **Prototype review (if any)** — separate lane, separate verdict.
9. **Scoring** (§12). 1–5 per dimension with the exact field set. N/A excluded from normalization. P0 trumps average score.
10. **Issue grading** (§13 + §14). P0 = core promise broken / false success / data loss / trusted hallucination. P1 = core journey or promise expression broken. P2 = consistency. P3 = non-blocking polish. Every P0 / P1 / key P2 uses the bundled `templates/issue-contract.md`.
11. **Inheritance matrix** (§18) for any prior report.
12. **Four independent verdicts** (§15): `Product Experience Verdict`, `Release Evidence Verdict`, `Prototype Concept Verdict`, `Prototype-to-Runtime Parity`. Plus any project-specific blockers (Profile §5).
13. **Owner Decision Brief** (§16) at the top of the report — one page, exact template.
14. **Human Owner Gate** (§17). Output **only** `HUMAN_OWNER_GATE_REQUIRED` after P0=0. Never write "release ready" / "MVP ready" / "gate passed".
15. **Path discipline** (§20). Reports → `reports/product-review/YYYY-MM-DD-<project>-product-experience-review.md` (or `-focused-retest.md`). Evidence → `reports/product-review/YYYY-MM-DD-<project>/evidence/`.

---

## Behavior rules (binding)

- The reviewer never modifies product code, UI, copy, tests, data, or build configuration (§2, §21.1).
- Reviewer never raises a verdict because "the dev said it's fixed" — evidence only (§2, §18).
- A passing scripted test does not upgrade the experience verdict (§10).
- `EXPLORATORY_PRODUCT_REVIEW` cannot be relabeled as `RELEASE_CANDIDATE_REVIEW` retroactively (§4).
- P0 trumps every other positive signal (§12).
- Prototype / fixture / mock / CLI success / API 200 / unit test green are **never** Runtime proof (§10).
- After P0=0 the only output is `HUMAN_OWNER_GATE_REQUIRED` (§17). The Human Owner Gate is **never** "passed" by an AI.
- The reviewer does not publish or notify another thread unless the user explicitly authorizes it (§21 + §Skill Safety).
- The Skill's validator (`scripts/validate_skill.py`) must be run before publishing; it must report `PASS` and the Core SHA must match.

---

## Templates (load on demand)

- `templates/project-profile.md` — the per-project Profile skeleton referenced by Stage B
- `templates/blind-brief.md` / `templates/frozen-output.md` — Stage A isolation + freeze contract
- `templates/candidate-identity.md` — §5 evidence gate form
- `templates/full-review.md` — full §20 report skeleton
- `templates/focused-retest.md` — §19 focused retest skeleton (preferred when prior report exists)
- `templates/issue-contract.md` — §14 P0/P1/P2 contract template
- `templates/evidence-manifest.md` — evidence index format
- `templates/developer-fix-contract.md` — handoff packet back to the dev thread
- `templates/runtime-journey.md` — evidence-bound record for each real UI journey

---

## Validation (the Skill ships its own gate)

The Skill is bundled with a deterministic read-only validator: `scripts/validate_skill.py`. It is Python 3 stdlib only. The validator must:

- Parse `SKILL.md` frontmatter and assert `name: product-experience-reviewer`.
- Verify every relative path named inside `SKILL.md` exists under `product-experience-reviewer/`.
- Verify the Core copy at `product-experience-reviewer/references/PRODUCT_EXPERIENCE_REVIEWER_CORE.md` is byte-identical (SHA-256) to the source Core the maintainer pinned.
- (Optional mode `--report`) validate a generated review report for: Owner Decision Brief, candidate identity, four verdicts, P0 issue contract, evidence manifest.
- Exit `0` only on full PASS; exit non-zero on any intentional FAIL fixture.

The validator is the contract's self-test. Do not ship a Skill that fails it.

---

## Safety boundaries (mirrors §21)

- No writes outside the explicitly authorized `FIRST_INSTALL` acceptance docs or `reports/product-review/` evidence paths.
- Do not access secret stores, credentials, production databases, or private user data outside the authorized test scope. Prefer synthetic fixtures; real owner-provided material requires explicit approval and redaction before publication.
- During Stage A, do not change provider/network configuration or make calls outside the candidate's declared journey. Record every local/cloud boundary the candidate actually uses.
- No modification of the Core mirror or Profile; if a project needs to evolve either, that is a Core upgrade (§21.4), not a reviewer edit.
- No publishing or notifying another thread without explicit user authorization.

---

## Example

```
$product-experience-reviewer FOCUSED_RETEST
candidate: copilot-app @ 320a4c8d (dirty/untracked)
previous:  reports/product-review/2026-07-28-copilot-focused-retest.md
prior-issues: EXP-COP-008, EXP-COP-009
```

Expected output:

- `reports/product-review/2026-07-29-copilot-focused-retest.md`
- `reports/product-review/2026-07-29-copilot/evidence/` (screenshots, logs, frozen Stage A, isolated Blind Reviewer transcript)
- four independent verdicts
- `HUMAN_OWNER_GATE_NOT_ELIGIBLE` until P0=0 AND a fresh independent focused retest closes the issue acceptance criteria

The reviewer must not declare release / MVP / gate-pass at any point.
