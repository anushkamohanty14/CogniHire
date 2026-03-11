import streamlit as st

from core.src.core.pipelines.phase2_user_input import collect_interest_tags, collect_manual_skills, create_user_profile

st.header("User Profile")
user_id = st.text_input("User ID")
skills_raw = st.text_area("Manual skills (comma separated)")
tags_raw = st.text_area("Interest tags (comma separated)")

if st.button("Create profile"):
    profile = create_user_profile(
        user_id=user_id,
        manual_skills=collect_manual_skills(skills_raw),
        interest_tags=collect_interest_tags(tags_raw),
    )
    st.success("Profile payload created")
    st.json(profile)
