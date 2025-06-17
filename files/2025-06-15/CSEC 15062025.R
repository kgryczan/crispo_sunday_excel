library(tidyverse)
library(readxl)

path = "files/2025-06-15/Challenge 35.xlsx"
input = read_excel(path, range = "B3:B11")
test = read_excel(path, range = "D3:E4")

result = input %>%
  mutate(
    title = case_when(
      str_count(Names, "[AEIOUaeiou]") == 0 ~ "No Vowels",
      str_count(Names, "[AEIOUaieou]") == 5 ~ "All Vowels",
      TRUE ~ "Some Vowels"
    )
  ) %>%
  filter(title != "Some Vowels") %>%
  summarise(
    count = n(),
    .by = title
  ) %>%
  pivot_wider(
    names_from = title,
    values_from = count,
    values_fill = 0
  )
all.equal(result, test, check.attributes = FALSE)
# TRUE
