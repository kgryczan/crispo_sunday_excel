library(tidyverse)
library(readxl)

path = "files/2025-06-08/Challenge 31.xlsx"
input = read_excel(path, range = "B3:D9")
test = read_excel(path, range = "F3:G5")

result = input %>%
  pivot_longer(cols = -c(1), names_to = "Store", values_to = "Fruit Sale") %>%
  mutate(count = 1) %>%
  summarise(count = sum(count, na.rm = T), .by = c("Store", "Fruit Sale")) %>%
  unite("Fruits Sale", c("Fruit Sale", "count"), sep = ": ") %>%
  summarise(
    `Fruits Sale` = paste(`Fruits Sale`, collapse = ", "),
    .by = "Store"
  )

all.equal(result, test)
# [1] TRUE
