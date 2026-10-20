# 1378. Replace Employee ID With The Unique Identifier  [Easy]
# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
# runtime 311 ms | memory 68.1 MB

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df=pd.merge(employees,employee_uni,on='id',how='left')
    return df[['unique_id','name']]
