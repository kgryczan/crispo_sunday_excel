library(tidyverse)
library(readxl)

path = "files/2025-09-14/challenge 60.xlsx"
input = read_excel(path, range = "B2:B18")
test  = read_excel(path, range = "D2:E9")

result = input %>%
  mutate(Stem = Quantity %/% 10, 
         Leaf = Quantity %% 10) %>%
  arrange(Stem, Leaf) %>%
  summarise(Leaf = paste(Leaf, collapse = " "), .by = Stem) 
  
all.equal(result, test)
# [1] TRUE