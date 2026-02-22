import pandas as pd
import numpy as np

path = "2026-02-22/Challenge 104.xlsx"
input = pd.read_excel(path, sheet_name="Sheet3", usecols="B:O", skiprows=2, nrows=22)
test = pd.read_excel(path, sheet_name="Sheet3", usecols="Q:X", skiprows=7, nrows=4)

result = input[input.apply(lambda x: x.count(), axis=1) > 1]
result.columns = result.iloc[0]
result = result[1:].reset_index(drop=True)
result = result.dropna(axis=1, how='all')
result = result.groupby(result.index // 2).agg(lambda x: ' '.join(x.dropna().astype(str)))
result.columns = test.columns
for col in ['Hours', 'Sessions', 'Cost']:
    if col in result.columns:
        nums = pd.to_numeric(result[col].astype(str).str.extract(r'(-?\d+\.?\d*)')[0], errors='coerce')
        nums = nums.round(0)           
        result[col] = nums.astype('int64')
if 'Date' in result.columns:
            result['Date'] = pd.to_datetime(result['Date'], errors='coerce')
print(result.equals(test))