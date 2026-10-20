# 2883. Drop Missing Data  [Easy]
# https://leetcode.com/problems/drop-missing-data/
# runtime 255 ms | memory 67.3 MB

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(subset=["name"],axis=0,inplace=True)
    return students
