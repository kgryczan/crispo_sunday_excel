import pandas as pd

path = "files/Excel Challenge 4th August.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows = 1, nrows = 6)
test = pd.read_excel(path,  usecols="E:F", skiprows = 1, nrows= 3)
test.columns = test.columns.str.replace('.1', '')

result = input.copy()
result['Customers'] = result['Customers'].str.split('; ')
result = result.explode('Customers')
result['Customers'] = result['Customers'].str.strip()
result['count'] = result.groupby(['Customers', 'Date'])['Customers'].transform('count')
result = result[result['count'] > 1].drop_duplicates()
result = result.groupby('Date')['Customers'].apply(lambda x: '; '.join(x)).reset_index(name='Repeat Customers')

print(result.equals(test)) # True