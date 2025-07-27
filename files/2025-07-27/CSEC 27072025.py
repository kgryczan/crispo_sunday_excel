import pandas as pd

path = "files/2025-07-27/CSEC 27072025.xlsx"
input = pd.read_excel(path, usecols="B:N", skiprows=1, nrows=3)
requirements = input.iloc[0].to_frame('Requirements')
test = input.iloc[1].to_frame('Test')
requirements['New Purchase'] = (req := requirements['Requirements']).sub(req.cummax().shift(fill_value=0)).clip(lower=0)

print(all(test['Test'] == requirements['New Purchase'])) # True
