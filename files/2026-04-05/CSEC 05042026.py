import pandas as pd
import numpy as np

path = "2026-04-05/Challenge 110.xlsx"
input1 = pd.read_excel(path, usecols="B", nrows = 1, skiprows = 1).values
input2 = pd.read_excel(path, usecols="C", nrows = 1, skiprows = 1).values
input3 = pd.read_excel(path, usecols="D", nrows = 1, skiprows = 1).values

test1 = pd.read_excel(path, usecols="B", nrows = 18, skiprows = 3).values.flatten()
test2 = pd.read_excel(path, usecols="C", nrows = 18, skiprows = 3).values.flatten()
test3 = pd.read_excel(path, usecols="D", nrows = 18, skiprows = 3).values.flatten()
while test3.size > 0 and np.isnan(test3[-1]):
    test3 = test3[:-1]

def seq(str):
    nums = [int(x) for x in str.split(",")]
    result = []
    for num in nums:
        if num == 0:
            result.append(np.nan)
            result.append(np.nan)
        else:
            result.extend([1] * num)
            result.append(np.nan)
    while result and np.isnan(result[-1]):
        result.pop()
    return result

s1  = seq(input1[0][0])
s2 = seq(input2[0][0])
s3 = seq(input3[0][0])

def equal_with_nan(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    return a.shape == b.shape and np.array_equal(a, b, equal_nan=True)

print(equal_with_nan(s1, test1)) # True
print(equal_with_nan(s2, test2)) # True
print(equal_with_nan(s3, test3)) # True