library(tidyverse)
library(readxl)

path = "files/CHALLENGE 1205.xlsx"
input = read_excel(path, range = "B3:B13")
test  = read_excel(path, range = "D3:G7")

result = input %>%
  separate(`SUB-DEPARTMENT NAMES`, into = c("sub_department", "department"), sep = "-", extra = "merge", remove = F) %>%
  mutate(rn = row_number(), .by = sub_department) %>%
  select(-department) %>%
  pivot_wider(names_from = sub_department, values_from = `SUB-DEPARTMENT NAMES`) %>%
  select(-rn)

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE