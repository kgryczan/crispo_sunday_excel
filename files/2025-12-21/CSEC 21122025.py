import pandas as pd
import re

path = "2025-12-21/Challenge 87.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=1, nrows=6)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=6)

def extract_city(address):
    match = re.search(r"(?<=\d{5} )[^,]+", str(address))
    return match.group(0) if match else None

input['extracted'] = input.iloc[:, 0].apply(extract_city)

print(input['extracted'].equals(test['City'])) # True
