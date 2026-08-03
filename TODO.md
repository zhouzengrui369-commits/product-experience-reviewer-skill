# TODO

## Now

- [x] Run the structure validator and capture exit `0`.
- [x] Verify PASS fixture exits `0` and intentional FAIL fixture exits `2`.
- [x] Verify the source and shipped Core are byte-identical.
- [ ] Publish the standalone repository and tag the initial release when desired.

## Soon

- [ ] Add an `examples/` directory with one rendered focused-retest report and
      one rendered full review report — both synthetic, both pinned to a known
      candidate SHA. The fixtures currently under `fixtures/` are minimal smoke
      tests, not full templates.
- [ ] Add a `--report-only` mode to the validator so the validator can be run
      on a candidate review without re-running the structural checks.
- [ ] Document how to consume `templates/developer-fix-contract.md` from a
      Codex `codex://threads/...` handoff URL (currently only path-based).

## Later

- [ ] Add CI that runs the validator and scans distributable files for private
      absolute paths and obvious secret patterns.
- [ ] When the Core or Overlay bumps to 1.1.x, add a CI check that fails when
      the shipped Skill's Core or Overlay SHA drifts from the ecosystem SSoT.

— end of TODO —
