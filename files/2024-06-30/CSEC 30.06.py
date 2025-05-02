import pandas as pd

path = "files/Excel Challenge  30th June.xlsx"

input = pd.read_excel(path, usecols="B:D", skiprows=2, nrows=4)
test = pd.read_excel(path, usecols="E:I", skiprows=2, nrows=4).fillna(0).astype(int)

result = input.copy()
result['seq'] = result.apply(lambda x: pd.date_range(start=x["Start Date "], end=x["End Date"], freq='M'), axis=1)
result = result.explode('seq')
result['year'] = result['seq'].dt.year
result['val'] = 1
result = result[['Project', 'year', 'val']].\
    pivot_table(index='Project', columns='year', values='val', aggfunc='sum').\
    fillna(0).astype(int)
result = result.reset_index().drop(columns='Project')

print(result.equals(test)) # True