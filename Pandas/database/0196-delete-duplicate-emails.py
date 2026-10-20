# 196. Delete Duplicate Emails  [Easy]
# https://leetcode.com/problems/delete-duplicate-emails/
# runtime 245 ms | memory 68.1 MB

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values('id',inplace=True)
    person.drop_duplicates(subset=['email'], inplace=True)
