import pandas as pd

path = "files/Ex-Challenge 08 2025.xlsx"
input = pd.read_excel(path, usecols="B:E", skiprows=1, nrows=3)
test = pd.read_excel(path, usecols="G:J", skiprows=1, nrows=6).rename(columns=lambda x: x.replace('.1', ''))

input[['Service', 'Rating']] = input[['Service', 'Rating']].apply(lambda x: x.str.split('\n').fillna(x))
input = input.explode(['Service', 'Rating']).reset_index(drop=True)
input['Rating'] = input['Rating'].astype('float64')

print(input.equals(test)) #True