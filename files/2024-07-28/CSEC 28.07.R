library(tidyverse)
library(readxl)

path = "files/Excel Challange 28th July.xlsx"
input = read_excel(path, range = "B3:D11", col_types = "text")
test = read_excel(path, range = "F3:J6", col_types = "text")
colnames(test) = c("Student", "t1", "t2", "t3", "t4")

result = input %>%
  pivot_wider(names_from = "Test", values_from = "Result", values_fill = "exempt")

identical(result, test)
# [1] TRUE