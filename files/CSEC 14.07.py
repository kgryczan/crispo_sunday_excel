import pandas as pd

path = "files/Excel Challenge 14th July.xlsx"
input = pd.read_excel(path, usecols="B:D", skiprows=1, nrows = 6)
test = pd.read_excel(path, usecols="F:L", skiprows=1, nrows = 6)
test.columns = test.columns.str.replace(".1", "")

result = input.assign(Customers=input.Customers.str.split("; "),
                     Orders=input.Orders.str.split("; ")) \
    .explode(["Customers", "Orders"]) \
    .pivot(index="Date", columns="Customers", values="Orders") \
    .reset_index()

result[result.columns[1:]] = result[result.columns[1:]].apply(pd.to_numeric).fillna(" ")
result.columns.name = None
test = test.fillna(" ")

print(result.equals(test)) # True