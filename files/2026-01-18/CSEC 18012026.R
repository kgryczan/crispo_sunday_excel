library(tidyverse)
library(readxl)
library(unpivotr)

path <- "2026-01-18/Challenge 99.xlsx"
input <- read_excel(path, range = "B3:K8", col_names = FALSE)
test <- read_excel(path, range = "M4:P8")

names(test) = c(
  "1 lowest offer",
  "1 lowest Cost",
  "2 lowest offer",
  "2 lowest Cost"
)

input_tidy <- input %>%
  select(-1) %>%
  as_cells() %>%
  behead("up", "offer") %>%
  fill(offer) %>%
  behead("up", "val") %>%
  select(-col) %>%
  pivot_wider(names_from = val, values_from = chr) %>%
  arrange(row) %>%
  mutate(Cost = ifelse(Note %in% c("NA") | Cost == 0, "NA", Cost)) %>%
  mutate(rank = rank(as.numeric(Cost), ties.method = "min"), .by = row) %>%
  filter(rank != 3) %>%
  select(row, offer, Cost, rank) %>%
  mutate(offer = ifelse(Cost == "NA", "NA", offer)) %>%
  pivot_wider(names_from = rank, values_from = c(offer, Cost)) %>%
  select(Cost_1, offer_1, Cost_2, offer_2)

names(input_tidy) = c(
  "1 lowest offer",
  "1 lowest Cost",
  "2 lowest offer",
  "2 lowest Cost"
)

all.equal(input_tidy, test, check.attributes = FALSE)
# [1] TRUE
