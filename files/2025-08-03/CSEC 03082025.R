library(tidyverse)
library(readxl)

path = "files/2025-08-03/Challenge 48.xlsx"
input = read_excel(path, range = "A2:H5")
test  = read_excel(path, range = "J1:K4")

result = input %>%
  unite("combined", -c(1), sep = "") %>%
  mutate(combined = str_replace_all(combined, "^0+|0+$", "")) %>%
  mutate(combined = str_replace_all(combined, "(?<=.)(?=.)", ","))

names(result) = c("item", "combined")
names(test) = c("item", "combined")

all.equal(result, test) 
# > [1] TRUE
