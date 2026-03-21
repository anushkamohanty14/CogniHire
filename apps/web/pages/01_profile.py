import streamlit as st

from core.src.core.pipelines.phase2_user_input import (
    collect_interest_tags,
    collect_manual_skills,
    create_user_profile,
    load_job_titles_from_onet,
    suggest_jobs_from_interest_tags,
    upload_resume,
)

st.header("User Profile")
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
    profile["phase1_job_suggestions"] = suggest_jobs_from_interest_tags(
        profile["interest_tags"],
        load_job_titles_from_onet(),
    )
    st.success("Profile payload created")
    st.json(profile)

if resume is not None and user_id.strip():
    result = upload_resume(resume.name, resume.read(), user_id.strip())
    st.info("Resume uploaded")
    st.json(result)
