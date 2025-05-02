import pandas as pd
import re

path = "files/Excel Challenge September 29th.xlsx"

input = pd.read_excel(path, usecols="B", skiprows=1, nrows=5)
test = pd.read_excel(path, usecols="D:E", skiprows=1, nrows=5)

date_patt = r'\d{1,2}/\d{1,2}/\d{4}'
amount_patt = r'\d+(?=\s|$)'

input['Date'] = input['Revenues Details'].apply(lambda x: pd.to_datetime(re.search(date_patt, x).group(), format='%m/%d/%Y') if re.search(date_patt, x) else None)
input['Amount'] = input['Revenues Details'].apply(lambda x: re.search(amount_patt, x).group().strip() if re.search(amount_patt, x) else None)
input['Amount'] = input['Amount'].astype('float64')

result = input.iloc[:, 1:]

print(result.equals(test)) # True
