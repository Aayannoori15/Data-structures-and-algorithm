# 586. Customer Placing the Largest Number of Orders  [Easy]
# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
# runtime 291 ms | memory 68.3 MB

import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(orders.value_counts('customer_number'))
    df=pd.merge(df,orders,on='customer_number',how='outer')
    new = df[df['count'] == df['count'].max()]
    return new[['customer_number']].head(1)
