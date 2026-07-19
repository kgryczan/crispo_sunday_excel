library(tidyverse)
library(readxl)

path <- "2026-07-19/Challenge 400.xlsx"
input <- read_excel(path, range = "B3:C12")
test <- read_excel(path, range = "E3:F6") %>%
  mutate(`Stock Out Days` = as.Date(`Stock Out Days`))

zero_runs <- rle(input$`Stock Bal` == 0)
ends <- cumsum(zero_runs$lengths)
starts <- c(1, head(ends, -1) + 1)

result <- tibble(
  `Stock Out Days` = as.Date(input$Date[starts[zero_runs$values]]),
  `Days Out` = zero_runs$lengths[zero_runs$values]
)

all.equal(result, test)
# TRUE
