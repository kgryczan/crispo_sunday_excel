import pandas as pd
import re

path = "files/Excel Challenge 22nd Dec.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=1)
test = pd.read_excel(path, usecols="D:G", skiprows=2, nrows=5)

rows = input.iloc[:, 0].str.split('\n').explode().tolist()

def process_row(row):
    words = row.split()
    non_digits = [word for word in words if not word.isdigit()]
    digits = [word for word in words if word.isdigit()]
    
    n = len(non_digits)
    
    if n >= 2:
        customer = non_digits[0]
        item = non_digits[1] if len(non_digits) > 1 else ""
    if n == 3:
        customer = " ".join(non_digits[0:2])
        item = non_digits[2]
    elif n == 4:
        if re.match(r"^[A-Z]\.$", non_digits[1]):
            customer = " ".join(non_digits[0:3])
            item = non_digits[3]
        else:
            customer = " ".join(non_digits[0:2])
            item = " ".join(non_digits[2:4])
    
    selling_price = digits[0]
    buying_price = digits[1]
    
    return {"Customer": customer, "Item": item, "Selling Price": selling_price, "Buying Price": buying_price}

processed_data = pd.DataFrame([process_row(row) for row in rows])
processed_data["Selling Price"] = processed_data["Selling Price"].astype('int64')
processed_data["Buying Price"] = processed_data["Buying Price"].astype('int64')
df = processed_data.reset_index(drop=True)

print(processed_data.equals(test)) # True