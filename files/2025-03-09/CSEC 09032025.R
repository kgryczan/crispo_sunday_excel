library(tidyverse)
library(readxl)

path = "files/Challenge1025.xlsx"
input = read_excel(path, range = "B3:D11")
test  = read_excel(path, range = "F3:G9")

step  = 5
min = floor(min(input$Qty) / step) * step
max = ceiling(max(input$Qty)/ step) * step


breaks = seq(min, max, by = step)
labels <- c(
  paste0(breaks[1], "-", breaks[2]),
  map2_chr(breaks[-length(breaks)], breaks[-1], ~ paste0(.x + 1, "-", .y))
) %>%
  .[-1]

result = input %>%
  mutate(Qty = cut(Qty, breaks = breaks, labels = labels)) %>%
  summarise(Amount = sum(Amount), .by = Qty)
  

r2 = tibble(`Qty Group` = labels) %>%
  left_join(result, by = c("Qty Group" = "Qty")) %>%
  replace_na(list(Amount = 0))

all.equal(r2, test, check.attributes = FALSE)
#> [1] TRUE