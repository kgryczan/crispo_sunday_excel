import pandas as pd
import re

path = "Excel Challenge 2nd June.xlsx"
input_data = pd.read_excel(path, usecols="C", skiprows=1, nrows=7)
test = pd.read_excel(path, usecols="D", skiprows=1, nrows=7)

def tail_after_last_letter(text):
    matches = list(re.finditer(r"[A-Za-z]", str(text)))
    if not matches:
        return None
    last_pos = matches[-1].end()
    return text[last_pos:] if last_pos < len(text) else None

result = input_data.assign(answer=input_data["Customers & Orders"].map(tail_after_last_letter))
print(result["answer"].equals(test["Last Correct Order"]))
