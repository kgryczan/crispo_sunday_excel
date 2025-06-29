library(tidyverse)
library(readxl)

path = "files/2025-06-22/Challenge 36.xlsx"
input = read_excel(path, range = "B3:C7")
test  = read_excel(path, range = "E3:F11")

result = input %>%
  separate_longer_delim(Students, delim = ", ") 

all.equal(test, result, check.attributes = FALSE)
#> [1] TRUE