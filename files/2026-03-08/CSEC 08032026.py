import pandas as pd

path = "2026-03-08/Challenge 106.xlsx"
input_df = pd.read_excel(path, usecols="B:D", skiprows=1, nrows=4)
test = pd.read_excel(path, usecols="F", skiprows=1, nrows=4)

total_days = (input_df["Week"] * 7 + input_df["Days"]) * input_df["Multiply By:"]
input_df["Results"] = total_days.apply(
    lambda d: f"Weeks: {int(d // 7)}   Days: {int(d % 7)}"
)
# correct but number of spaces between "Weeks:" and "Days:" is different, so not exactly the same as test$Results