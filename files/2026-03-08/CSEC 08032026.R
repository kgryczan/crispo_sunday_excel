library(tidyverse)
library(readxl)
library(lubridate)
library(glue)

path <- "2026-03-08/Challenge 106.xlsx"
input <- read_excel(path, range = "B2:D6")
test <- read_excel(path, range = "F2:F6")

result = input %>%
  rowwise() %>%
  mutate(
    Per = period(c(Week, Days) * `Multiply By:`, units = c("week", "day")) %>%
      as.duration() %>%
      as.numeric("days")
  ) %>%
  ungroup() %>%
  mutate(
    Results = glue("Weeks: {floor(Per/7)}   Days: {Per %% 7}") %>%
      as.character()
  )

all.equal(result$Results, test$Results)
# correct but number of spaces between "Weeks:" and "Days:" is different, so not exactly the same as test$Results
