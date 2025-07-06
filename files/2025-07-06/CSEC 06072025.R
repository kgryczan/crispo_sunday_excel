library(tidyverse)
library(readxl)

path = "files/2025-07-06/Challenge 38.xlsx"
input = read_excel(path, range = "B2:D11")
test  = read_excel(path, range = "F2:H8")

result = input %>%
  summarise(n = n_distinct(Product),
            Product = paste0(Product, collapse = ", "),
            .by = c(Date,Store)) %>%
  mutate(lag = lag(n, default = 0), .by = Store) %>%
  select(Date, Store, Product = lag)

all.equal(result, test, check.attributes = FALSE)            
#> [1] TRUE