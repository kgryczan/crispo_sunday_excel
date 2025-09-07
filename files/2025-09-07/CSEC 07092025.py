import pandas as pd

path = "files/2025-09-07/Challenge 57.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=6)
test  = pd.read_excel(path, usecols="F:K", skiprows=1, nrows=3)

input_long = (
    input.assign(**{'Assigned Staff': input['Assigned Staff'].str.split(', ')})
    .explode('Assigned Staff')
    .dropna(subset=['Assigned Staff'])
)
input_long['rn'] = input_long.groupby('Assigned Staff').cumcount() + 1
result = (
    input_long.pivot(index='rn', columns='Assigned Staff', values='Activity Code')
    .reindex(columns=test.columns)
    .reset_index(drop=True)
)
result.columns.name = None

print(result.equals(test)) # True