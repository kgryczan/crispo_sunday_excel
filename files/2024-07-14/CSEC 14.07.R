library(tidyverse)
library(readxl)

path = "files/Excel Challenge 14th July.xlsx"
input = read_xlsx(path, range = "B2:D8")
test  = read_xlsx(path, range = "F2:L8")

result = input %>%
  separate_rows(c(Customers, Orders), sep = "; ") %>%
  pivot_wider(names_from = Customers, values_from = Orders) %>%
  mutate(across(-c(1), ~as.numeric(.)))

all.equal(result, test)
#> [1] TRUE