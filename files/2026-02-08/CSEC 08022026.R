library(tidyverse)
library(readxl)

path <- "2026-02-08/Challenge 102.xlsx"
input <- read_excel(path, range = "B2:C13")
test <- read_excel(path, range = "E3:E3", col_names = FALSE) |> pull()

result <- input %>%
  filter(
    str_detect(
      Status,
      regex("(^|[^a-z])complete(d)?([^a-z]|$)", ignore_case = TRUE)
    ),
    str_detect(Status, regex("(^|[^a-z])ok([^a-z]|$)", ignore_case = TRUE)),
    !str_detect(
      Status,
      regex("not.?ok|risk|hold|incomplete", ignore_case = TRUE)
    )
  ) %>%
  count()

all(result == test)
# [1] TRUE
