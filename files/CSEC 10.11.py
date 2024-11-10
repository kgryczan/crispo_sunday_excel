import pandas as pd

path = "files/Excel Challenge Nov 10th.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=14)

input['change'] = input['Items'].ne(input['Items'].shift()).fillna(True)
print(input)