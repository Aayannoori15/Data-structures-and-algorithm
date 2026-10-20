# 177. Nth Highest Salary  [Medium]
# https://leetcode.com/problems/nth-highest-salary/
# runtime 259 ms | memory 67.7 MB

import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(ascending=False, method='dense').astype(int)
    employee = employee.sort_values('rank')
    
    df = employee[employee['rank'] == N][['salary']]
    df.columns = [f'getNthHighestSalary({N})']
    
    if df.empty:
        df = pd.DataFrame({f'getNthHighestSalary({N})': [np.nan]})
    
    return df.head(1)
