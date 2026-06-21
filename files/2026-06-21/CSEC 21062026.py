import pandas as pd

path = "2026-06-21/Challenge-Jun21.xlsx"
input1 = pd.read_excel(path, usecols="B:D", nrows=8, skiprows=2)
input2 = pd.read_excel(path, usecols="G:L", nrows=15, skiprows=2)
test = pd.read_excel(path, usecols="E", nrows=7, skiprows=2)

input2_long = input2.melt(id_vars="Grades", var_name="year", value_name="value")

result = (
    input1.merge(input2_long, left_on="Job Grade ", right_on="Grades", how="left")
    .assign(
        **{
            "Range Difference": lambda df: df.groupby("Job Grade ")["value"].transform(
                lambda x: x.diff().fillna(0)
            )
        }
    )
    .loc[lambda df: df["Salary"] <= df["value"]]
    .groupby("Job Grade ", sort=False)
    .first()
    .reset_index()[["Range Difference"]]
    .astype("int64")
)

print(result.equals(test))
# True
