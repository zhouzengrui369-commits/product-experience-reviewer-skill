# Spatial Experience Extension

Status: OPTIONAL EXTENSION

This extension adds focused review criteria for products that render geospatial/spatial context. It does not change the universal Product Experience Reviewer Core and remains read-only with respect to product code/data/configuration.

## Activate when

A project Profile declares a material spatial user journey: map, globe, location memory, route/incident situation, geographic knowledge coverage, or presentation map output.

## Required review dimensions

1. **Spatial comprehension** — user can understand scope, hierarchy, selected object and next action.
2. **Truth semantics** — visual nodes/edges/colors/animation do not overstate availability, verification or certainty.
3. **Source and time** — material claims expose source/freshness/confidence or a clear path to them.
4. **Navigation** — pan/zoom/drilldown/back/reset are predictable and recoverable.
5. **Accessibility** — keyboard/focus/labels and non-color semantics; critical tasks have a non-pointer path where required.
6. **Responsive behavior** — agreed mobile viewport (default 390x844 when applicable) preserves critical information.
7. **Renderer resilience** — WebGL/tiles/GeoJSON/network failures fail visibly and offer fallback/recovery.
8. **Performance** — no blocking jank/memory growth during required drilldown/route journeys.
9. **Privacy** — personal/sensitive location precision matches the project's permission contract.
10. **Parity** — 2D/3D/native/static variants preserve material truth, even when visual fidelity differs.

## Hard blockers

- verified-looking route without evidence;
- exact sensitive/personal coordinate shown outside authorized precision;
- missing/unverified data rendered as equivalent to verified success;
- mock/fixture path presented as live operational data;
- WebGL/API HTTP success substituted for an actual browser journey;
- static prototype used to raise runtime verdict;
- product cannot recover from a required renderer failure.

## Geo Context reference

For KnowMe ecosystem projects using `geo-context`, reviewers should additionally record:

- central capability authority commit;
- GeoScene schema hash;
- project `CAPABILITY_LOCK.json` identity;
- whether source/trust/privacy fields survive producer -> renderer;
- whether candidate/verified route semantics remain visibly distinct.

Current central candidate reference:

- authority SHA: `6edb5401084de24491038ac55525f584e9943bd7`
- GeoScene schema SHA-256: `8695f3d9d376bf5591138d78b1460c17758845312aeca52a4a0597ee873032df`

## Human Owner boundary

The extension may determine product-experience/release-evidence findings. It never grants Human Owner Gate PASS.
