library(tidyverse)
library(readxl)

path = "files/Ex-Challenge 06 2025.xlsx"
input = read_excel(path, range = "B3:D6")
test  = read_excel(path, range = "F3:H14")

result = input %>%
  separate(SNo., into = c("start", "end"), sep = "-", fill = "right", convert = TRUE) %>%
  mutate(SNo. = map2(start, coalesce(end, start), seq)) %>%
  unnest(SNo.) %>%
  select(SNo., Sport, Day)

all.equal(result, test)
#> [1] TRUE
