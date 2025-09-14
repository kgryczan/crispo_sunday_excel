import pandas as pd

path = "files/2025-09-14/challenge 60.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=17)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=7)

input['Stem'] = (input['Quantity'] // 10)
input['Leaf'] = (input['Quantity'] % 10)
input = input.sort_values(['Stem', 'Leaf'])
input = input.astype(str)
result = input.groupby('Stem')['Leaf'].apply(' '.join).reset_index()

print(pd.concat([test, result], axis=1))