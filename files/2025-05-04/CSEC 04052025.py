import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from calendar import monthrange, isleap

path = "files/2025-05-04/Challenge21.xlsx"
test = pd.read_excel(path, usecols="E:F", skiprows=2, nrows=17)

no_periods = 2
start_date = datetime.strptime("2025-01-07", "%Y-%m-%d")

leap_years = []
while len(leap_years) < no_periods:
    if isleap(start_date.year):
        leap_years.append(start_date.year)
    start_date += relativedelta(years=1)

first_dates = [datetime(year=leap_years[0], month=m, day=1) for m in range(1, 13)]
first = pd.DataFrame({
    "Period": [date.strftime("%b%y") for date in first_dates],
    "Days": [monthrange(date.year, date.month)[1] for date in first_dates]
})

second_dates = [datetime(year=leap_years[1], month=m, day=1) for m in range(1, 13)]
second = pd.DataFrame({
    "Period": [f"Q{((date.month - 1) // 3) + 1}_{date.year}" for date in second_dates],
    "Days": [monthrange(date.year, date.month)[1] for date in second_dates]
})
second = second.groupby("Period", as_index=False).sum()

result = pd.concat([first, second], ignore_index=True)

print(result)