# 2889. Reshape Data: Pivot  [Easy]
# https://leetcode.com/problems/reshape-data-pivot/
# runtime 294 ms | memory 67.8 MB

import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df = weather.pivot(index="month", columns="city", values="temperature")
    result=pd.DataFrame(df)
    return result
