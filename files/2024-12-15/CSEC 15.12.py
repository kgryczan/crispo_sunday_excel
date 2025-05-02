import pandas as pd
from itertools import accumulate

path = "files/Excel Challenge 15th Dec.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="E", skiprows=1, nrows=7)

input['Debt'] = input['Expense'] - input['Daily Budget']
input['Cumulative_Debt'] = list(accumulate(input['Debt'], lambda cum, debt: max(cum + debt, 0)))

print(input['Cumulative_Debt'].equals(test['Cumulative Debt'])) # True