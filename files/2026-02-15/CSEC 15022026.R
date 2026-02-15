library(tidyverse)
library(readxl)

path <- "2026-02-15/Challenge 103.xlsx"
input <- read_excel(path, range = "B2:B13")
test <- read_excel(path, range = "D2:D13")

result <- input %>%
  mutate(
    n = row_number() - 1,
    .by = Invoice,
    `Suffixed Invoice` = if_else(
      n == 0,
      Invoice,
      paste0(Invoice, "_D", str_extract(Invoice, "\\d+"), "-", n)
    )
  ) %>%
  select(`Suffixed Invoice`)

all.equal(result$`Suffixed Invoice`, test$`Suffixed Invoice`)
# Inconsitent second delim in test data, but otherwise correct.
