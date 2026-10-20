# 511. Game Play Analysis I  [Easy]
# https://leetcode.com/problems/game-play-analysis-i/
# runtime 298 ms | memory 68.2 MB

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity=activity.sort_values('event_date')
    activity=activity.drop_duplicates('player_id')
    activity.columns=['player_id','device_id','first_login','games_played']
    return activity[['player_id','first_login']]
