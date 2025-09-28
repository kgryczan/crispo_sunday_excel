library(tidyverse)
library(readxl)

path = "files/2025-09-28/Challenge 67.xlsx"
input = read_excel(path, range = "B2:E8")
test  = read_excel(path, range = "G2:J7")

result = input %>%
  mutate(Prices = Prices + first(Prices),
         Values = `Unit Values` + first(`Unit Values`)) %>%
  filter(row_number() != 1) %>%
  select(-`Unit Values`) 

all.equal(result, test)
# [1] TRUE