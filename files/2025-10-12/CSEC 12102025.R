library(tidyverse)
library(readxl)

path = "files/2025-10-12/Challenge 70.xlsx"
input = read_excel(path, range = "B2:C12")
test  = read_excel(path, range = "E2:F6")

result = input %>%
  mutate(Item = paste0("Group ",cumsum(str_detect(Item, "Group")))) %>%
  summarise(Prices = sum(Prices,na.rm = TRUE), .by = Item)

all.equal(result, test)
# [1] TRUE