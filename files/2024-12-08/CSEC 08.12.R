library(tidyverse)
library(readxl)

path = "files/Excel Challenge Dec 8th.xlsx"
input = read_excel(path, range = "B2:D12")
test  = read_excel(path, range = "F2:G6")

result = input %>%
  pivot_wider(names_from = "Numb", values_from = "Route") %>%                                                                                                                                                                                                                                                                                                                  pivot_wider(names_from = "Numb", values_from = "Route") %>%
  pivot_longer(cols = c(2:5), names_to = "Numb", values_to = "Route") %>%
  filter(!is.na(Route)) %>%
  mutate(Route = ifelse(Numb == 1, Route, str_extract(Route, "\\- [A-Z]+"))) %>%
  summarise(`Whole Route` = paste0(Route, collapse = " "), .by = Airline) %>%
  arrange(Airline)

all.equal(result, test)
#> [1] TRUE