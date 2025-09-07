library(tidyverse)
library(readxl)

path = "files/2025-09-07/Challenge 57.xlsx"
input = read_excel(path, range = "B2:D8")
test  = read_excel(path, range = "F2:K5")

result = input %>%
  separate_longer_delim(`Assigned Staff`, delim = ", ") %>%
  mutate(rn = row_number(), .by = `Assigned Staff`) %>%
  select(-Activity) %>%
  na.omit() %>%
  pivot_wider(names_from = `Assigned Staff`, values_from = `Activity Code`) %>%
  select(colnames(test))

all.equal(result, test)
# [1] TRUE