import pandas as pd

path = "files/CHALLENGE 1205.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=11)
test = pd.read_excel(path, usecols="D:G", skiprows=2, nrows=4)

input[['sub_department', 'department']] = input['SUB-DEPARTMENT NAMES'].str.split('-', n=1, expand=True)
input['rn'] = input.groupby('sub_department').cumcount() + 1
input = input.drop(columns=['department'])

result = input.pivot(index='rn', columns='sub_department', values='SUB-DEPARTMENT NAMES').reindex(columns=input['sub_department'].unique()).reset_index(drop=True)
result.index.name = None
result.columns.name = None

print(result.equals(test)) # True