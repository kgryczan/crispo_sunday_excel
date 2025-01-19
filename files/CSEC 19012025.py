import pandas as pd

path = "files/Ex-Challenge 03 2025.xlsx"
input = pd.read_excel(path, usecols="B:H", skiprows=2, nrows=9, names=['Shop', 'Fruit.1', 'Sale.1', 'Fruit.2', 'Sale.2', 'Fruit.3', 'Sale.3'])
test = pd.read_excel(path, usecols="J:L", skiprows=2, nrows=15)

result = pd.concat([input.iloc[:, [0, i, i+1]] for i in range(1, 6, 2)]).reset_index(drop=True)
result['Fruit'] = result[['Fruit.1', 'Fruit.2', 'Fruit.3']].bfill(axis=1).iloc[:, 0]
result['Sale'] = result[['Sale.1', 'Sale.2', 'Sale.3']].bfill(axis=1).iloc[:, 0]
result = result[['Shop', 'Fruit', 'Sale']]

summary = result.groupby(['Shop', 'Fruit'], as_index=False)['Sale'].sum()
summary = summary.pivot(index='Shop', columns='Fruit', values='Sale').fillna(0).reset_index()
summary = summary.melt(id_vars='Shop', var_name='Fruit', value_name='Sale')
summary['Sale'] = summary['Sale'].astype(int)
summary = summary.sort_values(['Shop', 'Sale'], ascending=[True, False]).reset_index(drop=True)

test.columns = summary.columns
test = test.sort_values(['Shop', 'Sale'], ascending=[True, False]).reset_index(drop=True)

print(all(summary == test))  # True
