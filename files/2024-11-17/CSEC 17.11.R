library(tidyverse)
library(readxl)

path = "files/Excel Challenge October 17th.xlsx"
input = read_excel(path, range = "B2:D16")
test  = read_excel(path, range = "E2:E16")

result = input %>%
  mutate(group = consecutive_id(Defects)) %>%
  mutate(`Running Totals` = ifelse(Defects != 1, cumsum(`Units Made`), 0), .by = group)
         
all.equal(result$`Running Totals`, test$`Running Totals`)
# [1] TRUE