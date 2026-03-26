"""Page 0 — CogniHire Dashboard.

Shows readiness ring, top-3 job matches, and skill/ability snapshots
for the logged-in user.
"""
from __future__ import annotations

import streamlit as st

from core.src.core.pipelines.phase7_hybrid_recommendation import HybridRecommender
from core.src.core.storage.mongo_store import MongoUserStore

st.set_page_config(
    page_title="CogniHire — Dashboard",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── CSS ───────────────────────────────────────────────────────────────────────

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

#MainMenu, footer, header { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Inter', sans-serif !important;
    background-color: #f8f9fc !important;
    color: #191c1e !important;
}
.block-container {
    padding-top: 0 !important;
    padding-bottom: 5rem !important;
    max-width: 820px !important;
}

/* topbar */
.db-topbar {
    background: #f8fafc;
    border-bottom: 1px solid rgba(226,232,240,0.5);
    padding: 0 1.5rem;
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: -1rem -1rem 2.5rem -1rem;
}
.db-brand {
    font-size: 1.125rem;
    font-weight: 900;
    letter-spacing: -0.04em;
    color: #00425e;
}
.db-nav-hint {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #40484e;
    opacity: 0.6;
}

/* overline */
.db-overline {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    font-weight: 700;
    color: #40484e;
    opacity: 0.7;
    margin-bottom: 0.4rem;
    display: block;
}

/* section heading */
.db-section-title {
    font-size: 0.6875rem;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    font-weight: 700;
    color: #40484e;
    margin: 2rem 0 1rem;
    display: block;
}

/* card */
.db-card {
    background: #f3f3f7;
    border-radius: 0.25rem;
    padding: 1.25rem 1.5rem;
    margin-bottom: 0.75rem;
}
.db-card-accent {
    border-left: 3px solid #00425e;
}

/* job match card */
.db-job-rank {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #40484e;
    margin-bottom: 0.25rem;
    display: block;
}
.db-job-title {
    font-size: 1rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #191c1e;
    line-height: 1.2;
    margin-bottom: 0.35rem;
}
.db-job-score {
    font-size: 0.8125rem;
    font-weight: 600;
    color: #00425e;
}
.db-job-activities {
    font-size: 0.8rem;
    color: #40484e;
    margin-top: 0.5rem;
    line-height: 1.6;
}

/* stat chip */
.db-chip {
    display: inline-block;
    background: #e1e2e6;
    border-radius: 0.125rem;
    padding: 0.2rem 0.6rem;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #40484e;
    margin-right: 0.4rem;
    margin-bottom: 0.4rem;
}

/* ability mini-bar */
.db-ability-row {
    margin-bottom: 0.6rem;
}

