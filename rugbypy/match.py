# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/match.ipynb.

# %% auto 0
__all__ = ['fetch_matches', 'fetch_match_details']

# %% ../nbs/match.ipynb 4
import pandas as pd

# %% ../nbs/match.ipynb 5
def fetch_matches(date: str):
    """Fetches all match information on a particular date that includes: \n
    * match_id \n
    * competition_id \n
    * home_team_id \n
    * away_team_id
    """

    print(f"Fetching matches on date:{date}...")
    try:
        date_url = f"https://github.com/seanyboi/rugbydata/blob/main/data/dates/{date}.parquet?raw=true"
        matches = pd.read_parquet(date_url, engine="pyarrow")
        matches = matches.assign(date=date)
        return matches
    except Exception as e:
        print(
            f"No match information for matches played on {date} either because no matches took place or rugbypy does not have access to the match data. Please raise if neither."
        )

# %% ../nbs/match.ipynb 7
def fetch_match_details(match_id: str):
    """Fetches match data for a certain match_id"""
    print(f"Fetching match details for match_id:{match_id}...")
    try:
        match_url = f"https://github.com/seanyboi/rugbydata/blob/main/data/match/{match_id}.parquet?raw=true"
        matches = pd.read_parquet(match_url, engine="pyarrow")
        return matches
    except Exception as e:
        print(f"Error fetching match data - {e}. Please raise an issue!")
