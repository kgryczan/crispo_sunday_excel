import pandas as pd

path = 'files/Excel Challenge  22nd June.xlsx'
input = pd.read_excel(path, skiprows = 1, usecols= "B")
test  = pd.read_excel(path, skiprows = 1, usecols= "D", nrows = 3)

input = pd.concat([input.iloc[::2].reset_index(drop=True), input.iloc[1::2].reset_index(drop=True)], axis=1)
input.columns = ['Dates', 'Values']
filtered_data = input[input['Values'] < input['Values'].shift()]
result = filtered_data[['Dates']].astype("datetime64[ns]").reset_index(drop=True)

print(result.equals(test)) # True