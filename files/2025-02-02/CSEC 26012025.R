library(tidyverse)
library(readxl)

path = "files/Ex-Challenge 04 2025.xlsx"
input = read_excel(path, range = "B3:D18")
test  = read_excel(path, range = "F3:G13")

result = input %>%
  mutate(Rank = dense_rank(desc(Demand))) %>%
  summarise(`Fruit(s)` = paste0(Fruit, collapse = " ; "), .by = Rank) %>%
  arrange(Rank)
