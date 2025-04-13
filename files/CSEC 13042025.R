library(tidyverse)
library(readxl)

path = "files/1425challenge.xlsx"
input = read_excel(path, range = "B3:D6")
test  = read_excel(path, range = "F3:G6")

result = input %>%
  mutate(start = as.Date(str_replace(Start, "^M", ""), "%m-%Y"),
         end = as.Date(str_replace(End, "^M", ""), "%m-%Y")) %>%
  rowwise() %>%
  mutate(Periods = paste(c(Start, format(seq(start + months(1), end - months(1), by = "1 month"), "M%m-%Y"), End), collapse = "; ")) %>%
  ungroup() %>%
  select(Project, Periods)

all.equal(result, test)
#> [1] TRUE