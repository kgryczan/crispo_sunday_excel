import pandas as pd

path = "files/2025-06-22/Challenge 36.xlsx"
input = pd.read_excel(path, usecols="B:C", skiprows=2, nrows=4)
test = (
    pd.read_excel(path, usecols="E:F", skiprows=2, nrows=8)
      .rename(columns=lambda col: col.replace('.1', ''))
)

result = (
    input
    .assign(Student=input['Students'].str.split(', '))
    .explode('Student')
    .reset_index(drop=True)
    [['Student', 'Subject']]
)

print(result.equals(test))
