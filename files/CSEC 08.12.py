import pandas as pd

path = "files/Excel Challenge Dec 8th.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=10)
test = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=4)
test.columns = ["Airline", "Whole Route"]

pivot_wider = input.pivot(index='Airline', columns='Numb', values='Route')
pivot_longer = pd.melt(pivot_wider.reset_index(), id_vars=['Airline'], value_vars=pivot_wider.columns, var_name='Numb', value_name='Route')
pivot_longer = pivot_longer.sort_values(['Airline', 'Numb'])
pivot_longer = pivot_longer.dropna()

pivot_longer['Route'] = pivot_longer.apply(lambda row: row['Route'] if row['Numb'] == 1 else (row['Route'].split('-')[1] if len(row['Route'].split('-')) > 1 else row['Route']), axis=1)

result = pivot_longer.groupby('Airline')['Route'].apply(lambda x: ' -'.join(x)).reset_index()
result.columns = ["Airline", "Whole Route"]

print(result.equals(test)) # True