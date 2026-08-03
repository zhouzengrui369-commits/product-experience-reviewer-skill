# DECISIONS

## D-001 — Ship a generic, project-agnostic Skill

Date: 2026-08-03
Status: `ACCEPTED`

The Skill is **not** Copilot-specific. It consumes a project's
`PRODUCT_EXPERIENCE_PROFILE.md` (Copilot, Lingxi, AOG, or any future
KnowMe-ecosystem product). The Core copy and Overlay are project-agnostic.
Decision recorded to prevent accidental drift into a Copilot-only Skill.

## D-002 — Overlay is strictly additive

Date: 2026-08-03
Status: `ACCEPTED`

`AI_PRODUCT_TASTE_OVERLAY.md` is positioned as **additive** to the Core.
The Overlay file explicitly disclaims overriding the Core. The validator
asserts that wording is present.

## D-003 — Validator must be stdlib-only Python 3

Date: 2026-08-03
Status: `ACCEPTED`

`scripts/validate_skill.py` uses Python 3 standard library only. No
third-party dependencies. This decision maximizes portability and keeps
the validator trivially auditable.

## D-004 — Skill author is read-only with respect to the Core copy

Date: 2026-08-03
Status: `ACCEPTED`

The validator hashes the Skill's Core copy at runtime and refuses to
treat reports that pin a different SHA as PASS. There is no codepath
that rewrites the Core copy in place.

## D-005 — Build root may be outside any project repo

Date: 2026-08-03
Status: `ACCEPTED`

The Skill is built in an isolated temporary directory, outside the source
product repository and outside the active personal skills directory. This
avoids accidental product edits or partial installation. Installation is a
separate explicit action.

## D-006 — Worker self-report is not acceptance

Date: 2026-08-03
Status: `ACCEPTED`

Mirrors Core §21 and §17. The worker's task-level receipts
(`RESULT.md` / `EVIDENCE.md` / `commands.log` / `changed-files.txt`)
are not acceptance. Acceptance requires an independent re-run on a
host with `python3` + `shasum` + `node` access, plus a human owner
review of the Core mirror SHA.

## D-007 — Skill is fail-safe on missing receipts

Date: 2026-08-03
Status: `ACCEPTED`

The primary worker could not execute verification commands, so it correctly
returned `BLOCKED`. The controller then ran the smallest permitted fallback,
fixed only validation defects, and upgraded the project to `PASS` after
capturing structure, hash, positive-fixture, and negative-fixture receipts.

— end of DECISIONS —
