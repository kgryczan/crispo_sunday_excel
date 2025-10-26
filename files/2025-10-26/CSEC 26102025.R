library(tidyverse)
library(readxl)

path = "files/2025-10-26/Challenge 72.xlsx"
input = read_excel(path, range = "B3:F8", col_names = FALSE, col_types = "text")
test  = read_excel(path, range = "H3:K12", col_names = FALSE) %>%
  mutate(...1 = str_to_title(...1))

result = input %>%
  mutate(...1 = str_to_title(...1)) %>%
  mutate(measure = ifelse(!str_detect(...1, "item|Item"), ...1, NA)) %>%
  fill(measure, .direction = "down") %>%
  filter(measure != ...1) %>%
  pivot_longer(-c(measure, ...1, ...2), names_to = "item", values_to = "value") %>%
  pivot_wider(names_from = measure, values_from = value) %>%
  add_row(...1 = NA, ...2 = NA, item = "", Units = "Units", Availability = "Availability", .before = 1) %>%
  select(-item)

colnames(result) = colnames(test)

all.equal(result, test)
# [1] TRUE