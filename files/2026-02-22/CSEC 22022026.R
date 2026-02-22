library(tidyverse)
library(readxl)

path <- "2026-02-22/Challenge 104.xlsx"
input <- read_excel(path, sheet = "Sheet3", range = "B3:O24")
test <- read_excel(path, sheet = "Sheet3", range = "Q8:X12")


result = input %>%
  filter(rowSums(!is.na(.)) > 1) %>%
  select(where(~ any(!is.na(.)))) %>%
  janitor::row_to_names(row_number = 1) %>%
  janitor::clean_names() %>%
  fill(!starts_with("na"), .direction = "down") %>%
  fill(na_3, .direction = "down") %>%
  rename(
    Course = na,
    Hours = na_2,
    Session = na_3
  ) %>%
  select(where(~ any(!is.na(.)))) %>%
  fill(everything(), .direction = "up") %>%
  distinct() %>%
  mutate(
    date = janitor::excel_numeric_to_date(as.numeric(date)) %>% as.POSIXct(),
    cost = as.numeric(cost)
  )

names(result) = names(test)
all.equal(result, test)
#> [1] TRUE
