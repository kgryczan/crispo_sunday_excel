import pandas as pd
from itertools import chain

path = "2026-03-22/Challenge 108.xlsx"
input1 = pd.read_excel(path, usecols="B", nrows = 2, skiprows = 1).iloc[:, 0].tolist()
input2 = pd.read_excel(path, usecols="B", nrows = 3, skiprows = 5).iloc[:, 0].tolist()
test = pd.read_excel(path, usecols="D", nrows = 13, skiprows = 1)

result = list(chain.from_iterable((a, b) for b in input2 for a in input1))

print(result == test.values.flatten().tolist())
## [1] TRUE