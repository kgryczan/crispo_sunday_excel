import pandas as pd

path = "2026-05-17/Challenge 121.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=13, skiprows=2)
test = pd.read_excel(path, usecols="E:F", nrows=3, skiprows=2)

input["Attendance"] = pd.to_datetime(input["Attendance"])

out = (
    pd.MultiIndex.from_product(
        [pd.date_range(input.Attendance.min(), input.Attendance.max(), freq="B"),
         input.Employee.unique()],
        names=["Date", "Employee"]
    )
    .to_frame(index=False)
    .merge(input.assign(k=1), left_on=["Date", "Employee"],
           right_on=["Attendance", "Employee"], how="left")
    .sort_values(["Employee", "Date"])
    .assign(g=lambda x: x.k.isna().groupby(x.Employee).cumsum())
    .dropna(subset="k")
    .groupby(["Employee", "g"])
    .size()
    .reset_index(name="gsize")
    .assign(gsize=lambda x: x.gsize.where(x.gsize > 1, 0))
    .groupby("Employee", as_index=False)["gsize"]
    .max()
    .rename(columns={"gsize": "Consecutive Streak"})
)
print(out["Consecutive Streak"].equals(test["Consecutive Streak (Work days)"]))
# True