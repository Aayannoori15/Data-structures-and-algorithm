# 570. Managers with at Least 5 Direct Reports  [Medium]
# https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
# runtime 275 ms | memory 68.6 MB

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby("managerId", as_index = False).agg("count")
    return employee[employee["id"].isin(df[df["id"] >= 5]["managerId"].values)][["name"]]
