# 2879. Display the First Three Rows  [Easy]
# https://leetcode.com/problems/display-the-first-three-rows/
# runtime 279 ms | memory 66.3 MB

import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(employees)
    return df.head(3)
