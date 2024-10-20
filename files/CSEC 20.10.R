library(tidyverse)
library(readxl)

path = "files/Excel Challenge October 20th.xlsx"
input = read_excel(path, range = "B2:C16")
test  = read_excel(path, range = "E2:F5")

result = input %>%
  mutate(diff1 = Units - lag(Units, 1),
         diff2 = lag(Units, 1) - lag(Units, 2),
         diff3 = lag(Units, 2) - lag(Units, 3),
         all_positive = diff1 > 0 & diff2 > 0 & diff3 > 0) %>%
  filter(all_positive) %>%
  select(Date, Units)

all.equal(result, test)  
#> [1] TRUE