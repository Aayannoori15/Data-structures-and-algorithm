# 2882. Drop Duplicate Rows  [Easy]
# https://leetcode.com/problems/drop-duplicate-rows/
# runtime 258 ms | memory 66.9 MB

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset=["email"],inplace=True)
    return customers
