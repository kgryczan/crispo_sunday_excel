import pandas as pd

path = "2026-07-19/Challenge 400.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=9, skiprows=2)
test = pd.read_excel(path, usecols="E:F", nrows=3, skiprows=2)
test.columns = ["Stock Out Days", "Days Out"]

stock_is_zero = input["Stock Bal"].eq(0)
run_id = stock_is_zero.ne(stock_is_zero.shift()).cumsum()

rows = []
for _, run in input[stock_is_zero].groupby(run_id[stock_is_zero]):
    rows.append([run["Date"].iloc[0], len(run)])

result = pd.DataFrame(rows, columns=["Stock Out Days", "Days Out"])
print(result.equals(test))
