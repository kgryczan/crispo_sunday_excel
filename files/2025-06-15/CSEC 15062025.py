import pandas as pd
import re

# Read data from Excel
path = "files/2025-06-15/Challenge 35.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=9)
test = pd.read_excel(path, usecols="D:E", skiprows=2, nrows=1)

input['vowel_count'] = input.iloc[:,0].astype(str).apply(lambda name: sum(1 for c in name if c.lower() in 'aeiou'))
input['title'] = input['vowel_count'].apply(lambda vowels: "No Vowel" if vowels == 0 else ("All Vowels" if vowels == 5 else "Some Vowels"))
filtered = input[input['title'] != "Some Vowels"]

pivoted = filtered.value_counts('title').reindex(["No Vowel", "All Vowels"], fill_value=0).to_frame().T
pivoted.columns.name = None
pivoted.reset_index(drop=True, inplace=True)

print(pivoted.equals(test)) # True