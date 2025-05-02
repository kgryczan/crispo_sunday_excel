library(tidyverse)
library(readxl)

path = "files/Ex-Challenge 08 2025.xlsx"
input = read_excel(path, range = "B2:E5")
test  = read_excel(path, range = "G2:J8")

result = input %>%
  separate_rows(Service, Rating, sep = "\r\n") %>%
  mutate(Rating = as.numeric(Rating))

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE