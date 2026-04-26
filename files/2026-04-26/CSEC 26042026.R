library(tidyverse)
library(readxl)

path <- "2026-04-26/Challenge 114.xlsx"
input <- read_excel(path, range = "B3:D8")
input2 <- read_excel(path, range = "B10:C12")
test <- read_excel(path, range = "F3:H8")

result <-
  input %>%
  left_join(input2, by = "Customer") %>%
  group_by(Customer) %>%
  arrange(Invoice, .by_group = TRUE) %>%
  mutate(
    cum = cumsum(Amount),
    prev = lag(cum, default = 0),
    Allocated = pmax(0, pmin(Amount, Payment - prev)),
    Remaining = Amount - Allocated
  ) %>%
  ungroup() %>%
  select(Invoice, Allocated, Remaining)

all.equal(result, test)
# [1] TRUE
