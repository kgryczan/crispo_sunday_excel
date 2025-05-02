import pandas as pd

path = "files/Ex-Challenge 05 2025.xlsx"
input = pd.read_excel(path, usecols="B:I", skiprows=1, nrows=5)
test = pd.read_excel(path, usecols="K:M", skiprows=1, nrows=20)\
    .rename(columns=lambda x: x.replace('.1', ''))\
    .sort_values(by=['Patient', 'Appointments']).reset_index(drop=True)

input_piv = input.melt(id_vars=input.columns[:2], var_name="Appointments", value_name="value")
input_piv = input_piv.dropna()
input_piv = input_piv[input_piv['value'] >= 0]
input_piv = input_piv.loc[input_piv.index.repeat(input_piv['value'])].reset_index(drop=True)
input_piv = input_piv.drop(columns=['value'])
input_piv = input_piv.sort_values(by=['Patient', 'Appointments']).reset_index(drop=True)

print(input_piv.equals(test)) # True