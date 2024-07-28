import pandas as pd

path = "files/Excel Challange 28th July.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=2, dtype=str)
test = pd.read_excel(path, usecols="F:J", skiprows=2, nrows=3, dtype=str)
test.columns = ["Student", "t1", "t2", "t3", "t4"]
test = test.sort_values(by="Student").reset_index(drop=True)

result = input.pivot(index="Student", columns="Test", values="Result").fillna("exempt").reset_index()
result.columns.name = None

print(result.equals(test)) # True
