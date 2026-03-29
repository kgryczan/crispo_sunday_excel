import re
import pandas as pd

path = "2026-03-29/Challenge 109.xlsx"
input_df = pd.read_excel(path, usecols="B", skiprows=1, nrows=4, engine="openpyxl", names=["Order_Description"])
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=4, engine="openpyxl", names=["Order No."]).fillna("")
test["Order No."] = test["Order No."].str.strip()

pattern = re.compile(r"PRD-[A-Z][0-9]+")

def extract_join(text):
    if pd.isna(text):
        return ""
    matches = pattern.findall(str(text))
    return " ; ".join(matches)

result = input_df.copy()
result["Order No."] = result["Order_Description"].map(extract_join)

print(result["Order No."].equals(test["Order No."]))
# Output: True