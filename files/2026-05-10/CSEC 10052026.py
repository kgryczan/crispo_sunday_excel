import pandas as pd

path = "2026-05-10/Challenge 120.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=5, skiprows=2)
test = pd.read_excel(path, usecols="F:H", nrows=5, skiprows=2).rename(columns=lambda c: c.replace(".1", ""))

result = input[["Employee", "Start Date", "End Date"]].assign(
	**{"Start Date": lambda d: pd.to_datetime(d["Start Date"]), "End Date": lambda d: pd.to_datetime(d["End Date"])}
)

ov = result.rename(columns={"Employee": "Employee_1", "Start Date": "start_1", "End Date": "end_1"}).merge(
	result.rename(columns={"Employee": "Employee_2", "Start Date": "start_2", "End Date": "end_2"}), how="cross"
).query("Employee_1 != Employee_2 and start_1 <= end_2 and start_2 <= end_1")

exp = ov.assign(
    dates=ov.apply(lambda r: pd.date_range(max(r.start_1, r.start_2), min(r.end_1, r.end_2), freq="D"), axis=1)
)[["Employee_1", "Employee_2", "dates"]].explode("dates")

def format_dates(s):
    dt = pd.Series(pd.to_datetime(pd.unique(s))).dropna().sort_values()
    return ", ".join(f"{d.month}/{d.day}/{d.year}" for d in dt)

summary = exp.groupby("Employee_1", sort=False).agg(
    Overlaps=("Employee_2", lambda s: ", ".join(pd.unique(s))),
    **{"Date(s)": ("dates", format_dates)},
).reset_index().rename(columns={"Employee_1": "Employee"})

order_map = {n: i for i, n in enumerate(["Aiden", "Bob", "Aditya", "Doris"])}
overlap_pairs = result[["Employee"]].drop_duplicates().merge(summary, on="Employee", how="left").sort_values(
	"Employee", key=lambda s: s.map(order_map).fillna(len(order_map))
).reset_index(drop=True)

print(overlap_pairs.equals(test))