import pandas as pd
import datetime
import calendar

path = "files/Excel Challange 21st July.xlsx"
input_data = pd.read_excel(path, usecols="D:F", skiprows=1, nrows=4)
test = pd.read_excel(path, usecols="G:H", skiprows=1, nrows=4)

month_dict = {month: index for index, month in enumerate(calendar.month_name) if month}

result = input_data.copy()
result['Expected Start Month'] = result['Expected Start Month'].str.strip() # May had extra space at the end :D
result['month'] = result['Expected Start Month'].apply(lambda x: month_dict[x])
result['Start Date'] = result.apply(lambda row: datetime.datetime(datetime.datetime.now().year, row['month'], 1), axis=1)
result['End Date'] = result.apply(lambda row: row['Start Date'] + pd.DateOffset(months=row['Duration (Months)']) - pd.DateOffset(days=1), axis=1)
result = result[['Start Date', 'End Date']].apply(pd.to_datetime)

print(result.equals(test))  # True
