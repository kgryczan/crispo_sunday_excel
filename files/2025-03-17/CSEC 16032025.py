import pandas as pd

path = "CHALLENGE 1205.xlsx"
input_data = pd.read_excel(path, usecols="B", skiprows=2, nrows=11)
test = pd.read_excel(path, usecols="D:G", skiprows=2, nrows=5)

result = (
    input_data["SUB-DEPARTMENT NAMES"]
    .str.split("-", n=1, expand=True)
    .rename(columns={0: "sub_department", 1: "department"})
)
result["SUB-DEPARTMENT NAMES"] = input_data["SUB-DEPARTMENT NAMES"]
result["rn"] = result.groupby("sub_department").cumcount() + 1
result = result.drop(columns=["department"]).pivot(index="rn", columns="sub_department", values="SUB-DEPARTMENT NAMES").reset_index(drop=True)

print(result.equals(test))
