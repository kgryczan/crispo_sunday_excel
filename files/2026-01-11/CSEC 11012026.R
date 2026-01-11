library(tidyverse)
library(readxl)

path <- "2026-01-11/Challenge 90.xlsx"
input <- read_excel(path, range = "B4:C12", col_types = c("text", "numeric"))
test <- read_excel(path, range = "F4:G8", col_names = c("Item", "Answer"))

result = input %>%
  summarise(Answer = ifelse(n() > 1, n(), Date), .by = Item) %>%
  arrange(Item)

all.equal(result, test, check.attributes = FALSE)
# First answer is not correct.
