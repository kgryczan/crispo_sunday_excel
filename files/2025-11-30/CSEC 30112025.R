library(tidyverse)
library(readxl)

path <- "2025-11-30/Challenge 81.xlsx"
input <- read_excel(path, range = "B2:B6")
test <- read_excel(path, range = "D2:D6")

result = input %>%
  mutate(across(everything(), ~ str_remove_all(., "<.*?>"))) %>%
  mutate(across(everything(), ~ str_replace_all(., "&nbsp;", ""))) %>%
  mutate(across(everything(), ~ str_squish(.)))

all.equal(result$Problem, test$Solution)
# [1] TRUE
