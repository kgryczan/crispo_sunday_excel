library(tidyverse)
library(readxl)

path = "files/Excel Challenge  22nd June.xlsx"

input = read_xlsx(path, range = "B2:B22", col_types = "text")
test  = read_xlsx(path, range = "D2:D5")

result <- tibble(
  Dates = as.POSIXct(as.Date(as.numeric(input$`Date & Orders`[seq(1, nrow(input), 2)]), 
                             origin = "1899-12-30")),
  Values = as.numeric(input$`Date & Orders`[seq(2, nrow(input), 2)])
) %>%
  filter(Values < lag(Values)) %>%
  select(Dates)

identical(result, test)
# [1] TRUE



