library(tidyverse)
library(readxl)

input = read_excel("files/Excel Challenge 2nd June.xlsx", range = "C2:C8")
test  = read_excel("files/Excel Challenge 2nd June.xlsx", range = "D2:D8")

result = input %>%
  mutate(last_letter = map_int(str_locate_all(`Customers & Orders`,
                                              "[A-Za-z]"),
                               ~max(.x[,2]))) %>%
  mutate(answer = ifelse(last_letter < nchar(`Customers & Orders`), 
                         str_sub(`Customers & Orders`, last_letter + 1), 
                         NA_character_))
           
identical(result$answer, test$`Last Correct Order`)         
#> [1] TRUE