# 2888. Reshape Data: Concatenate  [Easy]
# https://leetcode.com/problems/reshape-data-concatenate/
# runtime 341 ms | memory 66.8 MB

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df=pd.concat([df1,df2],axis=0)
    return df
