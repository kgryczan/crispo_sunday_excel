import pandas as pd

path = "files/Excel Challenge October 17th.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=15)
test = pd.read_excel(path, usecols="E", skiprows=1, nrows=15)

input['group'] = (input['Defects'] != input['Defects'].shift()).cumsum()
input['Running Totals'] = input.groupby('group')['Units Made'].cumsum().where(input['Defects'] != 1, 0)

print(input['Running Totals'].eq(test['Running Totals']).all()) # True