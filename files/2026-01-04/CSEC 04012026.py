import pandas as pd

path = "2026-01-04/Challenge 89.xlsx"

input1 = pd.read_excel(path, usecols="B:C", skiprows=3, nrows=2)
input2 = pd.read_excel(path, usecols="B:C", skiprows=8, nrows=2)
test = pd.read_excel(path, usecols="F:G", skiprows=3, nrows=8, header=None, dtype=str)

test.columns = [0, 1]
input1['Pages'] = input1['Pages'].astype(str)

result = input1.merge(input2, how="cross")[["Chapter", "Pages", "Section", "Part"]].to_numpy().reshape(-1, 2)

out = pd.DataFrame(result, columns=[0, 1]).reset_index(drop=True)
test = test.reset_index(drop=True)

print(out.equals(test))  # True
