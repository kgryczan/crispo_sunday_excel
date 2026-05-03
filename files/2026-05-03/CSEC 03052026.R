library(tidyverse)
library(readxl)

path <- "2026-05-03/Challenge 115.xlsx"
input <- read_excel(path, range = "B3:D9")
test <- read_excel(path, range = "F3:G5")

result = input %>%
  arrange(Product, Date) %>%
  filter(Price < lag(Price), .by = Product) %>%
  slice_head(n = 1, by = Product) %>%
  transmute(Product, `First Drop Date` = Date)

all.equal(result, test)
# [1] TRUE
