library(tidyverse)
library(readxl)

path = "files/2025-08-31/Challenge 53.xlsx"
input = read_excel(path, range = "B2:E8")
test  = read_excel(path, range = "G2:G4") %>% pull()

result = input %>%
  filter(if_all(-Customer, is.na)) %>%
  pull(Customer)

all.equal(result, test)
