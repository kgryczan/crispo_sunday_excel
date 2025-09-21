library(tidyverse)
library(readxl)

path = "files/2025-09-21/Challenge 61.xlsx"
input = read_excel(path, range = "B2:F8")
test  = read_excel(path, range = "H2:J8")

# short but little bit difficult
result = input %>%
  select(-where(~all(is.na(.)))
         
# short and easy
result2 = input %>%
  janitor::remove_empty("cols")

all.equal(test, result, check.attributes = FALSE) # True
all.equal(test, result2, check.attributes = FALSE) # True
