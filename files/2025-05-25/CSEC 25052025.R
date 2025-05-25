library(tidyverse)
library(readxl)

path = "files/2025-05-25/Challenge25.xlsx"
input = read_excel(path, range = "B3:B12")
test = read_excel(path, range = "D3:D6")

letters2 = rep(letters, 2) %>% paste0(collapse = "")
sequences = map(1:26, ~ substr(letters2, .x, .x + 3)) %>% unlist()

result = input %>%
  mutate(
    contains_sequence = map_lgl(Words, ~ any(str_detect(.x, sequences)))
  ) %>%
  filter(contains_sequence) %>%
  select(Words)

all.equal(result$Words, test$Words)
# [1] TRUE
