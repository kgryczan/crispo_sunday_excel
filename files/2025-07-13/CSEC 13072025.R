library(tidyverse)
library(readxl)

path = "files/2025-07-13/Challenge 39.xlsx"
input = read_excel(path, range = "B2:D11")
test  = read_excel(path, range = "H2:I11")

result = input %>%
  arrange(Product, Date) %>%
  mutate(Product = ifelse(row_number() > 1, NA_character_, Product), .by = Product) %>%
  select(-Date)

all.equal(result, test, check.attributes = FALSE) 
# > [1] TRUE