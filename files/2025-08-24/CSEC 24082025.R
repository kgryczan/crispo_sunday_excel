library(tidyverse)
library(readxl)

path = "files/2025-08-24/Challenge 52.xlsx"
input = read_excel(path, range = "B2:E8")
test  = read_excel(path, range = "G2:H8") %>%
  replace_na(list(`Missing Data` = ""))

result = input %>%
  mutate(Customer = as.factor(Customer)) %>%
  pivot_longer(cols = -Customer, 
               names_to = "Var", 
               values_to = "val", 
               values_transform = as.character) %>%
  mutate(missing = ifelse(is.na(val), Var, NA)) %>%
  summarise(`Missing Data` = paste(missing[!is.na(missing)], collapse = ", "), .by = Customer) %>%
  mutate(Customer = as.character(Customer))

all.equal(result, test, check.attributes = FALSE)
# > [1] TRUE         