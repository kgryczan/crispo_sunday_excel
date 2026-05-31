library(tidyverse)
library(readxl)

path <- "2026-05-31/Challenge 128.xlsx"
input <- read_excel(path, range = "B2:B8")
test <- read_excel(path, range = "D2:E8")

result <- input %>%
  mutate(
    word = str_extract_all(Sentence, "\\b\\w+\\b"),
    `Longest Word` = map_chr(word, ~ .x[which.max(nchar(.x))]),
    `Length` = nchar(`Longest Word`)
  ) %>%
  select(`Longest Word`, Length)

all.equal(result, test)
# [1] TRUE
