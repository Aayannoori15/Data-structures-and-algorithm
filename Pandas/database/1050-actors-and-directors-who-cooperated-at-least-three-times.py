# 1050. Actors and Directors Who Cooperated At Least Three Times  [Easy]
# https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
# runtime 303 ms | memory 68.2 MB

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
   df=actor_director.groupby(['actor_id','director_id']).agg(numbers=('timestamp','nunique')).reset_index()
   df=df[(df['numbers']>=3)]
   return df[['actor_id','director_id']]
