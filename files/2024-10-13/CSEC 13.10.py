import pandas as pd

path = "files/Excel Challenge October 13th.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=15)
test = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=15).rename(columns=lambda x: x.replace('.1', ''))

input['Date'] = input['Date'].ffill()
input['open'] = input.groupby('Date')['Units'].transform('first')
input['Units'] = input.apply(lambda row: row['open'] + row['Units'] if pd.isna(row['Instance']) else row['Units'], axis=1)

result = input[['Date', 'Units']]

print(result.equals(test))  # True