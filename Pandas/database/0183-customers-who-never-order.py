# 183. Customers Who Never Order  [Easy]
# https://leetcode.com/problems/customers-who-never-order/
# runtime 289 ms | memory 68.3 MB

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    new=orders.copy()
    new.columns=['index','id']
    df=pd.merge(customers,new,on='id',how='outer')
    df2=df[(df['index'].isna())]
    df3= df2[['name']]
    df3.columns=['Customers']
    return df3
