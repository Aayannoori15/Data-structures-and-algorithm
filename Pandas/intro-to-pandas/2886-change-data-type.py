# 2886. Change Data Type  [Easy]
# https://leetcode.com/problems/change-data-type/
# runtime 275 ms | memory 66.2 MB

import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"]=students["grade"].astype(int)
    return students
