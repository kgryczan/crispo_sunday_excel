library(tidyverse)
library(readxl)

path <- "2026-05-24/Challenge 122.xlsx"
input <- read_excel(path, range = "B3:B11")
test <- read_excel(path, range = "D3:D11")

get_first_non_duplicate <- function(x) {
  chars <- strsplit(x, "", fixed = TRUE)[[1]]
  chars[which(!duplicated(chars) & !duplicated(chars, fromLast = TRUE))[1]]
}
result = input %>%
  mutate(first_non_duplicate = map_chr(Text, get_first_non_duplicate))

all.equal(result$first_non_duplicate, test$`1st Unique`)
# [1] TRUE
