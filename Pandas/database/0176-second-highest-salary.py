# 176. Second Highest Salary  [Medium]
# https://leetcode.com/problems/second-highest-salary/
# runtime 263 ms | memory 68 MB

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(ascending=False, method='dense').astype(int)
    employee = employee.sort_values('rank')
    
    df = employee[employee['rank'] == 2][['salary']]
    df.columns = [f'SecondHighestSalary']
    
    if df.empty:
        df = pd.DataFrame({f'SecondHighestSalary': [np.nan]})
    
    return df.head(1)
