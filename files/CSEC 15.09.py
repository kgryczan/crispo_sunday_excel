import pandas as pd

path = "files/Excel Challenge September 15th.xlsx"

input = pd.read_excel(path, usecols = "B:C", skiprows = 1, nrows = 7)
test = pd.read_excel(path, usecols = "E:F", skiprows = 1, nrows = 4).fillna("")

result = input.assign(Salary_Range = lambda x: pd.cut(x["Salary"], 
                                                      bins = [1000, 5000, 10000, 15000, 100000], 
                                                      labels = ["1000 - 4999", "5000 - 9999", "10000 - 14999", "> 15000"]))
result = result.groupby("Salary_Range")["Staff"].apply(lambda x: ", ".join(x)).reset_index(name="Staffs")

print(result)
print(test)
# sorting names in one cell is not the same.