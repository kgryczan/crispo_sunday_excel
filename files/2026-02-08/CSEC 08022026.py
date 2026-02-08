import pandas as pd
import re

path = "2026-02-08/Challenge 102.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=11)
test = pd.read_excel(path, usecols="E", skiprows=2, nrows=1, header=None).iloc[0, 0]

def clean_string(s):
    return re.sub(r'[^a-z]+', ' ', s.lower())

res = input[input.Status.apply(lambda s:
    "complete" in clean_string(s)
    and "ok" in clean_string(s)
    and not re.search(r'not ok|risk|hold|incomplete', clean_string(s))
)]

print(len(res) == test)
# True