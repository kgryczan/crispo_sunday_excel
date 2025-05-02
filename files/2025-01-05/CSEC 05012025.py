import pandas as pd

path = "files/Ex-Challenge 01 2025.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=12)
test = pd.read_excel(path, usecols="G:J", skiprows=1, nrows=6)\
    .rename(columns=lambda x: x.replace('.1', ''))\
    .apply(lambda x: x.str.strip() if x.name == 'Invoice' else x)

input['name'] = input[['Invoice', 'Posted', 'Dept']]\
    .apply(lambda x: x.str.strip()).astype(str)\
    .agg('_'.join, axis=1)

grouped = input.groupby('name')\
    .filter(lambda x: len(x) == 1 or (len(x) == 2 and x['Value'].sum() != 0))

result = grouped.copy().assign(**grouped['name'].str.split('_', expand=True).rename(columns={0: 'Invoice', 1: 'Posted', 2: 'Dept'}))\
    .drop(columns=['name']).reset_index(drop=True)

print(result.equals(test)) # True