import zipfile
import xml.etree.ElementTree as ET
import pandas as pd

path = "2026-03-15/Challenge 107.xlsx"
NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
with zipfile.ZipFile(path) as z:
    with z.open("xl/worksheets/sheet1.xml") as f:
        root = ET.parse(f).getroot()

col_elements = root.findall(f".//{{{NS}}}col")
hidden_cols = [int(col.get("min")) for col in col_elements if col.get("hidden") == "1"]
df = pd.read_excel(path, usecols="A:I", skiprows=1, nrows=4)
test = pd.read_excel(path, usecols="K", skiprows=1, nrows=4)
cols_to_drop = [df.columns[i - 1] for i in hidden_cols]
result = (
    df.drop(columns=cols_to_drop)
      .dropna(axis=1, how="all")
)
result["Total"] = result.select_dtypes(include="number").sum(axis=1)
(result["Total"] == test["Total"].values).all()
# True
