# 2891. Method Chaining  [Easy]
# https://leetcode.com/problems/method-chaining/
# runtime 313 ms | memory 67.1 MB

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    result=animals[animals["weight"]>100]
    result.sort_values(by="weight",ascending=False,inplace=True)
    return result[["name"]]
