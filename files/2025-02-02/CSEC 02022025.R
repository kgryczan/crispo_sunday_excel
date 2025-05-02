library(tidyverse)
library(readxl)

path = "files/Ex-Challenge 05 2025.xlsx"
input = read_excel(path, range = "B2:I7")
test  = read_excel(path, range = "K2:M21")

result = input %>%
  pivot_longer(cols = -c(1, 2), names_to = "Appointments", values_to = "value") %>%
  na.omit() %>%
  uncount(value) 

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE