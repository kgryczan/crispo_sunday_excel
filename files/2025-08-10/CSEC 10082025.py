import pandas as pd

path = "files/2025-08-10/Challenge 50.xlsx"
param = "National ID"
input = pd.read_excel(path, usecols="A:C", skiprows=1, nrows = 12)
test  = pd.read_excel(path, usecols="E", skiprows=1, nrows = 4).squeeze().to_list()

result = (input.groupby('Staff No.')
            .filter(lambda g: param not in g['Identifiers'].values)
            ['Staff No.'].unique().tolist())

print(result == test) # True