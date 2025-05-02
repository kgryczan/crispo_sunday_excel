import pandas as pd
from pandas.tseries.offsets import MonthEnd

input = pd.read_excel("files/Excel Challenge 5th May.xlsx", sheet_name="Sheet1", header=1, usecols="B:D")

input['Month'] = pd.to_datetime(input['Date']).dt.to_period('M').dt.to_timestamp() 
input['quarter'] = input['Month'].dt.quarter
input['year'] = input['Date'].dt.year

result = input.groupby(['year', 'Month', 'quarter']).agg({'Man Hour': 'sum', 'LTI Recorded': 'sum'}).reset_index()
result['valid'] = result['LTI Recorded'].gt(0).astype(int)
result['valid'] = result.groupby(['year', 'quarter'])['valid'].transform('all').astype(int)
result = result[["year", "quarter", "valid"]].drop_duplicates()
result = result.agg({'valid': 'sum'}).reset_index()

print(result) # 3