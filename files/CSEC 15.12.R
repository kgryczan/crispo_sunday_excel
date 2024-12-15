library(tidyverse)
library(readxl)
path = "files/Excel Challenge 15th Dec.xlsx"
input = read_excel(path, range = "B2:D8")
test  = read_excel(path, range = "E2:E8")

result = input %>%
  mutate(
    Debt = Expense - `Daily Budget`, 
    Cumulative_Debt = accumulate(Debt, ~ max(.x + .y, 0), .init = 0)[-1]
  )

all.equal(result$Cumulative_Debt, test$`Cumulative Debt`)
#> [1] TRUE