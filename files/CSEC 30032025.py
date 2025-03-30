import pandas as pd
from itertools import product
from datetime import time

path = "files/Challenge1325.xlsx"
input = pd.read_excel(path, sheet_name=0, usecols="B:D", skiprows=2, nrows=17)
test = pd.read_excel(path, sheet_name=0, usecols="F:I", skiprows=2, nrows=14).rename(columns=lambda x: x.replace('.1', ''))

df = pd.DataFrame(product(input['Staff No.'].unique(), input['Date'].unique()), columns=['Staff No.', 'Date'])
df = df.merge(input, on=['Staff No.', 'Date'], how='left')
df = df.sort_values(by=['Staff No.', 'Date', "Time"]).reset_index(drop=True)
df = df.groupby(['Staff No.', 'Date']).apply(lambda group: group.iloc[[0, -1]]).reset_index(drop=True)
df = df.drop_duplicates().reset_index(drop=True)
df['Count'] = df.groupby(['Staff No.', 'Date']).cumcount() + 1
df_pivot = df.pivot(index=['Staff No.', 'Date'], columns='Count', values='Time').reset_index()
df_pivot = df_pivot.sort_values(by=['Date', 'Staff No.']).reset_index(drop=True)
df_pivot.columns = ['Staff No.', 'Date', 'Time In', 'Time Out']

print(df_pivot)