# 184. Department Highest Salary  [Medium]
# https://leetcode.com/problems/department-highest-salary/
# runtime 310 ms | memory 69.3 MB

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df=employee.groupby('departmentId', as_index=False)['salary'].max()
    employee=pd.merge(employee,df,how='right')
    department.columns=['departmentId','name']
    employee=pd.merge(employee,department,on='departmentId',how='outer')
    employee.columns=['id','Employee','Salary','departmentId','Department']
    employee=employee.dropna()
    return employee[['Department','Employee','Salary']]
