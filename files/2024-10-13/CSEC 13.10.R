library(tidyverse)
library(readxl)

path = "files/Excel Challenge October 13th.xlsx"
input = read_excel(path, range = "B2:D16")
test  = read_excel(path, range = "F2:G16")

result = input %>%
  fill(Date, .direction = "down") %>%
  group_by(Date) %>%
  mutate(open = first(Units)) %>%
  mutate(Units = ifelse(is.na(Instance) , open + Units, Units)) %>%
  select(Date, Units)

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE