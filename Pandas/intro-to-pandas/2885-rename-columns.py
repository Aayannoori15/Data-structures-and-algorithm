# 2885. Rename Columns  [Easy]
# https://leetcode.com/problems/rename-columns/
# runtime 276 ms | memory 66.6 MB

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
   students.rename(columns={"id": "student_id", "first": "first_name", "last": "last_name", "age": "age_in_years"}, inplace=True)
   return students
