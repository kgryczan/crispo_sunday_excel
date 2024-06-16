import pandas as pd
import numpy as np

path = "files/Excel Challenge 16th June.xlsx"
input = pd.read_excel(path, skiprows=1, usecols="B")
test = pd.read_excel(path, skiprows=1, usecols="D:E", nrows = 3)

result = pd.DataFrame(input.values.reshape(-1, 2), columns=['A', 'B'])
result['month'] = result['A'].dt.month
result = result.groupby('month').tail(1)
result = result[['month', 'B']].reset_index(drop=True)
result = result.astype('int64')

result.columns = test.columns

print(result.equals(test)) # True

