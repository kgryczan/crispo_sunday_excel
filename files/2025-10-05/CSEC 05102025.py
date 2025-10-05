import pandas as pd

path = "files/2025-10-05/Challenge 65.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=13)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=13)

input['cid'] = (input['Cost Codes'] != input['Cost Codes'].shift()).cumsum()
result = input.assign(
    Consecutive = input.groupby('cid')['Cost Codes'].transform('size') > 1
)[['Consecutive']]

print(result.equals(test)) # True