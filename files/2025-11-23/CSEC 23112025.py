import pandas as pd

input = pd.read_excel("2025-11-23/Challenge 80.xlsx", usecols="B:C", skiprows=2, nrows=11)
test = pd.read_excel("2025-11-23/Challenge 80.xlsx", usecols="E:F", skiprows=2, nrows=11).rename(columns=lambda c: c.replace('.1', ''))

input["val2"] = input["Value"].where(input["Criteria"], pd.NA).bfill().astype(float).fillna(0)
input["val3"] = input.apply(lambda r: 0 if r["Criteria"] else r["Value"] + r["val2"], axis=1)
result = input[["Criteria", "val3"]].rename(columns={"val3": "Value"})
result["Value"] = result["Value"].astype(int)

print(result.equals(test)) # True