library(tidyverse)
library(readxl)

path = "files/2025-07-27/CSEC 27072025.xlsx"
input = read_excel(path, range = "B3:N3", col_names = FALSE) %>% t() %>% data.frame(Requirements = .)
test  = read_excel(path, range = "B4:N4", col_names = FALSE) %>% t() %>% data.frame(Test = .)

result = input %>%
  mutate(`New Purchase` = pmax(Requirements - lag(cummax(Requirements),1, default = 0),0))

all.equal(result$`New Purchase`, test$Test, check.attributes = FALSE) 
# > [1] TRUE