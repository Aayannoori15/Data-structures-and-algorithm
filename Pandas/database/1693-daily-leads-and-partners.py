# 1693. Daily Leads and Partners  [Easy]
# https://leetcode.com/problems/daily-leads-and-partners/
# runtime 351 ms | memory 68.1 MB

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df=daily_sales.groupby(['date_id','make_name'],as_index=False).agg(unique_leads=('lead_id','nunique'),unique_partners=('partner_id','nunique'))
    return df
