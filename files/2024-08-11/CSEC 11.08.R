library(tidyverse)
library(readxl)

path = "files/Excel Challenge 11th August.xlsx"
input = read_excel(path, range = "B2:C14")
test  = read_excel(path, range = "E2:F9") 
dup_test =  pull(test, `Duplicate Price`) %>% sort()
uniq_test = pull(test, `Unique Price`) %>% sort()

result = input %>%
  mutate(unique = n(), .by = Price) %>%
  mutate(uniqueness = if_else(unique == 1, "Unique Price", "Duplicata Price")) %>%
  select(Cookies, uniqueness)

dup_result = filter(result, uniqueness == "Duplicata Price") %>% pull(Cookies) %>% sort()
uniq_result = filter(result, uniqueness == "Unique Price") %>% pull(Cookies) %>% sort()

identical(dup_test, dup_result) && identical(uniq_test, uniq_result)
#> [1] TRUE