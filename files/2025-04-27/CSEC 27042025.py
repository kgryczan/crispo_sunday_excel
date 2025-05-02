import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

path = "files/Challenge20.xlsx"
test = pd.read_excel(path, usecols="E", skiprows=1, nrows=35)

period_years = 2
start = datetime(2025, 1, 1)
end = start + relativedelta(years=period_years) - timedelta(days=1)

seq = pd.date_range(start=start, end=end, freq='D')

month = pd.to_datetime(seq).to_period('M').unique().strftime('%b%y')

quarters = pd.to_datetime(seq).to_period('Q').unique()
quarters = [f"Q{q.quarter}_{q.year}" for q in quarters]

years = pd.to_datetime(seq).to_period('Y').unique().year.astype(str)

result = pd.DataFrame({"Dynamic Period": list(month) + [f"Q{q.quarter}_{q.year}" for q in pd.to_datetime(seq).to_period('Q').unique()] + list(pd.to_datetime(seq).to_period('Y').unique().year)})
print(result.equals(test)) # True