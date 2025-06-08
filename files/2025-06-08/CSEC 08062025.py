import pandas as pd

path = "files/2025-06-08/Challenge 31.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=2, nrows=7)
test = pd.read_excel(path, usecols="F:G", skiprows=2, nrows=2)

df = input.melt(id_vars=input.columns[0], var_name="Store", value_name="Fruit Sale")
df["count"] = 1
grouped = df.groupby(["Store", "Fruit Sale"], dropna=False, as_index=False)["count"].sum()
grouped["Fruits Sale"] = grouped["Fruit Sale"].astype(str) + ": " + grouped["count"].astype(str)
result = grouped.groupby("Store", as_index=False)["Fruits Sale"].apply(lambda x: ", ".join(x)).reset_index(drop=True)

print(result.equals(test))
# Semantically result the same, different order of fruits.