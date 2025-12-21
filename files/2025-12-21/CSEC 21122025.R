library(tidyverse)
library(readxl)

path <- "2025-12-21/Challenge 87.xlsx"
input <- read_excel(path, range = "B2:B8")
test <- read_excel(path, range = "D2:D8")

result = input %>%
  mutate(extracted = str_extract(Address, "(?<=\\d{5} )[^,]+"))

all.equal(result$extracted, test$City)
# [1] TRUE
