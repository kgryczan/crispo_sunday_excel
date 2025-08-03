import pandas as pd

path = "files/2025-08-03/Challenge 48.xlsx"
input = pd.read_excel(path, usecols="A:H", skiprows=1, nrows=4)
test  = pd.read_excel(path, usecols="J:K", nrows=3)

result = input.iloc[:, [0]].copy()
result['combined'] = input.iloc[:, 1:8].astype(str).agg(''.join, axis=1)\
    .str.replace(r'^0+|0+$', '', regex=True)\
    .apply(lambda x: ','.join(x) if pd.notnull(x) else x)
result.columns = ['item', 'combined']
test.columns = ['item', 'combined']

print(result.equals(test)) # True