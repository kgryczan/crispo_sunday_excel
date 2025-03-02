library(tidyverse)
library(readxl)
library(lubridate)
library(hms)

path = "files/Ex-Challenge 09 2025.xlsx"
input = read_excel(path, range = "B3:B7")
test  = read_excel(path, range = "D3:F7") %>%
  mutate(Time = as_hms(Time) %>% as.POSIXct())

result = input %>%
  mutate(Dates = gsub("\\.", "", Dates)) %>%
  mutate(Dates = parse_date_time(Dates, "b. d, Y, I:M p")) %>%
  mutate(Date = as.Date(Dates) %>% as.POSIXct(),
         Day = wday(Dates, label = TRUE, abbr = FALSE, locale = "en") %>% as.character(),
         Time = as_hms(Dates) %>% as.POSIXct()) %>%
  select(-Dates)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE