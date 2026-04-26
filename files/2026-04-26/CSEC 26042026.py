import pandas as pd

path = "2026-04-26/Challenge 114.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=6, skiprows=2)
input2 = pd.read_excel(path, usecols="B:C", nrows=3, skiprows=9)
test = pd.read_excel(path, usecols="F:H", nrows=6, skiprows=2).rename(columns=lambda c: c.replace(".1", ""))

df = (
    input.merge(input2, on="Customer")
    .sort_values(["Customer", "Invoice"])
)
df["cum"] = df.groupby("Customer")["Amount"].cumsum().astype("int64")
df["prev"] = df.groupby("Customer")["cum"].shift(fill_value=0).astype("int64")
df["Allocated"] = (df["Payment"] - df["prev"]).clip(lower=0).clip(upper=df["Amount"]).astype("int64")
df["Remaining"] = (df["Amount"] - df["Allocated"]).astype("int64")
result = df[["Invoice", "Allocated", "Remaining"]]

print(result.equals(test))
# True