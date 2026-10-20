# 1484. Group Sold Products By The Date  [Easy]
# https://leetcode.com/problems/group-sold-products-by-the-date/
# runtime 333 ms | memory 68.1 MB

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
   df=activities.groupby('sell_date',as_index=False)['product'].apply(lambda x: sorted(set(x)))
   df['num_sold']=df['product'].apply(lambda x:len(x))
   df['products']=df['product'].apply(lambda x : ','.join(x))
   return df[['sell_date','num_sold','products']]
