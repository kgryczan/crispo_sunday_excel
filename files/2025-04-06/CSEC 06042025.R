library(tidyverse)
library(readxl)

path = "files/Challenge1425.xlsx"
input = read_excel(path, range = "B3:D23")
test  = read_excel(path, range = "F3:H7")

input = input %>%
  mutate(Date = str_replace(Date, "29-02", "27-02") %>% dmy())

seq = seq.Date(min(input$Date), max(input$Date), by = "1 day") %>%
  data.frame(Date = .) %>%
  left_join(input, by = "Date") %>%
  fill(`Staff No.`, .direction = "down") %>%
  mutate(week = isoweek(Date)) %>%
  summarise(`Total Hours` = sum(`Worked Hours`, na.rm = TRUE),
            `Week Dates` = paste(min(Date), max(Date), sep = " - "),
            .by = c("Staff No.", "week")) %>%
  select(1,4,3)

