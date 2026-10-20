# 2887. Fill Missing Data  [Easy]
# https://leetcode.com/problems/fill-missing-data/
# runtime 304 ms | memory 66.3 MB

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"].fillna(0,inplace=True)
    return products
