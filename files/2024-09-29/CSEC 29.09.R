library(tidyverse)
library(readxl)
library(rebus.datetimes)

path = "files/Excel Challenge September 29th.xlsx"
input = read_excel(path, range = "B2:B6")
test  = read_excel(path, range = "D2:E6")


date_patt = digit(1, 2) %R% "/" %R% digit(1, 2) %R% "/" %R% digit(4,4)
amount_patt = SPACE %R% one_or_more(DIGIT) %R% or(SPACE, END)

result = input %>%
  mutate(Date = str_extract(`Revenues Details`, date_patt) %>% mdy() %>% as.POSIXct(),
         Amount = str_extract(`Revenues Details`, amount_patt) %>% as.numeric()) %>%
  select(-`Revenues Details`)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE