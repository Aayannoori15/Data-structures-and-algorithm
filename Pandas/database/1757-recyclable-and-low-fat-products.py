# 1757. Recyclable and Low Fat Products  [Easy]
# https://leetcode.com/problems/recyclable-and-low-fat-products/
# runtime 287 ms | memory 67.6 MB

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    subset=products[(products["low_fats"]=='Y') & (products["recyclable"]=='Y')]
    return subset[["product_id"]]
