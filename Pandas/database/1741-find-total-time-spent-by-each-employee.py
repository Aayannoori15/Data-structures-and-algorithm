# 1741. Find Total Time Spent by Each Employee  [Easy]
# https://leetcode.com/problems/find-total-time-spent-by-each-employee/
# runtime 350 ms | memory 67.6 MB

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time']=employees['out_time']-employees['in_time']
    employees=employees.groupby(['emp_id','event_day'],as_index=False)['total_time'].sum()
    employees.columns=['emp_id','day','total_time']
    return employees[['day','emp_id','total_time']]
