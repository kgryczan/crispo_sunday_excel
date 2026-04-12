import pandas as pd

path = "2026-04-12/Challenge 112.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=5).rename(columns=lambda c: c.strip() if isinstance(c, str) else c)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=5).rename(columns=lambda c: c.strip() if isinstance(c, str) else c)

result = (
	input
	.assign(rn=lambda d: range(1, len(d) + 1))
	.assign(Name=lambda d: d["Name"].astype(str).str.split(" "))
	.explode("Name")
	.assign(
		label=lambda d: d["Name"].str.fullmatch(r"[A-Z]+", na=False).map(
			{True: "First Name", False: "Other Names"}
		)
	)
	.groupby(["rn", "label"], as_index=False)["Name"]
	.agg(" ".join)
	.pivot(index="rn", columns="label", values="Name")
	.reset_index(drop=True)
	.reindex(columns=["First Name", "Other Names"])
)
result.columns.name = None

print(result.equals(test))
# True