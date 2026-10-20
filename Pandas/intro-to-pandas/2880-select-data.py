# 2880. Select Data  [Easy]
# https://leetcode.com/problems/select-data/
# runtime 309 ms | memory 67 MB

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(students)
    filterrow=df[df["student_id"]==101]
    subset=filterrow[['name','age']]
    return subset
