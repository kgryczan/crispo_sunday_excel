import pandas as pd

input = pd.read_excel("files/Excel Challenge 26th May.xlsx", usecols="C:E", skiprows = 1, nrows = 18)
test  = pd.read_excel("files/Excel Challenge 26th May.xlsx", usecols="I:K", skiprows = 1, nrows = 5)

result = input.dropna().tail(5).reset_index(drop=True)
result["Amount"] = result["Amount"].astype("int64")
test.columns = input.columns

print(result.equals(test)) # True