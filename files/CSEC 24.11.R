library(tidyverse)
library(readxl)

path = "files/Excel Challenge Nov 24th.xlsx"
input = read_excel(path, range = "B2:B14")

result = input %>%
  mutate(cond_form = ifelse(str_detect(Items, "\\D+ \\d+ \\D+ \\d+", negate = T), "Yes", ""))
