library(tidyverse)
library(readxl)

path = "files/2025-05-11/Challenge 23.xlsx"
input = read_excel(path, range = "B2:D28")
test = read_excel(path, range = "F2:G6") %>%
  rename("Quarter" = 1)

result = input %>%
  mutate(Quarter = paste0("Q", quarter(Date))) %>%
  summarise(
    Production = sum(
      `Production (L)`[`Temp (°C)` >= -10 & `Temp (°C)` <= -5],
      na.rm = TRUE
    ),
    .by = Quarter
  )

all.equal(result, test)
#> [1] TRUE
