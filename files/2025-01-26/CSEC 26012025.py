import pandas as pd

path = "files/Ex-Challenge 04 2025.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=2, nrows=15)
test = pd.read_excel(path, usecols="F:G", skiprows=2, nrows=10)

result = input.assign(Rank=input['Demand'].rank(method='dense', ascending=False).astype(int)) \
              .groupby('Rank')['Fruit'].agg(' ; '.join) \
              .reset_index() \
              .sort_values(by='Rank')

