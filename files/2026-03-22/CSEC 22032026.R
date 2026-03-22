library(tidyverse)
library(readxl)

path <- "2026-03-22/Challenge 108.xlsx"
input1 <- read_excel(path, range = "B2:B4")
input2 <- read_excel(path, range = "B6:B9")
test <- read_excel(path, range = "D2:D14")

result = expand.grid(input1$Mentors, input2$Staff) %>%
  as.matrix() %>%
  t() %>%
  c()

all.equal(result, test$Session)
