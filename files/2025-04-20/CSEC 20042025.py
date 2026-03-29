import pandas as pd

path = "Challenge15-2025.xlsx"
input_data = pd.read_excel(path, usecols="B:G", skiprows=2, nrows=3)
test = pd.read_excel(path, usecols="I:K", skiprows=2, nrows=11)

result = (
    input_data.rename(columns={input_data.columns[0]: "product"})
    .melt(id_vars="product", var_name="month", value_name="sales")
    .sort_values(["product", "month"])
)
result["sales"] = result.groupby("product")["sales"].ffill()
result["m_diff"] = result.groupby("product")["sales"].diff().fillna(0)
result = result.loc[result["m_diff"] > 0, ["product", "month", "m_diff"]]
result = result.loc[result.index.repeat(result["m_diff"].astype(int))].reset_index(drop=True)
result["Required"] = 1
result.columns = test.columns

print(result.equals(test))
