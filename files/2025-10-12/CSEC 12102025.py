import pandas as pd

path = "files/2025-10-12/Challenge 70.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=11)
test = pd.read_excel(path, usecols="E:F", skiprows=1, nrows=4).rename(columns=lambda col: col.replace('.1', ''))

input['Item'] = "Group " + input['Item'].str.contains("Group").cumsum().astype(str)
result = input.groupby('Item', as_index=False)['Prices'].sum()

print(result.equals(test))