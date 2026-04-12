library(tidyverse)
library(readxl)

path <- "2026-04-12/Challenge 112.xlsx"
input <- read_excel(path, range = "B2:B6")
test <- read_excel(path, range = "D2:E6")

result <- input %>%
  mutate(rn = row_number()) %>%
  separate_rows(Name, sep = " ") %>%
  mutate(label = if_else(str_detect(Name, "^[A-Z]+$"), "First Name", "Other Names")) %>%
  summarise(Name = str_c(Name, collapse = " "), .by = c(rn, label)) %>%
  pivot_wider(names_from = label, values_from = Name) %>%
  select(-rn)

all.equal(result, test)
## [1] TRUE
