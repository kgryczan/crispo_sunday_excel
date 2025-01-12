library(tidyverse)
library(readxl)

path = "files/Ex-Challenge 02 2025.xlsx"
input = read_excel(path, range = "B2:C14")
test  = read_excel(path, range = "E2:F7")

result = input %>%
  mutate(Month = format(Date, "%B"),
         M = month(Date),
         D = day(Date)) %>%
  arrange(M, D) %>%
  summarise(Month = first(Month), 
            Customers = paste0(Customer, collapse = ","),
            .by = M) %>%
  select(-M)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE