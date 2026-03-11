import streamlit as st

from core.src.core.pipelines.phase3_ability_matching import compute_cognitive_scores

st.header("Cognitive Ability Matching")
st.write("Enter sample cognitive scores to preview normalized output.")
raw = st.text_input("Format: reasoning=12,memory=8,attention=10")

if st.button("Compute normalized scores"):
    pairs = [item.strip() for item in raw.split(",") if item.strip()]
    responses = {k.strip(): float(v.strip()) for k, v in (p.split("=") for p in pairs)}
    st.json(compute_cognitive_scores(responses))
