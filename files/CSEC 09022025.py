import pandas as pd

path = "files/Ex-Challenge 06 2025.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=2, nrows=3)
test = pd.read_excel(path, usecols="F:H", skiprows=2, nrows=12).rename(columns=lambda x: x.replace('.1', ''))

input[['start', 'end']] = input['SNo.'].str.split('-', expand=True)
input['start'] = input['start'].fillna(input['SNo.'])
input['end'] = input['end'].fillna(input['SNo.'])

input['start'] = input['start'].fillna(0).astype(int)
input['end'] = input['end'].fillna(input['start']).astype(int)

input['SNo.'] = input.apply(lambda row: list(range(row['start'], row['end']+1)), axis=1)

input = input.explode('SNo.')
result = input[['SNo.', 'Sport', 'Day']].reset_index(drop=True)
result['SNo.'] = result['SNo.'].astype('int64')

print(result.equals(test)) # True
