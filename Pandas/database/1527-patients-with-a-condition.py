# 1527. Patients With a Condition  [Easy]
# https://leetcode.com/problems/patients-with-a-condition/
# runtime 263 ms | memory 66.6 MB

import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[(patients['conditions'].str.contains(' DIAB1')) | (patients['conditions'].str.startswith('DIAB1'))]
