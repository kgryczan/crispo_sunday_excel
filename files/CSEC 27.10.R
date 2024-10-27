library(tidyverse)
library(readxl)

path = "files/Excel Challenge October 27th.xlsx"
input = read_excel(path, range = "C3:E21")
test  = read_excel(path, range = "G3:H7") %>% na.omit() %>% mutate(Date = as.Date(Date))
threshold = 800

result = input %>%
  group_by(Staff) %>%
  filter(cumsum(Sales) >= threshold) %>%
  slice(1) %>%
  mutate(Date = as.Date(Date)) %>%
  select(Staff, Date) %>%
  arrange(Date)

all.equal(result, test, check.attributes = FALSE)

