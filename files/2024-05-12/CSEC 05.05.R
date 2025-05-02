library(tidyverse)
library(readxl)

input = read_excel("files/Excel Challenge 5th May.xlsx", range = "B2:D41")

result = input %>%
  mutate(Month = floor_date(Date, "month"),
         quarter = quarter(Month), 
         year = year(Date)) %>%
  summarise(`Man Hour` = sum(`Man Hour`),
            `LTI Recorded` = sum(`LTI Recorded`),
            .by = c(year, Month, quarter)) %>%
  mutate(valid = ifelse(all(`LTI Recorded` > 0), 1, 0), .by = c(year, quarter)) %>%
  summarise(n = n_distinct(paste(year, quarter, sep = "-")), .by = valid) %>%
  filter(valid == 1) %>%
  pull(n)

print(result)
# [1] 3L
