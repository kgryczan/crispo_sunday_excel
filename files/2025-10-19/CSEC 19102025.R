library(tidyverse)
library(readxl)

path = "files/2025-10-19/Challenge 71.xlsx"
input = read_excel(path, range = "B2:C6")
test  = read_excel(path, range = "E2:M6")

make_weekly_table = function(input, no_weeks = 15, interval = 6) {
  no_intervals = ceiling(no_weeks / interval)
  result = tibble(Item = input$Item)
  for (i in seq_len(no_intervals)) {
    start = (i - 1) * interval + 1
    end = min(i * interval, no_weeks)
    wk_names = paste0("WK ", start:end)
    result = bind_cols(result, as_tibble(setNames(replicate(length(wk_names), input$Prices, simplify = FALSE), wk_names)))
    if (end < no_weeks)
      result[[paste0("TOTAL ", i)]] = rowSums(result[wk_names])
  }
  result$`GRAND TOTAL` = rowSums(result[paste0("WK ", 1:no_weeks)])
  result
}

all.equal(make_weekly_table(input, no_weeks = 6, interval = 3), test)

