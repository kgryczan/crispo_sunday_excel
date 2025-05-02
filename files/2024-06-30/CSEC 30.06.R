library(tidyverse)
library(readxl)

path = "files/Excel Challenge  30th June.xlsx"

input = read_xlsx(path, range = "B3:D7")
test  = read_xlsx(path, range = "E3:I7")

result = input %>%
  mutate(seq = map2(`Start Date`, `End Date`, seq, by = "month")) %>%
  unnest_longer(seq) %>%
  mutate(year = year(seq),
         val = 1) %>%
  select(Project, year, val) %>%
  pivot_wider(names_from = year, values_from = val, values_fn = sum) %>%
  select(-Project)

identical(result, test)
# [1] TRUE