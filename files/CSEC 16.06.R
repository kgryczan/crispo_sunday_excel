library(tidyverse)
library(readxl)

path = "files/Excel Challenge 16th June.xlsx"
input = read_excel(path, range = "B2:B22")
test  = read_excel(path, range = "D2:E5")

result = input %>%
  as.list() %>%
  unlist() %>%
  matrix(ncol = 2, byrow = TRUE) %>%
  as_tibble() %>%
  setNames(c("Date", "Value")) %>%
  mutate(Date = as.Date(Date, origin = "1899-12-30"),
         Month = month(Date)) %>%
  summarise(`Closing Order` = last(Value), .by = Month) 

identical(result, test)
# [1] TRUE