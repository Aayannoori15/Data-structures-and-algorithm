# 1907. Count Salary Categories  [Medium]
# https://leetcode.com/problems/count-salary-categories/
# runtime 335 ms | memory 90 MB

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    Lc=(accounts['income']<20000).sum()
    Ac=((accounts['income']>=20000) & (accounts['income']<=50000) ).sum()
    Hc=(accounts['income']>50000 ).sum()
    output={
        'category':['Low Salary','Average Salary','High Salary'],
        'accounts_count':[Lc,Ac,Hc]
    }
    df=pd.DataFrame(output)
    return df
