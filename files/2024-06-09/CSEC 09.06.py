import pandas as pd

input = pd.read_excel("files/Excel Challenge 9th June .xlsx", usecols="C:F", skiprows=1)
test = pd.read_excel("files/Excel Challenge 9th June .xlsx",  usecols="H:H", skiprows=1, nrows = 8) \
    .sort_values(by="Students").reset_index(drop=True)

result = input.melt(id_vars=["Start"], var_name="Subject", value_name="Students")
result = result.groupby("Students").count().reset_index()
result = result[result["Start"] == 1]["Students"].reset_index(drop=True)
print(result)
# Eric and Fred has 2 trainings