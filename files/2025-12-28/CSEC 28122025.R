library(tidyverse)
library(readxl)

path <- "2025-12-28/Challenge 88.xlsx"
input <- read_excel(path, range = "B3:D8")
test <- read_excel(path, range = "F3:K8")

result = input %>%
  mutate(
    Shifts = str_replace_all(
      Shifts,
      "(?<=\\D)(?=\\d)|(?<=\\d)(?=\\D)",
      "|"
    )
  ) %>%
  separate_wider_delim(
    Shifts,
    delim = "|",
    names_sep = "",
    too_few = "align_start"
  ) %>%
  select(starts_with("Shifts")) %>%
  mutate(across(c(4, 6), as.double))

all((result == test) | (is.na(result) & is.na(test)))
# [1] TRUE
