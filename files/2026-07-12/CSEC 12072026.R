library(tidyverse)
library(readxl)
library(Rmpfr)
options(scipen = 29)

path <- "2026-07-12/Challenge 391.xlsx"
input <- read_excel(path, range = "B3:E6", col_types = "text")
test <- read_excel(path, range = "G3:G6")

result <- input %>%
  mutate(
    total = pmap_chr(
      across(c(`Initial Value`, `Add 1`, `Add 2`, `Add 3`)),
      \(...) {
        c(...) %>%
          as.character() %>%
          mpfr(precBits = 128) %>%
          sum() %>%
          formatMpfr(digits = 22, scientific = FALSE)
      }
    )
  )

# VIsually compared. 1 and 2 correct. No 3. incorrect answer provided.
