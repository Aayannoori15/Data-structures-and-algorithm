# 1683. Invalid Tweets  [Easy]
# https://leetcode.com/problems/invalid-tweets/
# runtime 311 ms | memory 67.8 MB

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df=tweets[(tweets['content'].str.len()>15)]
    return df[['tweet_id']]
