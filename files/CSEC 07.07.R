library(tidyverse)
library(readxl)

path = "files/Excel Challenge  7th July.xlsx"

input = read_xlsx(path, range = "B3:B20", col_types = "date")
test  = read_xlsx(path, range = "D3:D8")

result = input %>%
  filter((is.na(lag(SALES)) | is.na(lead(SALES))) & (!row_number() %in% c(1, n())))

identical(result$SALES, test$`Before & After Dates`)
#> [1] TRUE