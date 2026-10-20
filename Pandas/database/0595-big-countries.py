# 595. Big Countries  [Easy]
# https://leetcode.com/problems/big-countries/
# runtime 361 ms | memory 69.2 MB

import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    subset=world[(world["area"]>=3000000) | (world["population"]>=25000000)]
    return subset[["name","population","area"]]
