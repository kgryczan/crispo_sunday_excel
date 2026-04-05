library(tidyverse)
library(readxl)

path <- "2026-04-05/Challenge 110.xlsx"
input1 <- read_excel(path, range = "B2:B3") %>% pull()
input2 <- read_excel(path, range = "C2:C3") %>% pull()
input3 <- read_excel(path, range = "D2:D3") %>% pull()

test1 <- read_excel(path, range = "B5:B22", col_names = FALSE) %>% pull()
test2 <- read_excel(path, range = "C5:C22", col_names = FALSE) %>% pull()
test3 <- read_excel(path, range = "D5:D22", col_names = FALSE) %>% pull()

while (length(test3) > 0 && is.na(tail(test3, n = 1))) {
  test3 <- head(test3, -1)
}

create_sequence <- function(input) {
  input = str_split(input, ",") %>% unlist() %>% as.numeric()
  sequence <- c()
  for (value in input) {
    if (value > 0) {
      sequence <- c(sequence, rep(1, value))
      sequence <- c(sequence, NA)
    } else {
      sequence <- c(sequence, NA, NA)
    }
  }
  if (length(sequence) > 0 && is.na(tail(sequence, n = 1))) {
    sequence <- head(sequence, -1)
  }
  return(sequence)
}

s1 = create_sequence(input1)
s2 = create_sequence(input2)
s3 = create_sequence(input3)

identical(s1, test1) # TRUE
identical(s2, test2) # TRUE
identical(s3, test3) # TRUE
