library(tidyverse)
library(readxl)

path <- "2026-02-01/Challenge 101.xlsx"
input1 <- read_excel(path, range = "B3:B6")
input2 <- read_excel(path, range = "D2:E4")
test <- read_excel(path, range = "G2:G9")

result <- input1 %>%
  mutate(row = row_number()) %>%
  left_join(input2, by = c("row" = "Item:")) %>%
  mutate(items = map2(`Items`, replace_na(`Repeats:`, 1), rep)) %>%
  unnest_longer(items) %>%
  select(items)

all.equal(result$items, test$Solution)
#> [1] TRUE
