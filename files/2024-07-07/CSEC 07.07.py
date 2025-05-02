import pandas as pd
import numpy as np

path = "files/Excel Challenge  7th July.xlsx"

input = pd.read_excel(path, usecols="B", skiprows = 2, nrows = 17)
test  = pd.read_excel(path, usecols="D", skiprows = 2, nrows = 5)

result = np.where((input["SALES"].shift() == "NEW ORDER") | (input["SALES"].shift(-1) == "NEW ORDER"), 1, 0)
result = input[result == 1].reset_index(drop=True)
result["SALES"] = result["SALES"].astype("datetime64[ns]")

print(result["SALES"].equals(test["Before & After Dates"])) # True