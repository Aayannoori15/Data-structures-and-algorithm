# 2884. Modify Columns  [Easy]
# https://leetcode.com/problems/modify-columns/
# runtime 298 ms | memory 66.4 MB

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"]=employees["salary"]*2
    return employees
