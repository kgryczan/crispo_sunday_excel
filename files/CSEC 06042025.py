import pandas as pd
import numpy as np

path = "files/Challenge1425.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=2, nrows=21)
test = pd.read_excel(path, usecols="F:H", skiprows=2, nrows=4)

input['Date'] = input['Date'].str.replace("29-02", "27-02", regex=False)
input['Date'] = pd.to_datetime(input['Date'], format='%d-%m-%Y')

date_range = pd.date_range(start=input['Date'].min(), end=input['Date'].max(), freq='D')
seq = pd.DataFrame({'Date': date_range})

seq = seq.merge(input, on='Date', how='left')
seq['Staff No.'] = seq['Staff No.'].ffill()

seq['week'] = seq['Date'].dt.isocalendar().week

summary = (
    seq.groupby(['Staff No.', 'week'])
    .agg(
        **{
            'Total Hours': ('Worked Hours', lambda x: x.sum(skipna=True)),
            'Week Dates': ('Date', lambda x: f"{x.min().strftime('%Y-%m-%d')} - {x.max().strftime('%Y-%m-%d')}")
        }
    )
    .reset_index()
)
summary = summary[['Staff No.', 'Week Dates', 'Total Hours']]