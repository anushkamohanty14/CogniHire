"""Shared CSS injection for all CogniHire Streamlit pages.

Usage
-----
from apps.web._styles import inject_css
inject_css()          # full Inter + palette + component resets
inject_css("minimal") # topbar + overline only (lightweight pages)
"""
from __future__ import annotations

import streamlit as st

# ── Base palette & typography ─────────────────────────────────────────────────

_BASE = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

#MainMenu, footer, header { display: none !important; }
[data-testid="stSidebar"]    { display: none !important; }
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
"""

# ── Topbar ────────────────────────────────────────────────────────────────────

_TOPBAR = """
.ch-topbar {
    background: #f8fafc;
    border-bottom: 1px solid rgba(226,232,240,0.5);
    padding: 0 1.5rem;
    height: 64px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: -1rem -1rem 2.5rem -1rem;
}
.ch-brand {
    font-size: 1.125rem;
    font-weight: 900;
    letter-spacing: -0.04em;
    color: #00425e;
}
.ch-page-label {
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #40484e;
    opacity: 0.6;
}
"""

# ── Typography utilities ──────────────────────────────────────────────────────

_TYPE = """
.ch-overline {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    font-weight: 700;
    color: #40484e;
    opacity: 0.7;
    margin-bottom: 0.4rem;
    display: block;
}
.ch-section {
    font-size: 0.6875rem;
    text-transform: uppercase;
    letter-spacing: 0.18em;
    font-weight: 700;
    color: #40484e;
    margin: 2rem 0 1rem;
    display: block;
}
.ch-heading {
    font-size: 1.875rem;
    font-weight: 900;
    letter-spacing: -0.03em;
    color: #191c1e;
    line-height: 1.1;
    margin-bottom: 1.25rem;
}
"""

# ── Cards ─────────────────────────────────────────────────────────────────────

_CARDS = """
.ch-card {
    background: #f3f3f7;
    border-radius: 0.25rem;
    padding: 1.25rem 1.5rem;
    margin-bottom: 0.75rem;
}
.ch-card-primary  { border-left: 3px solid #00425e; }
.ch-card-success  { border-left: 3px solid #006a6a; }
.ch-card-warning  { border-left: 3px solid #b45309; }
.ch-card-neutral  { border-left: 3px solid #40484e; }
"""

# ── Chips ─────────────────────────────────────────────────────────────────────

_CHIPS = """
.ch-chip {
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
.ch-chip-amber {
    background: #fef3c7;
    color: #92400e;
}
.ch-chip-teal {
    background: #ccfbf1;
    color: #0f766e;
}
"""

# ── Form controls ─────────────────────────────────────────────────────────────

_FORMS = """
.stButton > button {
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
    font-size: 11px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    border: none !important;
    border-radius: 0.25rem !important;
    padding: 0.875rem 1.5rem !important;
    width: 100% !important;
    background-color: #edeef1 !important;
    color: #191c1e !important;
    transition: all 0.12s !important;
}
.stButton > button:hover {
    background-color: #e7e8eb !important;
    transform: scale(0.99) !important;
}
.stButton > button:active { transform: scale(0.97) !important; }
.stButton > button[kind="primary"] {
    background-color: #00425e !important;
    color: #ffffff !important;
}
.stButton > button[kind="primary"]:hover { background-color: #005b7f !important; }
.stButton > button:disabled { opacity: 0.4 !important; cursor: not-allowed !important; }

.stTextInput input, .stSelectbox > div > div {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    background: #edeef1 !important;
    border: none !important;
    border-bottom: 2px solid #c0c7ce !important;
    border-radius: 0 !important;
    color: #191c1e !important;
    padding: 0.75rem 1rem !important;
}
.stTextInput input:focus { border-bottom-color: #00425e !important; box-shadow: none !important; }
.stTextInput label, .stSelectbox label, .stNumberInput label {
    font-family: 'Inter', sans-serif !important;
    font-size: 10px !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.15em !important;
    color: #40484e !important;
}
.stNumberInput input {
    font-family: 'Inter', sans-serif !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
    background: #edeef1 !important;
    border: none !important;
    border-bottom: 2px solid #c0c7ce !important;
    border-radius: 0 !important;
    color: #191c1e !important;
    padding: 0.875rem 1rem !important;
}
"""

# ── Progress bar (bottom nav) ─────────────────────────────────────────────────

_PROGRESS = """
.ch-bottom-nav {
    position: fixed;
    bottom: 0; left: 0;
    width: 100%;
    z-index: 999;
    background: #f1f5f9;
    border-top: 1px solid #e2e8f0;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Inter', sans-serif;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #075985;
}
.ch-progress-rail {
    position: fixed;
    bottom: 0; left: 0;
    width: 100%; height: 2px;
    background: rgba(7,89,133,0.12);
    z-index: 998;
}
.ch-progress-fill {
    height: 100%;
    background: #075985;
    transition: width 0.4s ease;
}
"""

# ── Readiness ring ────────────────────────────────────────────────────────────

def readiness_ring_html(score: float, size: int = 120) -> str:
    """Return an HTML string for a conic-gradient readiness ring.

    Parameters
    ----------
    score : float
        Readiness score 0–100.
    size : int
        Outer diameter in px (default 120).
    """
    inner  = int(size * 0.75)
    label  = f"{score:.0f}"
    return f"""
<div style="width:{size}px; height:{size}px; border-radius:50%;
            background:conic-gradient(#00425e {score:.1f}%, #e1e2e6 0);
            display:flex; align-items:center; justify-content:center;">
    <div style="width:{inner}px; height:{inner}px; border-radius:50%; background:#f8f9fc;
                display:flex; flex-direction:column; align-items:center; justify-content:center;">
        <span style="font-size:{size // 5}px; font-weight:900; color:#00425e;
                     font-family:Inter,sans-serif; line-height:1;">{label}</span>
        <span style="font-size:9px; font-weight:700; text-transform:uppercase;
                     letter-spacing:0.1em; color:#40484e; line-height:1.8;">Readiness</span>
    </div>
</div>
"""


# ── Topbar helper ─────────────────────────────────────────────────────────────

def topbar_html(page_label: str = "") -> str:
    """Return the standard CogniHire topbar HTML."""
    label_part = f'<span class="ch-page-label">{page_label}</span>' if page_label else ""
    return (
        f'<div class="ch-topbar">'
        f'<span class="ch-brand">CogniHire</span>'
        f'{label_part}'
        f'</div>'
    )


# ── Public inject function ────────────────────────────────────────────────────

_PROFILES = {
    "full":    _BASE + _TOPBAR + _TYPE + _CARDS + _CHIPS + _FORMS + _PROGRESS,
    "minimal": _BASE + _TOPBAR + _TYPE,
}


def inject_css(profile: str = "full") -> None:
    """Inject CogniHire shared CSS into the current Streamlit page.

    Parameters
    ----------
    profile : {"full", "minimal"}
        "full"    — all components (default, use for all app pages).
        "minimal" — base + topbar + typography only (use for static pages).
    """
    css = _PROFILES.get(profile, _PROFILES["full"])
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
