# Architecture — product-experience-reviewer

This Skill is a **procedural layer** on top of an authoritative document
(Core) and a small, additive taste overlay. It does not introduce any
runtime services, network endpoints, or persistent state.

```
┌──────────────────────────────────────────────────────────────────────┐
│                        Skill: product-experience-reviewer            │
│                                                                      │
│   ┌─────────────────────┐                                             │
│   │ SKILL.md (YAML+MD)  │  trigger + workflow + behavior rules       │
│   └──────────┬──────────┘                                             │
│              │ loads on demand                                       │
│              ▼                                                       │
│   ┌─────────────────────────────────────────────────────────────┐    │
│   │ references/                                                 │    │
│   │   PRODUCT_EXPERIENCE_REVIEWER_CORE.md   (authoritative,     │    │
│   │                                          SHA-pinned)        │    │
│   │   AI_PRODUCT_TASTE_OVERLAY.md           (additive overlay)  │    │
│   └─────────────────────────────────────────────────────────────┘    │
│                                                                      │
│   ┌─────────────────────┐                                             │
│   │ templates/           │  per-stage structured documents:          │
│   │                     │   project-profile, blind-brief,            │
│   │                     │   frozen-output, candidate-identity,      │
│   │                     │   full-review, focused-retest,             │
│   │                     │   issue-contract, evidence-manifest,      │
│   │                     │   developer-fix-contract, runtime-journey │
│   └─────────────────────┘                                             │
│                                                                      │
│   ┌─────────────────────┐                                             │
│   │ scripts/             │  read-only validator:                     │
│   │   validate_skill.py  │   parses SKILL.md frontmatter, asserts   │
│   │                     │   file presence, checks Core / Overlay    │
│   │                     │   identity, scans obvious secrets /        │
│   │                     │   private paths, optionally validates a    │
│   │                     │   generated review report                  │
│   └─────────────────────┘                                             │
│                                                                      │
│   ┌─────────────────────┐                                             │
│   │ agents/openai.yaml   │  agent description + default prompt       │
│   └─────────────────────┘                                             │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

## Layering

1. **Trigger layer** — `SKILL.md` description + `agents/openai.yaml` decide
   when the Skill is invoked. No automatic dispatch — the user / dispatcher
   explicitly chooses a review mode.
2. **Method layer** — `references/PRODUCT_EXPERIENCE_REVIEWER_CORE.md` is
   the **single** source of truth for review method, evidence discipline,
   verdicts, and the Human Owner Gate boundary. The Overlay adds taste
   dimensions without overriding the Core.
3. **Template layer** — `templates/*.md` provide the per-stage document
   skeletons the reviewer fills in. They are not part of the Core and are
   free to evolve with the Skill.
4. **Self-test layer** — `scripts/validate_skill.py` is the Skill's own
   gate. PASS only when: structure intact, Core self-identifies, Overlay
   disclaims overriding, no obvious secrets, no private paths in shipped
   Skill files, optional report has all required sections.

## Failure modes

- **Missing trigger context** → Skill returns `BLOCKED` (no mode picked).
- **Reproducibility failure** → `Release Evidence Verdict = BLOCKED_NON_REPRODUCIBLE_CANDIDATE`.
- **Runtime access failure** → `BLOCKED_RUNTIME_ACCESS`.
- **Missing report sections** → validator returns exit code 2.
- **Core SHA mismatch in a report** → validator returns exit code 3.
- **Secret / private-path detection** → validator returns exit code 4.

## Boundaries

- The Skill **never** writes to product code, UI, copy, tests, data, or
  build configuration.
- The Skill **never** publishes or notifies another thread unless the
  user explicitly authorizes it.
- The Skill **never** lets an AI claim a Human Owner Gate pass — output
  is always `HUMAN_OWNER_GATE_REQUIRED` or `HUMAN_OWNER_GATE_NOT_ELIGIBLE`.
- The Skill ships its own Core copy; a project repo's mirror is
  read-only and verified by SHA-256.

— end of architecture —
