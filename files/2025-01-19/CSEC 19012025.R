library(tidyverse)
library(readxl)

path = "files/Ex-Challenge 03 2025.xlsx"
input = read_excel(path, range = "B3:H12")
test  = read_excel(path, range = "J3:L18") %>% arrange(Shop, desc(Sale))

# because R repairs col names I don't have the chance to do it 
# as I wanted. I'll do it another way :D

result = 
  bind_rows(
    input %>% select(1,2,3),
    input %>% select(1,4,5),
    input %>% select(1,6,7)
  ) %>%
  mutate(Fruit = as.factor(Fruit)) %>%
  summarise(Sale = sum(Sale), .by = c(Shop, Fruit))  %>% 
  complete(Shop, Fruit, fill = list(Sale = 0)) %>%
  mutate(Fruit = as.character(Fruit)) %>%
  arrange(Shop, desc(Sale))

all.equal(result, test, check.attributes = FALSE)
# [1] TRUE