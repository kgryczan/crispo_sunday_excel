import pandas as pd

path = "files/Excel Challenge October 6th.xlsx"

input1 = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=3).assign(id=1)
input2 = pd.read_excel(path, usecols="E", skiprows=1, nrows=4).assign(id=1)
test = pd.read_excel(path, usecols="G:I", skiprows=1, nrows=13).rename(columns=lambda x: x.replace('.1', ''))
result = pd.merge(input1, input2, on="id", how="outer")[['Staff', 'PPE', 'Size']]
print(result.equals(test)) # True