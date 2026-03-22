import streamlit as st

from core.src.core.pipelines.phase2_user_input import (
    collect_interest_tags,
    collect_manual_skills,
    create_user_profile,
    load_job_titles_from_onet,
    merge_resume_skills,
    suggest_jobs_from_interest_tags,
    upload_resume,
)
from core.src.core.pipelines.phase5_resume_processing import process_resume

st.header("User Profile")

user_id     = st.text_input("User ID")
skills_raw  = st.text_area("Manual skills (comma separated)")
tags_raw    = st.text_area("Interest tags (comma separated)")
resume_file = st.file_uploader("Upload resume", type=["pdf", "txt", "doc", "docx"])

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
    st.success("Profile created")
    st.json(profile)

if resume_file is not None and user_id.strip():
    meta = upload_resume(resume_file.name, resume_file.read(), user_id.strip())
    st.info(f"Resume saved — {meta['size_bytes']:,} bytes")

    with st.spinner("Extracting skills…"):
        result = process_resume(meta["saved_path"])

    if result.method == "error":
        st.warning(f"Skill extraction failed: {result.error}")
    else:
        method_label = "AI (Claude)" if result.method == "llm" else "Rule-based"
        st.success(f"Extracted {len(result.skills)} skills via {method_label}")

        if result.skills:
            st.markdown("**Extracted skills:**")
            st.write(", ".join(result.skills))
            merge_resume_skills(user_id.strip(), result.skills)
