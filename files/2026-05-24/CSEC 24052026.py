import pandas as pd
import numpy as np

path = "2026-05-24/Challenge 122.xlsx"
input = pd.read_excel(path, usecols="B", nrows=9, skiprows=2)
test = pd.read_excel(path, usecols="D", nrows=9, skiprows=2)

def first_nonduplicated_char(s):
    for c in s:
        if s.count(c) == 1:
            return c
    return np.nan

input["First Nonduplicated Character"] = input["Text"].apply(first_nonduplicated_char)
print(input["First Nonduplicated Character"].equals(test['1st Unique']))
# True