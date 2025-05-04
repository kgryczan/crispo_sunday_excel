library(tidyverse)
library(readxl)
library(lubridate)

Sys.setlocale("LC_ALL", "English")

path = "files/2025-05-04/Challenge21.xlsx"
test = read_excel(path, range = "E3:F19")
no_periods = 2
start_date = as.Date("2025-01-07")

leap_years = c()
while (length(leap_years) < no_periods) {
  if (leap_year(start_date)) {
    leap_years = c(leap_years, year(start_date))
  }
  start_date = start_date + years(1)
}

first = make_date(year = leap_years[1], month = 1:12, day = 1) %>%
  as_tibble() %>%
  mutate(Days = days_in_month(value), Period = format(value, "%b%y")) %>%
  select(Period, Days)

second = make_date(year = leap_years[2], month = 1:12, day = 1) %>%
  as_tibble() %>%
  mutate(
    Days = days_in_month(value),
    Period = paste0("Q", quarter(value), "_", year(value))
  ) %>%
  summarise(Days = sum(Days), .by = Period)

result = bind_rows(first, second)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE
