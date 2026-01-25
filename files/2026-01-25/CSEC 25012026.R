library(tidyverse)
library(readxl)
library(unpivotr)

path <- "2026-01-25/Challenge 100.xlsx"
input <- read_excel(path, sheet = 2, range = "B3:B6")
multi <- read_excel(path, sheet = 2, range = "C2:C2", col_names = FALSE) %>%
  pull(1)
test <- read_excel(path, sheet = 2, range = "E2:E11")

result = input %>%
  mutate(Items = map(Items, ~ rep(.x, multi))) %>%
  unnest()

all.equal(result$Items, test$Solution)
# [1] TRUE
