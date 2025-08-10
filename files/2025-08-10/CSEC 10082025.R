library(tidyverse)
library(readxl)

path = "files/2025-08-10/Challenge 50.xlsx"
input = read_excel(path, range = "A2:C14")
test  = read_excel(path, range = "E2:E6")

param = "National ID"

result = input %>%
  nest_by(`Staff No.`) %>%
  mutate(has_id = any(data$Identifiers == param)) %>%
  filter(!has_id | is.na(has_id)) %>%
  select(`Staff No.`)

all.equal(result$`Staff No.`, test$`Staff Without National ID`)
# > [1] TRUE