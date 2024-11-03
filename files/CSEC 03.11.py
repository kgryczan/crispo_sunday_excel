import pandas as pd
from pandas.tseries.offsets import MonthEnd

path = "files/Excel Challenge Nov 3rd.xlsx"
input = pd.read_excel(path, usecols="B:I", skiprows=2, nrows=6)
test = pd.read_excel(path, usecols="K:M", skiprows=2, nrows=12).rename(columns=lambda x: x.replace('.1', ''))

input = input.melt(id_vars=input.columns[0], var_name="Month", value_name="HC")
input["HC"] = input["HC"].fillna(0)
input["Month"] = pd.to_datetime(input["Month"], format='%b-%y') + MonthEnd(0)
input["Hire"] = input.groupby("Position")["HC"].diff().fillna(input["HC"]).astype(int)
result = input[input["Hire"] > 0].drop(columns=["HC"]).sort_values(by=["Position", "Month"]).reset_index(drop=True)

print(result.equals(test))  # False, one value mistaken in challenge.