library(tidyverse)
library(readxl)

path <- "2026-03-29/Challenge 109.xlsx"
input <- read_excel(path, range = "B2:B6")
test <- read_excel(path, range = "D2:D6") %>%
  replace_na(list(`Order No.` = ""))

result = input %>%
  mutate(
    `Order No.` = str_extract_all(Order_Description, "PRD-[A-Z][0-9]+") %>%
      map_chr(~ str_c(., collapse = " ; "))
  )

all.equal(result$`Order No.`, test$`Order No.`)
# [1] TRUE
