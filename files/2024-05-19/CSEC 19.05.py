import pandas as pd

input = pd.read_excel("files/Excel Challenge 19th May.xlsx", usecols="B:E", skiprows=1, nrows=10)
test = pd.read_excel("files/Excel Challenge 19th May.xlsx", usecols= "G", skiprows=1, nrows=4)

result = input.assign(Combined=input.iloc[:, 1:4].apply(lambda x: ', '.join(sorted(x.dropna())), axis=1))
result = result.assign(n=result.groupby('Combined')['Combined'].transform('size')).query('n == 1').loc[:, ['Product']].reset_index(drop=True)
result.columns = ['Products']

print(result.equals(test))