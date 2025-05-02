library(tidyverse)
library(readxl)

path = "files/Excel Challange 21st July.xlsx"
input = read_excel(path, range = "D2:F6")
test  = read_excel(path, range = "G2:H6")

result = input %>%
  mutate(month = match(`Expected Start Month`, month.name),
         `Start Date` = make_date(year(now()), month, 1)) %>%
  mutate(`End Date` = `Start Date` + months(`Duration (Months)`)- days(1)) %>%
  select(`Start Date`, `End Date`) %>%
  mutate(across(everything(), as.POSIXct)) 

identical(result, test)
# [1] TRUE