/* CTA button */
.stButton > button {
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
    font-size: 11px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    border: none !important;
    border-radius: 0.25rem !important;
    padding: 0.75rem 1.25rem !important;
    width: 100% !important;
    background-color: #edeef1 !important;
    color: #191c1e !important;
    transition: all 0.12s !important;
}
.stButton > button:hover {
    background-color: #e7e8eb !important;
    transform: scale(0.99) !important;
}
.stButton > button[kind="primary"] {
    background-color: #00425e !important;
    color: #ffffff !important;
}
.stButton > button[kind="primary"]:hover { background-color: #005b7f !important; }

.stTextInput input {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    background: #edeef1 !important;
    border: none !important;
    border-bottom: 2px solid #c0c7ce !important;
    border-radius: 0 !important;
    color: #191c1e !important;
    padding: 0.75rem 1rem !important;
}
.stTextInput label {
    font-family: 'Inter', sans-serif !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.15em !important;
    color: #40484e !important;
}
</style>
""", unsafe_allow_html=True)

# ── Topbar ────────────────────────────────────────────────────────────────────

st.markdown(
    '<div class="db-topbar">'
    '<span class="db-brand">CogniHire</span>'
    '<span class="db-nav-hint">Dashboard</span>'
    '</div>',
    unsafe_allow_html=True,
)

# ── User ID ───────────────────────────────────────────────────────────────────

_, mid, _ = st.columns([1, 4, 1])
with mid:
    uid = st.text_input(
        "User ID",
        value=st.session_state.get("user_id", ""),
        placeholder="Enter your User ID",
        key="dash_uid",
    )

if uid.strip():
    st.session_state["user_id"] = uid.strip()
else:
    st.markdown(
        '<div style="text-align:center; padding:3rem 0;">'
        '<span class="db-overline" style="display:block; text-align:center;">Welcome</span>'
        '<h2 style="font-size:2rem; font-weight:900; letter-spacing:-0.04em; color:#191c1e;'
        '    font-family:Inter,sans-serif; margin-bottom:0.75rem;">Your Career Dashboard</h2>'
        '<p style="color:#40484e; font-family:Inter,sans-serif; font-size:0.9375rem;">'
        'Enter your User ID above to load your profile.</p>'
        '</div>',
        unsafe_allow_html=True,
    )
    st.stop()

user_id = uid.strip()

# ── Load profile ──────────────────────────────────────────────────────────────

store   = MongoUserStore()
profile = store.get_profile(user_id)

if profile is None:
    st.error("No profile found. Complete the Profile page first.")
    st.stop()

ability_percentiles = profile.get("ability_percentiles", {})
readiness           = profile.get("readiness_score")
resume_skills       = profile.get("resume_skills", [])
manual_skills       = profile.get("manual_skills", [])
user_skills         = list(set(resume_skills + manual_skills))
assessed_at         = profile.get("assessed_at", "")

# ── Hero — readiness ring ─────────────────────────────────────────────────────

if readiness is not None:
    readiness_pct  = float(readiness)
    readiness_text = f"{readiness_pct:.0f}"
    if readiness_pct >= 67:
        tier, tier_col = "High Readiness",   "#006a6a"
    elif readiness_pct >= 33:
        tier, tier_col = "Mid Readiness",    "#00425e"
    else:
        tier, tier_col = "Developing",       "#70787e"

    st.markdown(f"""
    <div style="text-align:center; padding:2rem 0 2.5rem;">
        <span class="db-overline" style="display:block; text-align:center;">
            Hello, {user_id}
        </span>
        <div style="display:flex; flex-direction:column; align-items:center; margin:1.25rem 0;">
            <div style="width:140px; height:140px; border-radius:50%;
                        background:conic-gradient(#00425e {readiness_pct:.1f}%, #e1e2e6 0);
                        display:flex; align-items:center; justify-content:center;">
                <div style="width:108px; height:108px; border-radius:50%; background:#f8f9fc;
                            display:flex; flex-direction:column; align-items:center; justify-content:center;">
                    <span style="font-size:2rem; font-weight:900; color:#00425e;
                                 font-family:Inter,sans-serif; line-height:1;">{readiness_text}</span>
                    <span style="font-size:9px; font-weight:700; text-transform:uppercase;
                                 letter-spacing:0.1em; color:#40484e; line-height:1.8;">Readiness</span>
                </div>
            </div>
            <span style="font-size:10px; font-weight:700; text-transform:uppercase;
                         letter-spacing:0.12em; color:{tier_col}; margin-top:0.75rem;">{tier}</span>
            <p style="font-size:0.8125rem; color:#40484e; font-family:Inter,sans-serif;
                      margin-top:0.25rem; text-align:center;">
                Overall cognitive percentile vs 9,000+ test-takers
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style="text-align:center; padding:2rem 0;">
        <p style="color:#40484e; font-family:Inter,sans-serif;">
            No assessment results yet.
            Complete the <strong>Cognitive Assessment</strong> to see your readiness score.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ── Top 3 job matches ─────────────────────────────────────────────────────────

st.markdown('<span class="db-section-title">Top Job Matches</span>', unsafe_allow_html=True)

if not ability_percentiles:
    st.info("Complete the Cognitive Assessment to see job matches.")
else:
    @st.cache_resource
    def _get_recommender() -> HybridRecommender:
        return HybridRecommender()

    with st.spinner("Loading matches…"):
        rec     = _get_recommender()
        top3    = rec.recommend(
            ability_percentiles=ability_percentiles,
            user_skills=user_skills,
            top_n=3,
        )

    for r in top3:
        acts = ", ".join(r.strength_activities[:2]) if r.strength_activities else "—"
        score_bar_pct = min(r.total_score * 100, 100)
        st.markdown(f"""
        <div class="db-card db-card-accent">
            <span class="db-job-rank">#{r.rank} Match</span>
            <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                <span class="db-job-title">{r.job_title}</span>
                <span style="font-size:1.25rem; font-weight:900; color:#00425e;
                             font-family:Inter,sans-serif; white-space:nowrap; margin-left:1rem;">
                    {r.total_score * 100:.0f}%
                </span>
            </div>
            <div style="height:3px; background:#e1e2e6; border-radius:2px; margin:0.5rem 0;">
                <div style="height:100%; width:{score_bar_pct:.1f}%; background:#00425e; border-radius:2px;"></div>
            </div>
            <div style="display:flex; gap:1.5rem; margin-top:0.4rem;">
                <span style="font-size:11px; color:#40484e;">
                    <strong style="color:#006a6a;">Cognitive</strong> {r.ability_score * 100:.0f}%
                </span>
                <span style="font-size:11px; color:#40484e;">
                    <strong style="color:#00425e;">Activity</strong> {r.activity_score * 100:.0f}%
                </span>
                <span style="font-size:11px; color:#40484e;">
                    <strong style="color:#40484e;">Skills</strong> {r.skill_score * 100:.0f}%
                </span>
            </div>
            <p class="db-job-activities">Strength activities: {acts}</p>
        </div>
        """, unsafe_allow_html=True)

    _, c_mid, _ = st.columns([2, 3, 2])
    with c_mid:
        if st.button("View All Job Matches →", type="primary", use_container_width=True):
            st.switch_page("pages/04_results.py")

# ── Skills snapshot ───────────────────────────────────────────────────────────

st.markdown('<span class="db-section-title">Skills Snapshot</span>', unsafe_allow_html=True)

col_s, col_a = st.columns(2)

with col_s:
    total_skills = len(user_skills)
    st.markdown(f"""
    <div class="db-card">
        <span class="db-overline">Technical Skills</span>
        <div style="font-size:2.5rem; font-weight:900; color:#00425e;
                    font-family:Inter,sans-serif; line-height:1; margin-bottom:0.4rem;">
            {total_skills}
        </div>
        <div style="font-size:0.8125rem; color:#40484e; margin-bottom:0.75rem;">
            {len(resume_skills)} from resume &nbsp;·&nbsp; {len(manual_skills)} manually added
        </div>
        <div>
            {"".join(f'<span class="db-chip">{s}</span>' for s in user_skills[:8])}
            {"" if len(user_skills) <= 8 else f'<span class="db-chip">+{len(user_skills)-8} more</span>'}
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_a:
    abilities_assessed = len(ability_percentiles)
    st.markdown(f"""
    <div class="db-card">
        <span class="db-overline">Abilities Assessed</span>
        <div style="font-size:2.5rem; font-weight:900; color:#00425e;
                    font-family:Inter,sans-serif; line-height:1; margin-bottom:0.75rem;">
            {abilities_assessed}<span style="font-size:1rem; font-weight:600; color:#40484e;"> / 9</span>
        </div>
    """, unsafe_allow_html=True)
    if ability_percentiles:
        for label, pct in list(ability_percentiles.items())[:5]:
            short = label.split()[0]
            st.markdown(f"""
        <div class="db-ability-row">
            <div style="display:flex; justify-content:space-between; margin-bottom:2px;">
                <span style="font-size:11px; font-weight:600; color:#40484e;">{short}</span>
                <span style="font-size:11px; font-weight:700; color:#191c1e;">{pct:.0f}</span>
            </div>
            <div style="height:3px; background:#e1e2e6; border-radius:2px;">
                <div style="height:100%; width:{min(float(pct),100):.1f}%;
                            background:#00425e; border-radius:2px;"></div>
            </div>
        </div>
            """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ── Navigation CTAs ───────────────────────────────────────────────────────────

st.markdown('<span class="db-section-title">Continue</span>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("Cognitive Assessment", use_container_width=True):
        st.switch_page("pages/02_cognitive.py")
with c2:
    if st.button("Update Profile", use_container_width=True):
        st.switch_page("pages/01_profile.py")
with c3:
    if st.button("Skills & Growth", use_container_width=True):
        st.switch_page("pages/05_skills.py")
