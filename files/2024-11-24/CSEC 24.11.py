import pandas as pd
import re

path = "Excel Challenge Nov 24th.xlsx"
input_data = pd.read_excel(path, usecols="B", skiprows=1, nrows=13)

pattern = r"\D+ \d+ \D+ \d+"
result = input_data.assign(cond_form=input_data["Items"].map(lambda x: "" if re.fullmatch(pattern, str(x)) else "Yes"))
print(result)
