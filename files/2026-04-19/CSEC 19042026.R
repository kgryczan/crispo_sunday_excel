library(tidyverse)
library(readxl)

path <- "2026-04-19/Challenge 113.xlsx"
input <- read_excel(path, range = "B2:C7")
test <- read_excel(path, range = "E2:F5")

result = input %>%
  mutate(Date = as.Date(Date)) %>%
  group_by(Customer) %>%
  complete(Date = seq.Date(min(Date), max(Date), by = "day")) %>%
  filter(!Date %in% as.Date(input$Date)) %>%
  mutate(Date = as.POSIXct(Date))

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE
