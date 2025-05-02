import pandas as pd

path = "files/Ex-Challenge 09 2025.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=5)
test = pd.read_excel(path, usecols="D:F", skiprows=2, nrows=5)

input['Dates'] = input['Dates'].apply(lambda x: x.split()[0][:3] + ' ' + ' '.join(x.split()[1:]))
input['Dates'] = input['Dates'].str.replace('.', '', regex=False)
input['Dates'] = input['Dates'].str.replace('am', 'AM').str.replace('pm', 'PM')

input['Date'] = pd.to_datetime(input['Dates']).dt.date.astype('datetime64[ns]')
input['Day'] = pd.to_datetime(input['Dates']).dt.day_name()
input['Time'] = pd.to_datetime(input['Dates']).dt.time

input = input.drop(columns=['Dates'])

print(input.equals(test)) # True
