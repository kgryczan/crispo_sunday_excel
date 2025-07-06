import pandas as pd

path = "files/2025-07-06/Challenge 38.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=10)
test = pd.read_excel(path, usecols="F:H", skiprows=1, nrows=6).rename(columns=lambda col: col.replace('.1', ''))

result = (
    input.groupby(['Date', 'Store'], as_index=False)
    .agg(n=('Product', 'nunique'))
)
result['Product'] = result.groupby('Store')['n'].shift(1, fill_value=0)
result = result[['Date', 'Store', 'Product']]

print(result.equals(test))
