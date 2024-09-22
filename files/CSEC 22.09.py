import pandas as pd

path = "files/Excel Challenge September 22nd.xlsx"

input1 = pd.read_excel(path, usecols="B:C", skiprows=2, nrows=8, names=["sub_dept", "money"])
input2 = pd.read_excel(path, usecols="E:F", skiprows=2, nrows=9, names=["department", "sub_dept"])
test = pd.read_excel(path, usecols="H:I", skiprows=2, nrows=9, names=["department", "total"])\
    .sort_values(by=['total', "department"], ascending=False)\
    .reset_index(drop=True)

lookup = (input2.assign(sub_dept=input2['sub_dept'].str.split(', '))
          .explode('sub_dept')
          .merge(input1, on='sub_dept', how='left')
          .groupby('department', as_index=False)['money'].sum()
          .sort_values(by=['money', 'department'], ascending=False)
          .reset_index(drop=True))
lookup['money'] = lookup['money'].astype('int64')
lookup.columns = test.columns

print(lookup.equals(test)) # True