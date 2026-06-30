import pandas as pd

path = "2026-06-28/Challenge 299.xlsx"
input = pd.read_excel(path, usecols="B:D", nrows=13, skiprows=2)
test = pd.read_excel(path, usecols="F:H", nrows=13, skiprows=2).rename(
    columns=lambda c: c.replace(".1", "")
)
project_start = pd.Timestamp("2026-01-01")

input["Earliest Start"] = pd.NaT
input["Earliest Finish"] = pd.NaT

while input["Earliest Finish"].isna().any():
    for i in input[input["Earliest Finish"].isna()].index:
        parent = input.at[i, "Depends On"]

        if pd.isna(parent) or pd.notna(
            input.loc[input["Task"].eq(parent), "Earliest Finish"].iloc[0]
        ):
            start = (
                project_start
                if pd.isna(parent)
                else input.loc[input["Task"].eq(parent), "Earliest Finish"].iloc[0]
                + pd.Timedelta(days=1)
            )
            input.at[i, "Earliest Start"] = start
            input.at[i, "Earliest Finish"] = start + pd.Timedelta(
                days=input.at[i, "Duration (Days)"] - 1
            )

answer = input[["Task", "Earliest Start", "Earliest Finish"]].copy()

answer["Earliest Start"] = pd.to_datetime(answer["Earliest Start"]).dt.normalize()
answer["Earliest Finish"] = pd.to_datetime(answer["Earliest Finish"]).dt.normalize()

print(answer.equals(test))
# True
