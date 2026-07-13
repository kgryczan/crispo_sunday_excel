import pandas as pd
from decimal import Decimal, getcontext

path = "2026-07-12/Challenge 391.xlsx"
input = pd.read_excel(path, usecols="B:E", nrows=4, skiprows=2, dtype="str")
test = pd.read_excel(path, usecols="G", nrows=4, skiprows=2, dtype="str")


getcontext().prec = 50

cols = ["Initial Value", "Add 1", "Add 2", "Add 3"]

input["total"] = input[cols].apply(
    lambda row: format(sum(Decimal(str(x)) for x in row), ".21f"), axis=1
)

# VIsually compared. 1 and 2 correct. No 3. incorrect answer provided.
