import pandas as pd

path = "files/2025-08-31/Challenge 53.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="G", skiprows=1, nrows=2).squeeze().tolist()

result = input[input.drop('Customer', axis=1).isna().all(axis=1)]['Customer'].tolist()

print(test == result) # True