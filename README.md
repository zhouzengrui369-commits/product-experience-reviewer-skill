# product-experience-reviewer

[![Validate Skill](https://github.com/zhouzengrui369-commits/product-experience-reviewer-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/zhouzengrui369-commits/product-experience-reviewer-skill/actions/workflows/validate.yml)

An **independent product-experience reviewer** delivered as a Codex
procedural Skill. It judges **what the user actually experiences** in a
real product candidate — not what the code does, not what the README
claims, not what a prototype looks like.

The Skill is **read-only with respect to product code, UI, copy, tests,
data, and build configuration**. It may write its own review reports and
evidence directories only.

The Skill is **not Copilot-specific**. It is a generic procedural layer
that consumes a project's `PRODUCT_EXPERIENCE_PROFILE.md` (Copilot,
Lingxi, AOG, or any future KnowMe-ecosystem product) and applies the
universal Core shipped at
`product-experience-reviewer/references/PRODUCT_EXPERIENCE_REVIEWER_CORE.md`.

---

## Value

- Replaces ad-hoc "did the dev say it's fixed?" checks with an evidence-bound,
  verdict-bound, gate-bound review flow.
- Forces Runtime / Prototype / Parity separation so that a slick prototype
  cannot raise the Runtime verdict.
- Preserves a four-verdict structure (Product Experience / Release
  Evidence / Prototype Concept / Parity) plus a separate Human Owner Gate.
- Ships its own validator so the Skill can be self-tested before being
  installed into `~/.codex/skills/`.

---

## Install

```bash
# 1. Verify the Skill on disk (stdlib-only Python 3).
python3 product-experience-reviewer/scripts/validate_skill.py --root .

# 2. Drop the Skill into your Codex skills root (or a project-local skills dir).
cp -R product-experience-reviewer ~/.codex/skills/

# 3. (Optional) Validate an existing review report.
python3 product-experience-reviewer/scripts/validate_skill.py \
        --root . \
        --report path/to/a-rendered-report.md
```

No global config change. No remote calls. No credentials required.

---

## Invoke

```
$product-experience-reviewer <mode> <candidate> [prior-issues]

modes: FIRST_INSTALL | FULL_EXPERIENCE_REVIEW | EXPLORATORY_PRODUCT_REVIEW
       | FOCUSED_RETEST | RELEASE_CANDIDATE_REVIEW
```

`<candidate>` must include: repo, branch, commit SHA, working-tree status,
App / package / URL, build command, SHA-256 or deployment ID, OS, arch,
device, runtime version, model / provider, network state, configuration
snapshot, prior review reference. Missing fields force
`BLOCKED_NON_REPRODUCIBLE_CANDIDATE`.

---

## Workflow (the Skill does this in order)

1. **Pick the review mode.** `RELEASE_CANDIDATE_REVIEW` only if every
   reproducibility field is present.
2. **Capture candidate identity** (`templates/candidate-identity.md`).
3. **Stage A — isolated experience.** Blind User Reviewer with only user
   identity, candidate entry, one real task, safety boundary
   (`templates/blind-brief.md` / `templates/frozen-output.md`). Freeze
   Stage A **before** reading any product-positioning document. If true
   isolation is impossible, label `PRIMED_COGNITIVE_WALKTHROUGH`.
4. **Stage B — positioning + baseline reconciliation.** Now read the
   project Profile, ecosystem baseline, README / PRD / architecture /
   Release Scope / prior review / candidate RESULT-EVIDENCE-ACCEPTANCE.
5. **Runtime / Prototype / Parity split.** Prototype scores never raise
   the Runtime verdict.
6. **Scope fairness.** Tag every dimension `IN_CURRENT_RELEASE_SCOPE`,
   `OUT_OF_CURRENT_RELEASE_SCOPE`, or `AMBIGUOUS_SCOPE`. N/A never
   normalizes into the score.
7. **Walk Runtime journeys.** Each conclusion binds: reproducible step,
   expected, actual, user feeling, screenshot/log/artifact, candidate
   version, time.
8. **Score 1–5 per dimension.** N/A excluded. P0 trumps average score.
9. **Grade issues P0/P1/P2/P3** using `templates/issue-contract.md`.
10. **Inheritance matrix** for any prior report.
11. **Four independent verdicts** — Product Experience, Release Evidence,
    Prototype Concept, Parity.
12. **Owner Decision Brief** at the top of the report.
13. **Human Owner Gate** — output only `HUMAN_OWNER_GATE_REQUIRED` after
    P0=0. Never "passed" by an AI.

---

## Example (focused retest)

```
$product-experience-reviewer FOCUSED_RETEST
candidate: copilot-app @ 320a4c8d (dirty/untracked)
previous:  reports/product-review/2026-07-28-copilot-focused-retest.md
prior-issues: EXP-COP-008, EXP-COP-009
```

Expected output:

- `reports/product-review/2026-07-29-copilot-focused-retest.md`
- `reports/product-review/2026-07-29-copilot/evidence/` (screenshots,
  logs, frozen Stage A, isolated Blind Reviewer transcript)
- four independent verdicts
- `HUMAN_OWNER_GATE_NOT_ELIGIBLE` until P0=0 AND a fresh independent
  focused retest closes the issue acceptance criteria

The reviewer must not declare release / MVP / gate-pass at any point.

---

## Safety boundaries

- **No writes** outside explicitly authorized first-install acceptance docs or
  `reports/product-review/` evidence paths.
- **No access** to secret stores, credentials, production databases, or private
  user data outside the authorized test scope. Prefer synthetic fixtures; real
  owner-provided material requires explicit approval and publication redaction.
- **No undeclared egress.** Stage A may exercise the candidate's declared
  network path, but must not change provider/network configuration or call
  unrelated services.
- **No modification** of the Core mirror or Profile; Core upgrades go
  through Core §21.4.
- **No publishing or notifying** another thread without explicit user
  authorization.
- **No AI Human Owner Gate PASS.** After P0=0, the Skill outputs only
  `HUMAN_OWNER_GATE_REQUIRED`. The Human Owner Gate is for the human
  Owner, not the AI.

---

## Self-test (run before install)

```bash
python3 product-experience-reviewer/scripts/validate_skill.py --root .

# Should print:
#   core_sha256=<64-hex>
#   PASS
# Exit code 0.

# Validate the PASS fixture:
python3 product-experience-reviewer/scripts/validate_skill.py \
        --root . \
        --report product-experience-reviewer/fixtures/pass-report.md
# Should print: report_ok=... PASS, exit code 0.

# Validate the FAIL fixture (must exit non-zero):
python3 product-experience-reviewer/scripts/validate_skill.py \
        --root . \
        --report product-experience-reviewer/fixtures/fail-report-incomplete.md
# Should print FAIL with exit code 2.
```

The repository is published only after the structure check, Core hash check,
PASS fixture, and intentional FAIL fixture all produce the expected receipts.

---

## License

MIT — see `LICENSE`.
