library(tidyverse)
library(readxl)

input = read_excel("files/Excel Challenge 26th May.xlsx", range = "C2:E20")
test  = read_excel("files/Excel Challenge 26th May.xlsx", range = "I2:K7")

result = input %>%
  na.omit() %>%
  tail(5)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE