import pandas as pd
import re

path = "files/Challenge1225.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=2, nrows=5)
test = pd.read_excel(path, usecols="E:F", skiprows=2, nrows=5).rename(columns=lambda col: re.sub(r'\.1$', '', col))

input = input.assign(
    Narration=input['Narration'].str.split(r'[,.]')
).explode('Narration').dropna(subset=['Narration'])

input['action'] = input['Narration'].str.extract(r'(sell|sold|buy)', expand=False)
input = input.dropna(subset=['action'])
input['amount'] = input['Narration'].str.extract(r'(\d+)').astype('int64')
input.loc[input['action'] == 'buy', 'amount'] *= -1

result = input.groupby('Items', sort=False)['amount'].sum().rename('Profit (loss)').reset_index()

print(result.equals(test)) # True
