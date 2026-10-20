# 1148. Article Views I  [Easy]
# https://leetcode.com/problems/article-views-i/
# runtime 278 ms | memory 67.3 MB

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df=views[(views['author_id']==views["viewer_id"])]
    df2=df.drop_duplicates('author_id')
    df3=df2[['author_id']]
    df3.columns=['id']
    df3=df3.sort_values('id')
    return df3
