# branding.py

BROOKLYN_PRIMARY = "#000000"  # Black
BROOKLYN_GOLD = "#D4AF37"     # Gold
BROOKLYN_SILVER = "#C0C0C0"   # Silver
BROOKLYN_WHITE = "#FFFFFF"    # White

APP_BACKGROUND = "#111111"
CARD_BACKGROUND = "#1C1C1C"
ACCENT_COLOR = BROOKLYN_GOLD

def apply_streamlit_theme(st):
    """
    Apply basic theming to the Streamlit app using Brooklyn FC colors.
    """
    st.markdown(
        f"""
        <style>
        .reportview-container .main {{
            background-color: {APP_BACKGROUND};
            color: {BROOKLYN_WHITE};
        }}
        .sidebar .sidebar-content {{
            background-color: {CARD_BACKGROUND};
        }}
        .stMetric, .stDataFrame, .stTable {{
            background-color: {CARD_BACKGROUND};
            border-radius: 8px;
        }}
        .stButton>button {{
            background-color: {ACCENT_COLOR};
            color: {BROOKLYN_BLACK};
            border-radius: 6px;
            border: none;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
