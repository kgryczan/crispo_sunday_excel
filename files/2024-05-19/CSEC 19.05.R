library(tidyverse)
library(readxl)

input = read_excel("files/Excel Challenge 19th May.xlsx", range = "B2:E11")
test  = read_excel("files/Excel Challenge 19th May.xlsx", range = "G2:G6")

result = input %>%
  mutate(Combined = pmap_chr(.[2:4], ~ toString(sort(c(...))))) %>%
  mutate(n = n(), .by = Combined) %>%
  filter(n == 1) %>%
  select(Products = Product)

identical(result, test)
#> [1] TRUE