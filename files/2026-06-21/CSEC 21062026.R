library(tidyverse)
library(readxl)

path <- "2026-06-21/Challenge-Jun21.xlsx"
input1 <- read_excel(path, range = "B3:D10")
input2 <- read_excel(path, range = "G3:L17")
test <- read_excel(path, range = "E3:E10")

result <- input1 %>%
  left_join(
    input2 %>% pivot_longer(-Grades, names_to = "year", values_to = "value"),
    by = c(`Job Grade` = "Grades")
  ) %>%
  mutate(
    `Range Difference` = coalesce(value - lag(value), 0),
    .by = `Job Grade`
  ) %>%
  filter(Salary <= value) %>%
  slice_head(n = 1, by = `Job Grade`) %>%
  select(`Range Difference`)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE
