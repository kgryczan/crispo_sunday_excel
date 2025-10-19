import pandas as pd
import math

path = "files/2025-10-19/Challenge 71.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=5)
test = pd.read_excel(path, usecols="E:M", skiprows=1, nrows=5).rename(columns=lambda col: col.replace('.1', ''))

def make_weekly_table(input, no_weeks=15, interval=6):
    no_intervals = math.ceil(no_weeks / interval)
    result = pd.DataFrame({'Item': input['Item']})
    prices = input['Prices'].values

    for i in range(1, no_intervals + 1):
        start = (i - 1) * interval + 1
        end = min(i * interval, no_weeks)
        week_cols = {}
        for wk in range(start, end + 1):
            week_cols[f'WK {wk}'] = prices
        week = pd.DataFrame(week_cols)
        result = pd.concat([result, week], axis=1)
        if end < no_weeks:
            result[f'TOTAL {i}'] = result.loc[:, [f'WK {wk}' for wk in range(start, end + 1)]].sum(axis=1)

    result['GRAND TOTAL'] = result.loc[:, [f'WK {wk}' for wk in range(1, no_weeks + 1)]].sum(axis=1)
    return result

output = make_weekly_table(input, no_weeks=6, interval=3)

print(output.equals(test)) # True