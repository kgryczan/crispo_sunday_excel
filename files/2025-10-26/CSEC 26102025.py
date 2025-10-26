import pandas as pd
import numpy as np

path = "files/2025-10-26/Challenge 72.xlsx"

input = pd.read_excel(path, header=None, skiprows=2, nrows=6, usecols="B:F", dtype=str)
test = pd.read_excel(path, header=None, skiprows=2, nrows=10, usecols="H:K", dtype=str)
test.iloc[:, 0] = test.iloc[:, 0].str.title()

input.iloc[:, 0] = input.iloc[:, 0].str.title()
input['measure'] = input.iloc[:, 0].where(~input.iloc[:, 0].str.contains("item", case=False), None)
input['measure'] = input['measure'].ffill()
filtered = input[input['measure'] != input.iloc[:, 0]]

longer = filtered.melt(id_vars=['measure', filtered.columns[0], filtered.columns[1]], 
                      var_name='item', value_name='value')
wider = longer.pivot_table(index=[filtered.columns[0], filtered.columns[1], 'item'],
                           columns='measure', values='value', aggfunc='first').reset_index()
wider = pd.concat([pd.DataFrame([{filtered.columns[0]: np.nan, filtered.columns[1]: np.nan, 'item': '', 'Units': 'Units', 'Availability': 'Availability'}]), wider], ignore_index=True)
wider = wider.drop('item', axis=1)
wider.columns = test.columns

print(wider.equals(test)) # True