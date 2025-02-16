import pandas as pd

path = "files/Ex-Challenge 07 2025.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=11)
test = pd.read_excel(path, usecols="D", skiprows=2, nrows=15).astype(str)

input['group'] = (input['Staff'].diff() < 0).cumsum() + 1
input['Staff'] = input['Staff'].astype(str)

result = input.groupby('group', group_keys=False).apply(
    lambda x: x._append(pd.DataFrame({'Staff': [f"GROUP {x.name}"]}))
).reset_index(drop=True)[['Staff']].rename(columns={'Staff': 'Groups'})

print(result.equals(test))