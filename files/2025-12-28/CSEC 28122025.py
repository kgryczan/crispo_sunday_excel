import pandas as pd

path = "2025-12-28/Challenge 88.xlsx"

inp = pd.read_excel(path, usecols="B:D", skiprows=2, nrows=6)
tst = pd.read_excel(path, usecols="F:K", skiprows=2, nrows=6)

res = (
    inp.assign(
        Shifts=lambda d: d.Shifts.str.replace(
            r"(?<=\D)(?=\d)|(?<=\d)(?=\D)", "|", regex=True
        )
    )["Shifts"]
    .str.split("|", expand=True)
)
res.columns = tst.columns
res.iloc[:, [1, 3, 5]] = res.iloc[:, [1, 3, 5]].astype(float)

print(((res.values == tst.values) | (pd.isna(res) & pd.isna(tst))).all())