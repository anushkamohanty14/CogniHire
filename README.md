# CogniHire (Phase 1 + Phase 2 Integration)

This repository now contains a working integration of:

- **Phase 1:** O*NET job ability data loading/cleaning/matrix creation
- **Phase 2:** User profile registration, manual skills/tags collection, and resume upload

## What is integrated

1. API can load O*NET data and list jobs (`/onet/jobs`).
2. Creating a user profile (`/users/profile`) enriches the profile with
   `phase1_job_suggestions` based on lexical matching between `interest_tags`
   and Phase 1 O*NET job titles.
3. Profiles are persisted in local JSON storage (`data/interim/user_profiles.json`).
4. Resume uploads are supported via `/users/resume` and Streamlit UI.

## One-command setup

```bash
./scripts/setup.sh
```

This installs all required packages from `requirements.txt`.

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
python -m unittest discover -s tests -p 'test_*.py' -v
```
