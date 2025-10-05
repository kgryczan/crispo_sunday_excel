library(tidyverse)
library(readxl)

path = "files/2025-10-05/Challenge 65.xlsx"
input = read_excel(path, range = "B2:B14")
test  = read_excel(path, range = "D2:D14")

result = input %>%
  mutate(cid = consecutive_id(`Cost Codes`)) %>%
  mutate(gr_n = n(), .by = cid) %>%
  mutate(Consecutive = ifelse(gr_n > 1, T, F)) %>%
  select(Consecutive)

all.equal(result, test)
# [1] TRUE