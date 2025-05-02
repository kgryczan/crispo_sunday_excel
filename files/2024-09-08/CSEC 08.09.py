import pandas as pd

path = "files/Excel Challenge September 8th.xlsx"
input = pd.read_excel(path, usecols = "B:C", skiprows = 1, nrows = 5, names = ["Stall","Stock"])

search_vec = ["Apple", "Kiwi"]
result = input
result["Stock"] = result["Stock"].str.replace(" ", "").str.split(",")
result = result.explode("Stock")
result = result[result["Stock"].isin(search_vec)]["Stall"].nunique()

print(result) # 3 
# True