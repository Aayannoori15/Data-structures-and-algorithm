# 2881. Create a New Column  [Easy]
# https://leetcode.com/problems/create-a-new-column/
# runtime 294 ms | memory 65.7 MB

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(employees)
    df["bonus"]=df["salary"]*2
    return df
