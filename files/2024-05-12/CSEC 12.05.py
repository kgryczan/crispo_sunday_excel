import pandas as pd

input = pd.read_excel("files/Excel Challenge 12th May.xlsx", sheet_name="Sheet1", skiprows=2, usecols="B:E")

result = input.melt(id_vars=["Doctors", "Session"], var_name="Day", value_name="Patient")
result["Appointment"] = result["Doctors"] + " - " + result["Session"] + " - " + result["Day"]
result = result.sort_values(by=["Patient", "Appointment"])[["Patient", "Appointment"]].reset_index(drop=True)

print(result)
