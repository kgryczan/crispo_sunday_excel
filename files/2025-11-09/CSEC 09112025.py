import pandas as pd
import numpy as np

path = "2025-11-09/Challenge 74.xlsx"
input = pd.read_excel(path, usecols="B:F", skiprows=2, header=None, nrows=6)
test = pd.read_excel(path, usecols="H:K", skiprows=2, header=None, nrows=13)

result = (
    input
    .assign(
        aspect=lambda df: np.where(
            ~df.iloc[:, 0].str.contains("(?i)item", regex=True),
            df.iloc[:, 0],
            np.nan
        )
    )
    .ffill()
    .loc[lambda df: df.iloc[:, 0] != df["aspect"]]
    .melt(
        id_vars=[input.columns[0], input.columns[1], "aspect"],
        var_name="item",
        value_name="value"
    )
    .loc[:, [input.columns[0], input.columns[1], "aspect", "value"]]
    .assign(value=lambda df: df["value"].astype(str))
)
header = pd.DataFrame({
    result.columns[0]: [np.nan],
    result.columns[1]: [np.nan],
    result.columns[2]: [np.nan],
    result.columns[3]: ["Values"]
})
result = pd.concat([header, result], ignore_index=True)

# provided answer is not correct