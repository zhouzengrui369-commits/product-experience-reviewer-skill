# Spatial Runtime Review Checklist

Bind every item to candidate identity, reproducible steps and screenshot/log evidence.

## Identity

- [ ] exact product repository / branch / SHA
- [ ] runtime URL/package/device
- [ ] capability lock + authority SHA/schema hash if applicable

## Core journeys

- [ ] direct spatial entry/deep link
- [ ] scope/drilldown and return path
- [ ] select one real object and inspect its evidence/trust state
- [ ] candidate vs verified route/resource distinction
- [ ] reset/recovery path

## Real browser/device

- [ ] desktop agreed viewport
- [ ] 390x844 when mobile-responsive scope applies
- [ ] keyboard/focus route
- [ ] blocking console/page errors = 0 outside intentional fault injection
- [ ] WebGL/renderer actually active when 3D is claimed

## Failure/recovery

- [ ] geometry/GeoJSON failure
- [ ] tile/network failure where applicable
- [ ] WebGL unavailable or renderer initialization failure
- [ ] fallback preserves core task/truth
- [ ] online recovery does not silently change source/trust semantics

## Truth/provenance

- [ ] source ID/reference visible or reachable
- [ ] source snapshot vs generated/reviewed/observed times remain distinguishable
- [ ] confidence/review status survives rendering
- [ ] unverified/missing/fixture never looks equivalent to verified
- [ ] animation does not imply execution or availability

## Privacy

- [ ] exact/coarse/region-only/hidden behavior matches permission contract
- [ ] screenshots/logs redact sensitive coordinates when publication scope requires it

## Performance

- [ ] required pan/zoom/drilldown journey remains responsive
- [ ] repeated drilldown/back does not produce unbounded memory/resource growth

## Verdict rule

Any P0/safety blocker dominates average visual score. Output Human Owner signal according to the universal Core; never self-authorize release.
