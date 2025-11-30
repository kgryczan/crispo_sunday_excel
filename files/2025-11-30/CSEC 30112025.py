import pandas as pd
import re

path = "2025-11-30/Challenge 81.xlsx"
input = pd.read_excel(path, usecols="B", nrows = 4, skiprows = 2)
test = pd.read_excel(path, usecols="D", nrows=4, skiprows=2).rename(columns=lambda c: c.replace('.1', ''))

def clean_text(s):
    return s if pd.isnull(s) else " ".join(re.sub(r"<.*?>", "", str(s)).replace("&nbsp;", "").split())

result = input.map(clean_text)

print(result.equals(test)) # True