import pandas as pd

path = "files/2025-06-29/Challenge 37.xlsx"

input = pd.read_excel(path, usecols="B:F", skiprows=2, nrows=8)
test = pd.read_excel(path, usecols="H:O", skiprows=2, nrows=1)
test = test.rename(columns={test.columns[0]: "Item"})

input['Col'] = input[['Level', 'Gender', 'Location']].bfill(axis=1).iloc[:, 0]
result = input.pivot(index='Item', columns='Col', values='Values').reset_index()[test.columns]

print(result.equals(test)) # True
