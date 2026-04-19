import pandas as pd

path = "2026-04-19/Challenge 113.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=6, skiprows=1)
test = pd.read_excel(path, usecols="E:F", nrows=3, skiprows=1)

result = (
    input.groupby("Customer")
      .apply(lambda x: pd.DataFrame({
          "Date": pd.date_range(x["Date"].min(), x["Date"].max())
      }).assign(Customer=x.name)
      .merge(x := input, on=["Customer","Date"], how="left", indicator=True)
      .query("_merge == 'left_only'")
      .drop(columns="_merge")
      .reset_index(drop=True)
))
result = result[["Customer", "Date"]].rename(columns={"Date": "Missing Date", "Customer": "Customer.1"}).reset_index(drop=True)

print(result.equals(test))
# True