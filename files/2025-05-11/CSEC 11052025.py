import pandas as pd

path = "Challenge 23.xlsx"
input_data = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=27)
test = pd.read_excel(path, usecols="F:G", skiprows=1, nrows=5)
test.columns = ["Quarter", "Production"]

input_data["Date"] = pd.to_datetime(input_data["Date"])
input_data["Quarter"] = "Q" + input_data["Date"].dt.quarter.astype(str)
result = (
    input_data.loc[input_data["Temp (°C)"].between(-10, -5)]
    .groupby("Quarter", as_index=False)["Production (L)"]
    .sum()
    .rename(columns={"Production (L)": "Production"})
)

print(result.equals(test))
