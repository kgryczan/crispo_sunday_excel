import pandas as pd

path = "files/Excel Challenge October 20th.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=14)
test = pd.read_excel(path, usecols="E:F", skiprows=1, nrows=3).rename(columns=lambda x: x.replace(".1", ""))

input['diff1'] = (input['Units'].shift(1)-input['Units'])<0
input['diff2'] = (input['Units'].shift(2)-input['Units'].shift(1))<0
input['diff3'] = (input['Units'].shift(3)-input['Units'].shift(2))<0 

input = input[input[['diff1', 'diff2', 'diff3']].all(axis=1)].reset_index(drop=True)[['Date', 'Units']]

print(input.equals(test)) # True