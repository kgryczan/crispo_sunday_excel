library(tidyverse)
library(readxl)

path <- "2026-01-04/Challenge 89.xlsx"
input1 <- read_excel(path, range = "B4:C6")
input2 <- read_excel(path, range = "B9:C11")
test <- read_excel(path, range = "F4:G11", col_names = FALSE) %>%
  select(`0` = 1, `1` = 2)

result = crossing(input1, input2) %>%
  mutate(Pages = as.character(Pages)) %>%
  pivot_longer(
    cols = everything(),
    names_to = "type",
    values_to = "value"
  ) %>%
  mutate(id = (row_number() + 1) %% 2, id2 = (row_number() + 1) %/% 2) %>%
  pivot_wider(
    id_cols = id2,
    names_from = id,
    values_from = value
  ) %>%
  select(-id2)

all.equal(result, test)
# [1] TRUE
