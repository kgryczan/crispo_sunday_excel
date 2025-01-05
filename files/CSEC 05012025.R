library(tidyverse)
library(readxl)

path = "files/Ex-Challenge 01 2025.xlsx"
input = read_excel(path, range = "B2:E14")
test  = read_excel(path, range = "G2:J8")

result = input %>%
  mutate(across(c(Invoice, Posted, Dept), ~trimws(.))) %>%
  unite("name", c("Invoice", "Posted", "Dept"), sep = "_") %>%
  group_by(name) %>%
  filter(n() == 1 | (n() == 2 & sum(Value) != 0)) %>%
  separate("name", c("Invoice", "Posted", "Dept"), sep = "_")

all.equal(result, test)
#> [1] TRUE