import streamlit as st

from core.src.core.pipelines.phase1_onet_data import build_job_ability_matrix, clean_onet_data, load_onet_data
from core.src.core.pipelines.phase2_user_input import (
    collect_interest_tags,
    collect_manual_skills,
    create_user_profile,
    suggest_jobs_from_interest_tags,
    upload_resume,
)

st.header("User Profile (Phase 2)")
user_id = st.text_input("User ID")
skills_raw = st.text_area("Manual skills (comma separated)")
tags_raw = st.text_area("Interest tags (comma separated)")
resume = st.file_uploader("Upload resume", type=["pdf", "txt", "doc", "docx"])

if st.button("Create profile"):
    profile = create_user_profile(
        user_id=user_id,
        manual_skills=collect_manual_skills(skills_raw),
        interest_tags=collect_interest_tags(tags_raw),
    )

    rows = clean_onet_data(load_onet_data())
    job_titles = list(build_job_ability_matrix(rows).keys())
    profile["phase1_job_suggestions"] = suggest_jobs_from_interest_tags(profile["interest_tags"], job_titles)

    st.success("Profile payload created")
    st.json(profile)

if resume is not None and user_id.strip():
    result = upload_resume(resume.name, resume.read(), user_id.strip())
    st.info("Resume uploaded")
    st.json(result)
