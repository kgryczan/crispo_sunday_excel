import pandas as pd

path = "files/2025-09-28/Challenge 67.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="G:J", skiprows=1, nrows=5).rename(columns=lambda c: c.replace('.1', ''))

numeric_cols = input.select_dtypes(include='number').columns
for col in numeric_cols:
    input[col] = input[col] + input[col].iloc[0]
result = input.iloc[1:].reset_index(drop=True)

result.columns = test.columns
print(result.equals(test)) # True