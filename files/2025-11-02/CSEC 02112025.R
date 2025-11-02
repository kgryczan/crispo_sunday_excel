library(tidyverse)
library(readxl)
library(glue)
library(janitor)

path = "files/2025-11-02/Challenge 73.xlsx"
input = read_excel(path, range = "B3:F9")
test  = read_excel(path, range = "H3:I6")
test$Experience = str_replace(test$Experience, "-Twitter", "- Twitter")

result = input %>%
  clean_names() %>%
  mutate(rn = row_number(), .by = candidate) %>%
  transmute(
    Candidate = candidate,
    Experience = glue("{rn}. {from_date}:{to_date} - {past_position} - {past_employer}")) %>%
  summarise(Experience = str_c(Experience, collapse = "\r\n"), .by = Candidate)

all.equal(result,test) 
# [1] TRUE