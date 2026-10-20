# 1795. Rearrange Products Table  [Easy]
# https://leetcode.com/problems/rearrange-products-table/
# runtime 320 ms | memory 67.2 MB

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df=pd.melt(
    products,
    id_vars=['product_id'],
    value_vars=['store1','store2','store3'],
    var_name='store',
    value_name='price'
    )
    return df.dropna()
