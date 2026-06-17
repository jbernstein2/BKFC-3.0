# app.py

import streamlit as st
import pandas as pd

from branding import apply_streamlit_theme
from data_parser import (
    load_brooklyn_season_stats,
    load_opponent_season_stats,
    load_match_stats,
    prepare_kpi_frame,
)
from insight import (
    compute_match_kpis_from_df,
    build_season_comparison,
    compute_season_averages,
)
from report_generator import generate_match_deck


def main():
    st.set_page_config(
        page_title="Brooklyn FC Match Report",
        layout="wide",
    )
    apply_streamlit_theme(st)

    st.title("Brooklyn FC Match Report System")

    st.sidebar.header("Data inputs")

    brooklyn_season_file = st.sidebar.file_uploader(
        "Brooklyn season Excel", type=["xlsx"]
    )
    opponent_season_file = st.sidebar.file_uploader(
        "Opponent season Excel", type=["xlsx"]
    )
    match_file = st.sidebar.file_uploader(
        "Match stats Excel (Brooklyn vs opponent)", type=["xlsx"]
    )

    opponent_name = st.sidebar.text_input("Opponent name", value="Opponent")
    match_label = st.sidebar.text_input(
        "Match label", value="Louisville City 2-2 Brooklyn"
    )

    generate_deck = st.sidebar.button("Generate PowerPoint deck")

    if not (brooklyn_season_file and opponent_season_file and match_file):
        st.info("Upload all three Excel files to start.")
        return

    # Load data
    brooklyn_season_df = load_brooklyn_season_stats(brooklyn_season_file)
    opponent_season_df = load_opponent_season_stats(opponent_season_file)
    match_df = load_match_stats(match_file)

    # Tabs
    tab_match, tab_season = st.tabs(
        ["Match KPIs & Visuals", "Season Averages Comparison"]
    )

    # --- Match tab ---
    with tab_match:
        st.subheader("Match KPIs: Brooklyn vs Opponent")

        match_kpis = compute_match_kpis_from_df(match_df)

        brooklyn_kpis = match_kpis.get("Brooklyn", {})
        opponent_kpis = match_kpis.get(opponent_name, {})

        kpi_df = prepare_kpi_frame(brooklyn_kpis, opponent_kpis)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Brooklyn xG", round(brooklyn_kpis.get("xG", 0), 2))
            st.metric(
                "Brooklyn Shots",
                brooklyn_kpis.get("Shots", 0),
            )
            st.metric(
                "Brooklyn Possession %",
                round(brooklyn_kpis.get("Possession %", 0), 1),
            )
        with col2:
            st.metric(
                f"{opponent_name} xG",
                round(opponent_kpis.get("xG", 0), 2),
            )
            st.metric(
                f"{opponent_name} Shots",
                opponent_kpis.get("Shots", 0),
            )
            st.metric(
                f"{opponent_name} Possession %",
                round(opponent_kpis.get("Possession %", 0), 1),
            )

        st.bar_chart(
            kpi_df.pivot(index="KPI", columns="Team", values="Value")
        )

        st.caption(
            "Simple match-level comparison of key metrics. "
            "We’ll plug in WyScout PDF parsing later."
        )

    # --- Season tab ---
    with tab_season:
        st.subheader("Season Averages: Brooklyn vs Opponent")

        season_comp_df = build_season_comparison(
            brooklyn_season_df, opponent_season_df, opponent_name
        )

        st.dataframe(season_comp_df)

        st.bar_chart(
            season_comp_df.pivot(index="KPI", columns="Team", values="Value")
        )

    # --- PowerPoint generation ---
    if generate_deck:
        brooklyn_season_avg = compute_season_averages(
            brooklyn_season_df, "Brooklyn"
        )
        opponent_season_avg = compute_season_averages(
            opponent_season_df, opponent_name
        )

        output_path = generate_match_deck(
            output_path="brooklyn_match_report.pptx",
            match_kpis_brooklyn=brooklyn_kpis,
            match_kpis_opponent=opponent_kpis,
            brooklyn_season_avg=brooklyn_season_avg,
            opponent_season_avg=opponent_season_avg,
            opponent_name=opponent_name,
            match_label=match_label,
        )

        st.success(f"PowerPoint deck generated: {output_path}")


if __name__ == "__main__":
    main()
