library(tidyverse)
library(readxl)

input = read_excel("files/Excel Challenge 9th June .xlsx", range = "C2:F13")
test  = read_excel("files/Excel Challenge 9th June .xlsx", range = "H2:H10") %>%
  arrange(Students)

result = input %>%
  pivot_longer(cols = -c(1)) %>%
  count(value) %>%
  filter(n == 1) %>%
  select(Students = value) %>%
  arrange(Students)

result
# Eric and Fred attended 2 trainings