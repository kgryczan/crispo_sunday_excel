import pandas as pd
import numpy as np

path = "files/Challenge1025.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=2, nrows=9)
test = pd.read_excel(path, usecols="F:G", skiprows=2, nrows=6).rename(columns=lambda x: x.replace('.1', ''))

step = 5
min_qty = np.floor(input["Qty"].min() / step) * step
max_qty = np.ceil(input["Qty"].max() / step) * step
breaks = np.arange(min_qty, max_qty + step, step)
labels = [f"{int(breaks[i-1] + 1)}-{int(breaks[i])}" for i in range(1, len(breaks))]

input["Qty_group"] = pd.cut(input["Qty"], bins=breaks, labels=labels, right=True, include_lowest=True)
result = input.groupby("Qty_group", observed=True)["Amount"].sum().reset_index()
result.rename(columns={"Qty_group": "Qty Group"}, inplace=True)
all_groups = pd.DataFrame({"Qty Group": labels})
r2 = pd.merge(all_groups, result, on="Qty Group", how="left")
r2["Amount"] = r2["Amount"].fillna(0)
r2["Amount"] = r2["Amount"].astype("int64")

print(test.equals(r2)) # True