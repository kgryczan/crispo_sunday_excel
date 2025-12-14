library(tidyverse)
library(readxl)
library(janitor)

path <- "2025-12-14/Challenge 83.xlsx"
input <- read_excel(path, range = "B2:D6")
test <- read_excel(path, range = "F2:H15")

result <- input %>%
  separate_longer_delim(cols = c(Customer, Sales), delim = ", ") %>%
  mutate(Sales = as.numeric(Sales))

summary <- result %>%
  group_by(Month) %>%
  summarize(Sales = sum(Sales, na.rm = TRUE), .groups = "drop") %>%
  mutate(Customer = NA_character_, .before = Sales)

months <- unique(result$Month)
final <- map_dfr(
  months,
  ~ bind_rows(
    result %>% filter(Month == .x),
    summary %>% filter(Month == .x)
  )
) %>%
  mutate(Month = ifelse(is.na(Customer), "Total Sales", Month))

all.equal(final, test)
# [1] TRUE
