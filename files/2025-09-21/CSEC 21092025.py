import pandas as pd

path = "files/2025-09-21/Challenge 61.xlsx"
input = pd.read_excel(path, usecols="B:F", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="H:J", skiprows=1, nrows=6).rename(columns=lambda x: x.replace('.1', ''))

result = input.dropna(axis=1, how='all')
print(test.equals(result))   # True

result2 = input.loc[:, input.notna().any()]
print(test.equals(result2))  # True
