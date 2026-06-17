# data_parser.py

import pandas as pd
from typing import Dict


def load_brooklyn_season_stats(path: str) -> pd.DataFrame:
    """
    Load Brooklyn FC season stats from an Excel file.
    Assumes one sheet with row-per-match or aggregated stats.
    """
    return pd.read_excel(path)


def load_opponent_season_stats(path: str) -> pd.DataFrame:
    """
    Load opponent season stats from an Excel file.
    Used as season baseline for that specific opponent.
    """
    return pd.read_excel(path)


def load_match_stats(path: str, sheet_name: str = None) -> pd.DataFrame:
    """
    Load match-level stats (Brooklyn vs specific opponent) from Excel.
    This can be a dedicated match report sheet you maintain.
    """
    if sheet_name:
        return pd.read_excel(path, sheet_name=sheet_name)
    return pd.read_excel(path)


def prepare_kpi_frame(
    brooklyn_match: Dict,
    opponent_match: Dict,
) -> pd.DataFrame:
    """
    Take simple dicts of match KPIs and return a tidy DataFrame
    for easy plotting and comparison.

    Example dict structure:
    brooklyn_match = {"xG": 2.39, "Shots": 14, "Possession": 47}
    opponent_match = {"xG": 3.21, "Shots": 25, "Possession": 53}
    """
    data = []
    for kpi in brooklyn_match.keys():
        data.append(
            {
                "KPI": kpi,
                "Team": "Brooklyn",
                "Value": brooklyn_match[kpi],
            }
        )
        data.append(
            {
                "KPI": kpi,
                "Team": "Opponent",
                "Value": opponent_match.get(kpi, None),
            }
        )
    return pd.DataFrame(data)
