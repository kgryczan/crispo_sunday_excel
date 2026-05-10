library(tidyverse)
library(readxl)
library(lubridate)

path <- "2026-05-10/Challenge 120.xlsx"
input <- read_excel(path, range = "B3:D7")
test <- read_excel(path, range = "F3:H7")

result <- transmute(
  input,
  Employee,
  interval = interval(`Start Date`, `End Date`)
)

overlap_pairs <- result |>
  rename(Employee_1 = Employee, interval_1 = interval) |>
  crossing(rename(result, Employee_2 = Employee, interval_2 = interval)) |>
  filter(Employee_1 != Employee_2, int_overlaps(interval_1, interval_2)) |>
  transmute(
    Employee = Employee_1,
    Overlaps = Employee_2,
    dates = map2(
      pmax(int_start(interval_1), int_start(interval_2)),
      pmin(int_end(interval_1), int_end(interval_2)),
      seq,
      by = "day"
    )
  ) |>
  unnest(dates) |>
  summarise(
    Overlaps = str_c(unique(Overlaps), collapse = ", "),
    `Date(s)` = str_c(
      paste(
        month(sort(unique(dates))),
        day(sort(unique(dates))),
        year(sort(unique(dates))),
        sep = "/"
      ),
      collapse = ", "
    ),
    .by = Employee
  ) |>
  right_join(distinct(result, Employee), by = "Employee") |>
  arrange(match(Employee, c("Aiden", "Bob", "Aditya", "Doris")))

all.equal(overlap_pairs, test)
# [1] TRUE
