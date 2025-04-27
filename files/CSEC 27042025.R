library(tidyverse)
library(readxl)
library(lubridate)

path = "files/Challenge20.xlsx"
test = read_excel(path, range = "E2:E36")

Sys.setlocale("LC_TIME", "en_US.UTF-8")
period_years = 2
start = as.Date('2025-01-01')
end = start + years(period_years) - days(1)

seq = seq.Date(start, end, by = "1 day")

month = floor_date(seq, unit = "month") %>% unique() %>% format("%b%y")
quarters = floor_date(seq, unit = "quarter") %>%
  quarter() %>%
  paste0("Q", ., "_", year(seq)) %>%
  unique()
years = floor_date(seq, unit = "year") %>% unique() %>% year()

result = data.frame(c(month, quarters, years))
all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE
