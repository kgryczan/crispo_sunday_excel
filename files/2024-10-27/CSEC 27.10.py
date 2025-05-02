import pandas as pd

path = "files/Excel Challenge October 27th.xlsx"
input = pd.read_excel(path, usecols="C:E", skiprows=2, nrows=19)
test = pd.read_excel(path, usecols="G:H", skiprows=2, nrows=5).dropna().rename(columns=lambda x: x.replace('.1', ''))
test['Date'] = pd.to_datetime(test['Date'])

threshold = 800

result = (input[input.groupby('Staff')['Sales'].cumsum() >= threshold]
          .drop_duplicates('Staff')
          .assign(Date=lambda df: pd.to_datetime(df['Date']))
          .loc[:, ['Staff', 'Date']]
          .sort_values(by='Date')
          .reset_index(drop=True))

print(result.equals(test)) # True