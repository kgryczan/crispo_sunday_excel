library(tidyverse)
library(readxl)

path = "files/Excel Challenge 4th August.xlsx"
input = read_excel(path, range = "B2:C8")
test  = read_excel(path, range = "E2:F5")

result = input %>%
  separate_rows(Customers, sep = "; ") %>%
  mutate(Customers = str_trim(Customers)) %>%
  mutate(count = n(), .by = c(Customers, Date)) %>%
  filter(count > 1) %>%
  distinct() %>%
  summarise(`Repeat Customers` = str_c(Customers, collapse = "; "), .by = Date)

identical(result, test)
# [1] TRUE