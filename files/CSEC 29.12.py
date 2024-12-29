import pandas as pd

path = "files/Excel Challenge 29th Dec.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=8)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=14)

input = input.dropna().assign(Problem=input['Problem'].str.split('')).explode('Problem').query('Problem != ""').reset_index(drop=True)

print(input['Problem'].equals(test['Solution Required'])) # True