# insight.py

import pandas as pd


def compute_match_kpis_from_df(df: pd.DataFrame) -> dict:
    """
    Given a match-level DataFrame (one row for Brooklyn, one for opponent),
    compute a simple KPI dict for each side.

    Expected columns (you can adapt later):
    - 'team'
    - 'xG'
    - 'shots'
    - 'shots_on_target'
    - 'possession'
    """
    kpis = {}
    for _, row in df.iterrows():
        team = row["team"]
        kpis[team] = {
            "xG": row.get("xG", None),
            "Shots": row.get("shots", None),
            "Shots on target": row.get("shots_on_target", None),
            "Possession %": row.get("possession", None),
        }
    return kpis


def compute_season_averages(df: pd.DataFrame, team_name: str) -> dict:
    """
    Compute season averages for a given team from its season DataFrame.

    Expected columns:
    - 'team' (or all rows already filtered)
    - 'xG'
    - 'shots'
    - 'shots_on_target'
    - 'possession'
    - 'goals_for'
    - 'goals_against'
    """
    if "team" in df.columns:
        df_team = df[df["team"] == team_name]
    else:
        df_team = df

    return {
        "xG": df_team["xG"].mean(),
        "Shots": df_team["shots"].mean(),
        "Shots on target": df_team["shots_on_target"].mean(),
        "Possession %": df_team["possession"].mean(),
        "Goals for": df_team["goals_for"].mean(),
        "Goals against": df_team["goals_against"].mean(),
    }


def build_season_comparison(
    brooklyn_season: pd.DataFrame,
    opponent_season: pd.DataFrame,
    opponent_name: str,
) -> pd.DataFrame:
    """
    Return a tidy DataFrame comparing Brooklyn season averages
    vs opponent season averages.
    """
    brooklyn_avg = compute_season_averages(brooklyn_season, "Brooklyn")
    opponent_avg = compute_season_averages(opponent_season, opponent_name)

    rows = []
    for kpi in brooklyn_avg.keys():
        rows.append(
            {"KPI": kpi, "Team": "Brooklyn", "Value": brooklyn_avg[kpi]}
        )
        rows.append(
            {"KPI": kpi, "Team": opponent_name, "Value": opponent_avg[kpi]}
        )

    return pd.DataFrame(rows)
