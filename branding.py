import streamlit as st

# ============================================================
# BROOKLYN FC BRAND COLORS
# ============================================================

BROOKLYN_BLACK = "#000000"
BROOKLYN_GOLD = "#D4AF37"
BROOKLYN_SILVER = "#A6A6A6"
BROOKLYN_WHITE = "#FFFFFF"

# ============================================================
# APPLY GLOBAL STREAMLIT THEME
# ============================================================

def apply_streamlit_theme():
    """
    Injects custom CSS to apply Brooklyn FC branding across the app.
    """

    st.markdown(
        f"""
        <style>

        /* GLOBAL BACKGROUND */
        .stApp {{
            background-color: {BROOKLYN_BLACK};
            color: {BROOKLYN_WHITE};
        }}

        /* HEADERS */
        h1, h2, h3, h4, h5, h6 {{
            color: {BROOKLYN_GOLD} !important;
        }}

        /* SIDEBAR */
        section[data-testid="stSidebar"] {{
            background-color: {BROOKLYN_SILVER};
        }}

        /* METRIC CARDS */
        .metric-card {{
            background-color: {BROOKLYN_BLACK};
            border: 1px solid {BROOKLYN_GOLD};
            padding: 12px;
            border-radius: 8px;
            margin-bottom: 10px;
        }}

        .metric-title {{
            font-size: 14px;
            color: {BROOKLYN_GOLD};
        }}

        .metric-value {{
            font-size: 22px;
            font-weight: bold;
            color: {BROOKLYN_WHITE};
        }}

        /* TABLES */
        table {{
            color: {BROOKLYN_WHITE} !important;
        }}

        /* BUTTONS */
        .stButton>button {{
            background-color: {BROOKLYN_GOLD};
            color: {BROOKLYN_BLACK};
            border-radius: 6px;
            border: none;
            font-weight: bold;
        }}

        .stButton>button:hover {{
            background-color: {BROOKLYN_WHITE};
            color: {BROOKLYN_BLACK};
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# METRIC CARD COMPONENT
# ============================================================

def metric_card(title, value, baseline=None, team="brooklyn"):
    """
    Renders a styled metric card.
    team = "brooklyn" or "opponent"
    """

    color = BROOKLYN_GOLD if team == "brooklyn" else BROOKLYN_SILVER

    baseline_text = f"<div style='color:{BROOKLYN_SILVER}; font-size:12px;'>Baseline: {baseline}</div>" if baseline else ""

    st.markdown(
        f"""
        <div class="metric-card" style="border-color:{color};">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            {baseline_text}
        </div>
        """,
        unsafe_allow_html=True
    )
