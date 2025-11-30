library(tidyverse)
library(readxl)

path <- "2025-11-23/Challenge 80.xlsx"
input <- read_excel(path, range = "B3:C13")
test  <- read_excel(path, range = "E3:F13")

result = input %>%
  mutate(val2 = ifelse(Criteria == T, Value, NA)) %>%
  fill(val2, .direction = "up") %>%
  replace_na(list(val2 = 0)) %>%
  mutate(val3 = case_when(
    Criteria == T ~ 0,
    Criteria == F ~ Value + coalesce(NA, val2))) %>%
  select(Criteria, Value = val3)

all.equal(result, test)
# [1] TRUE