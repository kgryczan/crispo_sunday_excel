library(tidyverse)
library(readxl)

path = "files/Excel Challenge September 22nd.xlsx"
input1 = read_excel(path, range = "B3:C11") %>% janitor::clean_names()
input2 = read_excel(path, range = "E3:F12") %>% janitor::clean_names()
test  = read_excel(path, range = "H3:I12")

lookup = input2 %>%
  separate_rows(sub_dept, sep = ", ") %>%
  left_join(input1, by = "sub_dept") %>%
  replace_na(list(x000 = 0)) %>%
  summarise(total = sum(x000), .by = department)

all.equal(test$total, lookup$Total, check.attributes = FALSE)
#> [1] TRUE