import pandas as pd

path = "2026-02-15/Challenge 103.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=12)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=12)

c = input.groupby("Invoice").cumcount()
result = pd.DataFrame({
    "Suffixed Invoice": input["Invoice"].where(
        c.eq(0),
        input["Invoice"] + "_D" +
        input["Invoice"].str.extract(r"(\d+)")[0] +
        "-" + c.astype(str)
    )
})

print(result.equals(test))
# Inconsitent second delim in test data, but otherwise correct.
