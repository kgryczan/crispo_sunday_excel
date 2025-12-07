library(tidyverse)
library(readxl)

path <- "2025-12-07/Challenge 82.xlsx"
input <- read_excel(path, range = "B2:C6")
test <- read_excel(path, range = "D2:D6")

result = input %>%
  separate_rows(`Price/Qty/Store No.`, sep = ", ") %>%
  separate_wider_delim(
    `Price/Qty/Store No.`,
    delim = "/",
    names = c("Price", "Qty", "Store No.")
  ) %>%
  mutate(Qty = ifelse(as.integer(Qty) > 100, as.integer(Qty), 0L)) %>%
  summarise(`Total Quantity` = sum(as.integer(Qty)), .by = Date)

all.equal(result$`Total Quantity`, test$`Total Qty`)
# [1] TRUE
