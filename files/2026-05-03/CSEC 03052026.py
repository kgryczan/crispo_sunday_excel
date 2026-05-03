import pandas as pd

path = "2026-05-03/Challenge 115.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=7, skiprows=2)
test = pd.read_excel(path, usecols="F:G", nrows=2, skiprows=2).rename(
	columns=lambda c: c.replace(".1", "")
)

result = (
	input.sort_values(["Product", "Date"])
	.assign(diff=lambda d: d.groupby("Product")["Price"].diff())
	.query("diff < 0")
	.drop_duplicates("Product")
	[["Product", "Date"]]
	.rename(columns={"Date": "First Drop Date"})
    .reset_index(drop=True)
)

print(result.equals(test))
# True