library(tidyverse)
library(readxl)

path = "files/Ex-Challenge 07 2025.xlsx"
input = read_excel(path, range = "B3:B14")
test  = read_excel(path, range = "D3:D18")

result = input %>%
  mutate(group = cumsum(c(1, diff(Staff) < 0)),
         Staff  = as.character(Staff)) %>%
  group_by(group) %>%
  group_split() %>%
  imap_dfr(~ {
    dynamic_row <- tibble(
      Staff = paste("GROUP", .y),
      group = unique(.x$group)
    )
    bind_rows(.x, dynamic_row)
  }) %>%
  select(Groups = Staff)

all.equal(result, test)
# [1] TRUE