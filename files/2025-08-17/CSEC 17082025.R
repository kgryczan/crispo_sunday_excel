library(tidyverse)
library(readxl)

path = "files/2025-08-17/Challenge 51.xlsx"
input = read_excel(path, range = "B2:D3")
test  = read_excel(path, range = "F2:G7")

excel_cols = function(start, end) {
  col = function(i) ifelse(i == 0, "", paste0(col((i - 1) %/% 26), LETTERS[(i - 1) %% 26 + 1]))
  idx = function(x) match(x, map_chr(1:16384, col))
  map_chr(seq(idx(start), idx(end)), col)
}

result = input %>%
  mutate(seq = map2(`From Column`, `To Column`, 
                   ~ excel_cols(.x, .y))) %>%
  unnest(seq) %>%
  mutate(GROUP = (row_number()-1) %/% 3 + 1) %>%
  summarise(COLUMNS = paste0(seq, collapse = ","),
            .by = GROUP) 

all.equal(result$COLUMNS, test$COLUMNS)
# > [1] TRUE