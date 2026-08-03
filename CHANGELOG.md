# CHANGELOG

## 1.0.0 — 2026-08-03

- Initial release of the **product-experience-reviewer** Skill.
- Ships an authoritative copy of `PRODUCT_EXPERIENCE_REVIEWER_CORE` v1.0.0.
- Adds an additive `AI_PRODUCT_TASTE_OVERLAY` v1.0.0 (never overrides Core).
- Bundles templates for project profile, blind brief, frozen output, candidate
  identity, full review, focused retest, issue contract, evidence manifest,
  and developer fix contract.
- Ships a deterministic read-only validator (`scripts/validate_skill.py`,
  Python 3 stdlib only) with PASS / FAIL fixtures.
- Validator verified against structure, PASS fixture, intentional FAIL fixture,
  Core SHA-256 identity, internal paths, and secret/private-path scanning.
- Adds GitHub Actions validation for structure, pinned Core, and positive/negative fixtures.

## Unreleased

- n/a
