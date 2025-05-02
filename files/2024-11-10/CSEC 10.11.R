library(tidyverse)
library(readxl)

path = "files/Excel Challenge Nov 10th.xlsx"
input = read_excel(path, range = "B3:B16")

result = input %>%
  mutate(change = Items != lag(Items)) %>%
  replace_na(list(change = TRUE))

print(result)
