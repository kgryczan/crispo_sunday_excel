library(tidyverse)
library(readxl)

path = "files/Challenge15-2025.xlsx"
input = read_excel(path, range = "B3:G5")
test = read_excel(path, range = "I3:K13")

result = input %>%
  rename(product = ...1) %>%
  pivot_longer(cols = -product, names_to = "month", values_to = "sales") %>%
  fill(sales, .direction = "down") %>%
  mutate(m_diff = sales - lag(sales, 1), .by = product) %>%
  replace_na(list(m_diff = 0)) %>%
  filter(m_diff > 0) %>%
  select(-sales) %>%
  uncount(m_diff) %>%
  mutate(Required = 1)

names(result) = names(test)

all.equal(result, test)
# [1] TRUE
