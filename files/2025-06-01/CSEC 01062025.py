import pandas as pd
from datetime import datetime, timedelta

path = "files/2025-06-01/Challenge 30.xlsx"
start_date = pd.to_datetime("2025-05-01")
work_days = 8
travel_days = 8

test = pd.read_excel(path, usecols="F:G", skiprows=2, nrows=21)
test['Schedule'] = pd.to_datetime(test['Schedule'])

dates = pd.date_range(start_date, periods=(work_days + travel_days) * 2)
df = pd.DataFrame({'dates': dates})
df['weekend'] = df['dates'].dt.weekday.isin([5, 6])
df['weekend'] = df['weekend'].map({True: 'Rest', False: 'Work'})
df['work_count'] = df.groupby('weekend').cumcount() + 1

df['work_index'] = None
mask = (df['weekend'] == 'Work') & (df['work_count'] == work_days + 1)
if mask.any():
    idx = df.index[mask][0]
    df.loc[idx:, 'work_index'] = idx
df['work_index'] = df['work_index'].ffill().bfill()

df.loc[df.index >= df['work_index'], 'weekend'] = 'Travel'
df['travel_count'] = df.groupby('weekend').cumcount() + 1
df1 = df[df['travel_count'] <= travel_days][['dates', 'weekend']]
df1.columns = ['Schedule', 'Activity']

print(df1.equals(test))