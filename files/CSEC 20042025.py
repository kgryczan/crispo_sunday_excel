import pandas as pd

path = "files/Challenge15-2025.xlsx"
input = pd.read_excel(path, usecols="B:G", skiprows=2, nrows=2)
test = pd.read_excel(path, usecols="I:K", skiprows=2, nrows=10)

input = input.fillna(0)
result = (
    input.rename(columns={input.columns[0]: "product"})
    .melt(id_vars="product", var_name="month", value_name="sales")
    .ffill()
)

month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
result["month"] = pd.Categorical(result["month"], categories=month_order, ordered=True)
result = (
    result.dropna()
    .sort_values(["product", "month"])
    .reset_index(drop=True)
    .assign(diff=lambda df: df.groupby("product")["sales"].diff())
    .query("diff > 0")
    .loc[lambda df: df.index.repeat(df["diff"].astype(int))]
    .assign(Req=1)
    .drop(columns=["sales", "diff"])
    .reset_index(drop=True)
)
result["month"] = result["month"].astype(str)
result.columns = test.columns

print(result.equals(test)) # True
