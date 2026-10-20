# 1873. Calculate Special Bonus  [Easy]
# https://leetcode.com/problems/calculate-special-bonus/
# runtime 391 ms | memory 68.6 MB

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df=employees[(employees['employee_id']%2!=0)]
    df=df[(~df['name'].str.startswith('M'))]
    new=pd.merge(df,employees,on='employee_id',how="outer")
    new=new[['employee_id','salary_x']]
    new.columns=['employee_id','bonus']
    new=new.fillna(0)
    return new
