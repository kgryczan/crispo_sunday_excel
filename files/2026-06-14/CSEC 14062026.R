library(tidyverse)
library(readxl)

path <- "2026-06-14/Challenge 140.xlsx"
input <- read_excel(path, range = "B2:C8")
test <- read_excel(path, range = "E2:F4")

result <- input %>%
  mutate(Month = match(Month, month.abb)) %>%
  distinct(Customer, Month) %>%
  transmute(Customer, Month = Month + 1) %>%
  anti_join(
    input %>% mutate(Month = match(Month, month.abb)),
    by = c("Customer", "Month")
  ) %>%
  filter(Month <= max(match(input$Month, month.abb), na.rm = TRUE)) %>%
  transmute(Month = month.abb[Month], `Customer Lost` = Customer)

all.equal(result, test)
# [1] TRUE
