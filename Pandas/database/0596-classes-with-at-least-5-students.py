# 596. Classes With at Least 5 Students  [Easy]
# https://leetcode.com/problems/classes-with-at-least-5-students/
# runtime 290 ms | memory 69.1 MB

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses=courses.sort_values('class',ascending=False)
    df=pd.DataFrame(courses['class'].value_counts())
    courses=courses.drop_duplicates('class')
    df=pd.merge(df,courses,on='class',how='outer')
    df=df[(df['count']>=5)]
    return df[['class']]
