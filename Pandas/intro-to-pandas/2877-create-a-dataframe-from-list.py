# 2877. Create a DataFrame from List  [Easy]
# https://leetcode.com/problems/create-a-dataframe-from-list/
# runtime 242 ms | memory 66 MB

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df=pd.DataFrame(student_data,columns=["student_id","age"])
    return df
