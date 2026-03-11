import streamlit as st

from core.src.core.pipelines.phase4_preference_matching import identify_preferred_careers

st.header("Work Preference Matching")
st.write("Phase 4 scaffold page.")
mock_scores = [("Data Analyst", 0.77), ("Teacher", 0.52), ("Mechanical Technician", 0.31)]
st.write("Preferred careers (threshold 0.5):")
st.json(identify_preferred_careers(mock_scores, threshold=0.5))
