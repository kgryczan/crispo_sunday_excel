library(tidyverse)
library(readxl)
library(lubridate)

path = "files/2025-06-01/Challenge 30.xlsx"
start_date = as.Date("2025-05-01")
work_days = 8
travel_days = 8
test = read_excel(path, range = "F3:G23") %>%
  mutate(Schedule = as.Date(Schedule))

df = data.frame(
  dates = seq.Date(
    from = start_date,
    by = "day",
    length.out = (work_days + travel_days) * 2
  )
)
df1 = df %>%
  mutate(weekend = ifelse(wday(dates) %in% c(7, 1), TRUE, FALSE)) %>%
  mutate(weekend = ifelse(weekend, "Rest", "Work")) %>%
  mutate(work_count = row_number(), .by = weekend) %>%
  mutate(
    work_index = ifelse(
      weekend == "Work" & work_count == work_days + 1,
      row_number(),
      NA
    )
  ) %>%
  fill(work_index, .direction = "downup") %>%
  mutate(weekend = ifelse(row_number() >= work_index, "Travel", weekend)) %>%
  mutate(travel_count = row_number(), .by = weekend) %>%
  filter(travel_count <= travel_days) %>%
  select(Schedule = dates, Activity = weekend)

all.equal(df1, test, check.attributes = FALSE)
# [1] TRUE
