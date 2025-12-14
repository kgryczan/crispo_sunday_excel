import pandas as pd

df = pd.read_excel("2025-12-14/Challenge 83.xlsx", usecols="B:D", skiprows=1, nrows=4)
test = pd.read_excel("2025-12-14/Challenge 83.xlsx", usecols="F:H", skiprows=1, nrows=14).rename(columns=lambda c: c.replace('.1', ''))

def split_and_align(a, b):
    a = a.split(", ") if isinstance(a, str) and ", " in a else [a]
    b = b.split(", ") if isinstance(b, str) and ", " in b else [b]
    n = max(len(a), len(b))
    return (a * n)[:n], (b * n)[:n]

df[["Customer", "Sales"]] = df.apply(lambda r: pd.Series(split_and_align(r["Customer"], r["Sales"])), axis=1)
df = df.explode(["Customer", "Sales"])
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
def add_subtotals(df):
    out = []
    for m, g in df.groupby("Month", sort=False):
        out.append(g)
        row = {**{c: None for c in df.columns}, "Month": "Total Sales", "Sales": g["Sales"].sum()}
        out.append(pd.DataFrame([row], columns=df.columns))
    return pd.concat(out, ignore_index=True)

df = add_subtotals(df)

print(df.equals(test))

