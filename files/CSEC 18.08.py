import pandas as pd
import numpy as np

path = "files/Excel Challenge 18th August.xlsx"
input = pd.read_excel(path, usecols = 'B:D', skiprows=1, nrows = 4)

def generate_dates(start_date, n):
    dates = pd.date_range(start=start_date, periods=n*2, freq='D')
    return dates

result = input.assign(dates=input.apply(lambda row: generate_dates(row['Start'], row['Days']), axis=1)) \
    .explode('dates') \
    .set_index('dates') \
    .drop(columns=['Start']) \
    .reset_index() \
    .assign(wday=lambda df: np.where(df['dates'].dt.dayofweek.isin([5, 6]), '', 'X'),
            wday_lab=lambda df: df['dates'].dt.dayofweek,
            dates=lambda df: df['dates'].dt.strftime('%m-%d'),
            nrow=lambda df: df.groupby(['Project', 'wday']).cumcount() + 1)\
    .assign(wday = lambda df: np.where((df['wday_lab'] == 5) | (df['wday_lab'] == 6) | (df["nrow"] > df['Days']),'', 'X')) \
    .pivot(index='Project', columns='dates', values='wday') \
    .fillna('')

result = result.iloc[:, :-5]
print(result)

# dates   08-16 08-17 08-18 08-19 08-20 08-21 08-22 08-23 08-24 08-25 08-26 08-27 08-28
# Project
# A           X                 X     X     X     X
# B                                   X     X     X     X                 X
# C                                               X     X                 X
# D           X                 X     X     X     X     X                 X     X     X