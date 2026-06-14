import pandas as pd
import calendar

path = "2026-06-14/Challenge 140.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=7, skiprows=1)
test = pd.read_excel(path, usecols="E:F", nrows=2, skiprows=1).rename(
    columns=lambda c: c.replace(".1", "")
)

month_abb = list(calendar.month_abbr[1:])
month_map = {m: i + 1 for i, m in enumerate(month_abb)}
input_m = input.assign(Month=input["Month"].map(month_map))
result = (
    input_m[["Customer", "Month"]]
    .drop_duplicates()
    .assign(Month=lambda df: df["Month"] + 1)
    .merge(
        input_m[["Customer", "Month"]],
        on=["Customer", "Month"],
        how="left",
        indicator=True,
    )
    .loc[lambda df: df["_merge"] == "left_only", ["Customer", "Month"]]
)
max_month = input["Month"].map(month_map).max(skipna=True)
result = (
    result.loc[result["Month"] <= max_month]
    .assign(
        Month=lambda df: df["Month"].apply(
            lambda m: month_abb[int(m) - 1] if pd.notna(m) else pd.NA
        ),
        **{"Customer Lost": lambda df: df["Customer"]},
    )[["Month", "Customer Lost"]]
    .reset_index(drop=True)
)
print(result.equals(test))
# True
