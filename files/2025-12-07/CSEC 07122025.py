import pandas as pd

path = "2025-12-07/Challenge 82.xlsx"
input_df = pd.read_excel(path, usecols="B:C", skiprows=1, nrows=4)
test = pd.read_excel(path, usecols="D:D", skiprows=1, nrows=4)

result = (
    input_df
    .assign(**{"Price/Qty/Store No.": input_df["Price/Qty/Store No."].str.split(", ")})
    .explode("Price/Qty/Store No.")
    .reset_index(drop=True)
    .assign(**{
        "Price": lambda df: df["Price/Qty/Store No."].str.split("/", expand=True)[0],
        "Qty": lambda df: pd.to_numeric(
            df["Price/Qty/Store No."].str.split("/", expand=True)[1],
            errors="coerce"
        ).fillna(0).astype(int).where(lambda x: x > 100, 0)
    })
    .groupby("Date", as_index=False)
    .agg(**{"Total Quantity": ("Qty", "sum")})
)

print(result["Total Quantity"].equals(test["Total Qty"]))
# True
