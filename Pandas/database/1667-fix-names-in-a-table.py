# 1667. Fix Names in a Table  [Easy]
# https://leetcode.com/problems/fix-names-in-a-table/
# runtime 311 ms | memory 68 MB

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name']=users['name'].str.lower().str.capitalize()
    users=users.sort_values('user_id')
    return users
