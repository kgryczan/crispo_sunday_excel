import pandas as pd
import numpy as np

path = "2026-01-25/Challenge 100.xlsx"
input_df = pd.read_excel(path, sheet_name=1, usecols="B", skiprows=2, nrows=3)
multi = pd.read_excel(path, sheet_name=1, usecols="C", skiprows=1, nrows=1, header=None).iloc[0, 0]
test = pd.read_excel(path, sheet_name=1, usecols="E", skiprows=1, nrows=10)

result = input_df.assign(Items=input_df['Items'].map(lambda x: list(np.repeat(x, multi)))).explode('Items').reset_index(drop=True)

print(result['Items'].equals(test['Solution'])) # True