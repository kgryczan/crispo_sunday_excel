import pandas as pd

path = "files/2025-08-24/Challenge 52.xlsx"

input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=6, dtype = str)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=6).rename(columns=lambda c: c.replace('.1', '')).assign(**{"Missing Data": lambda df: df["Missing Data"].fillna("")})

input["Customer"] = input["Customer"].astype("category")

long = input.melt(id_vars="Customer", var_name="Var", value_name="val")
long["val"] = long["val"].astype(str)
long.loc[long["val"] == "nan", "val"] = None
long["missing"] = long.apply(lambda row: row["Var"] if pd.isna(row["val"]) else None, axis=1)

result = (
    long.groupby("Customer")["missing"]
    .apply(lambda x: ", ".join([v for v in x if pd.notna(v)]))
    .reset_index()
    .rename(columns={"missing": "Missing Data"})
)

result["Customer"] = result["Customer"].astype(str)

print(result.equals(test))