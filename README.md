# CogniHire (Phase 1 + Phase 2+ Integration)

Current scaffold includes:

- Phase 1: O*NET job ability data usage for lexical job suggestion
- Phase 2: user profile input and normalization
- Phase 3: cognitive scoring and ability similarity
- Phase 4: activity preference matching
- Phase 5: reaction-time measurement (trial timestamps + RT in ms + correctness)
- Phase 6: composite task scoring (accuracy + RT)
- Phase 7: ability score normalization (z-score based scaling to 0–7)

For the current cognitive requirements and phase-by-phase delivery contract, see:

- `docs/cognitive_ability_requirements.md`
- `PROJECT_STRUCTURE_PHASE2_ONWARDS.md`

## Run API

```bash
uvicorn apps.api.src.main:app --reload
