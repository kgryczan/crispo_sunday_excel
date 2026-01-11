import pandas as pd

path = "2026-01-11/Challenge 90.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=3, nrows=8, dtype={"Item": str})
test = pd.read_excel(path, usecols="F:G", skiprows=3, nrows=5, names=["Item", "Answer"], header=None, dtype={"Item": str})


result = (
    input.groupby("Item", as_index=False)
    .agg(Answer=("Date", lambda x: len(x) if len(x) > 1 else x.iloc[0]))
    .sort_values("Item")
)
print(result.equals(test))
# First answer is not correct.
