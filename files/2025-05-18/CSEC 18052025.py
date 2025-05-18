import pandas as pd

path = "files/2025-05-18/Challenge24.xlsx"
start, end, skip, repetition = 2, 7, 4, 3
test = pd.read_excel(path, usecols="G", skiprows=2, nrows=16)

lst = [i for i in range(start, end+1) if i != skip] * repetition
result = pd.DataFrame({'List': sorted(lst)})

print(result.equals(test))