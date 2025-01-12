import pandas as pd

path = "files/Ex-Challenge 02 2025.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=12)
test = pd.read_excel(path, usecols="E:F", skiprows=1, nrows=5)

input['Month'] = input['Date'].dt.strftime('%B')
input['M'] = input['Date'].dt.month
input['D'] = input['Date'].dt.day

result = (input.sort_values(['M', 'D'])
          .groupby('M')
          .agg(Month=('Month', 'first'),
               Customers=('Customer', ','.join))
          .reset_index(drop=True))

print(result.equals(test))
# True