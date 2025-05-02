library(tidyverse)
library(readxl)

path = "files/Excel Challenge 29th Dec.xlsx"
input = read_excel(path, range = "B2:B9")
test  = read_excel(path, range = "D2:D15")

result = input %>%
  separate_rows(Problem, sep = "") %>%
  filter(Problem != "")

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE