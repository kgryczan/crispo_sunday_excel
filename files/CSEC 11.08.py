import pandas as pd

path = "files/Excel Challenge 11th August.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1)
test  = pd.read_excel(path, usecols="E:F", skiprows=1, nrows = 7)

input['Count'] = input.groupby('Price')['Price'].transform('count')

dupes = input["Cookies"][input['Count'] > 1].reset_index(drop=True)
unique = input["Cookies"][input['Count'] == 1].reset_index(drop=True)

print(sorted(dupes) == sorted(test["Duplicate Price"]) and sorted(unique) == sorted(test["Unique Price"][0:5]))
