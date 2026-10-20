# 2878. Get the Size of a DataFrame  [Easy]
# https://leetcode.com/problems/get-the-size-of-a-dataframe/
# runtime 264 ms | memory 66.6 MB

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df=pd.DataFrame(players)
    return list(df.shape)
