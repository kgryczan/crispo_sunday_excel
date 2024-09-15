library(tidyverse)
library(readxl)

path = "files/Excel Challenge September 8th.xlsx"
input = read_excel(path, range = "B2:C7")

search_vec = list("Apple", "Kiwi")

result = input %>%
  mutate(Stock = str_remove_all(Stock, "\\s") %>% str_split(",")) %>%
  mutate(Found = map_lgl(Stock, ~any(search_vec %in% .x))) %>%
  summarise(Count = sum(Found))

result
#   3
#   
#   True