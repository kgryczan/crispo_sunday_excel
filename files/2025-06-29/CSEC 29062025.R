library(tidyverse)
library(readxl)

path = "files/2025-06-29/Challenge 37.xlsx"
input = read_excel(path, range = "B3:F10")
test  = read_excel(path, range = "H3:O4") %>% 
  rename(Item = `...1`)

result = input %>%
  mutate(Col = coalesce(Level, Gender, Location)) %>%
  select(-c(Level, Gender, Location)) %>%
  pivot_wider(names_from = Col, values_from = Values) 

all.equal(result, test)
# > [1] TRUE