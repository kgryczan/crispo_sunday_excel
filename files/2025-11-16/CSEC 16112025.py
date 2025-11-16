import pandas as pd
df = pd.DataFrame({
    "Stock": [
        "Spoon Area-2 - Kitchen Item",
        "Forks - Dining Item : Silver Colour",
        "Sofa: Recliner Area-5 - Lounge Item",
        "King-Bed:Wide - Bedroom Item :Black-Lable"
    ],
    "Seller": ["Aiden", "Adrian", "Ericka", "Emma"]
})

test = pd.DataFrame({
    "Item & Seller": [
        "Kitchen Item: Aiden",
        "Dining Item: Adrian",
        "Lounge Item: Ericka",
        "Bedroom Item: Emma"
    ]
})

df["Item"] = df["Stock"].str.extract(r"([A-Za-z0-9\-]+) Item")[0] + " Item"
result = pd.DataFrame({
    "Item & Seller": df["Item"] + ": " + df["Seller"]
})

print(result.equals(test)) # True