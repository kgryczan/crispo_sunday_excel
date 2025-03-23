library(tidyverse)
library(readxl)

path = "files/Challenge1225.xlsx"
input = read_excel(path, range = "B3:C7")
test  = read_excel(path, range = "E3:F7")

result = input %>%
  separate_rows(Narration, sep = "[,.]") %>%
  mutate(action = case_when(
    str_detect(Narration, "sell|sold") ~ "sell",
    str_detect(Narration, "buy") ~ "buy",
    TRUE ~ NA_character_
  ))  %>%
  na.omit() %>%
  mutate(amount = as.numeric(str_extract(Narration, "\\d+")) * ifelse(action == "buy", -1, 1)) %>%
  summarise(`Profit (loss)` = sum(amount), .by = Items)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE