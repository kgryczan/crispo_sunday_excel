import pandas as pd

path = "files/2025-07-13/Challenge 39.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=10)
test = pd.read_excel(path, usecols="H:I", skiprows=1, nrows=10).rename(columns=lambda c: c.replace('.1', ''))

result = (
    input
    .sort_values(['Product', 'Date'])
    .assign(Product=lambda df: df['Product'].where(df.groupby('Product').cumcount() == 0))
    .drop(columns=['Date'])
    .reset_index(drop=True)
)

print(result.equals(test)) # True