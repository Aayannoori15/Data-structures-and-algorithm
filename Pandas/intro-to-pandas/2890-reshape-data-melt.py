# 2890. Reshape Data: Melt  [Easy]
# https://leetcode.com/problems/reshape-data-melt/
# runtime 294 ms | memory 66.8 MB

import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    melted = pd.melt(report, id_vars=["product"], var_name="quarter", value_name="sales")
    return melted
