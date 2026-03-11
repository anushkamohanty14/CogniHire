# CogniHire (Scaffold)

Initial implementation scaffold started for **Phase 2–4**:

- Phase 2: user profile input and normalization
- Phase 3: cognitive scoring and ability similarity
- Phase 4: activity preference matching

## Run API

```bash
uvicorn apps.api.src.main:app --reload
```

## Run Streamlit

```bash
streamlit run apps/web/app.py
```

## Run tests

```bash
python -m unittest discover -s tests -p 'test_*.py'
```
