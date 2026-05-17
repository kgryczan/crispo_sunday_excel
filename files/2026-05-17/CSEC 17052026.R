library(tidyverse)
library(readxl)

path <- "2026-05-17/Challenge 121.xlsx"
input <- read_excel(path, range = "B3:C15")
test <- read_excel(path, range = "E3:F6")

df <- tibble(
    Date = seq.POSIXt(
        from = min(input$Attendance),
        to = max(input$Attendance),
        by = "day"
    )
) %>%
    filter(wday(Date) %in% c(2:6)) %>%
    crossing(Employee = unique(input$Employee)) %>%
    left_join(
        input %>% mutate(k = 1),
        by = c("Date" = "Attendance", "Employee")
    ) %>%
    arrange(Employee, Date) %>%
    mutate(Group = cumsum(is.na(k)), .by = Employee) %>%
    na.omit() %>%
    mutate(gsize = n(), .by = c(Employee, Group)) %>%
    summarize(
        `Consecutive Streak` = max(if_else(gsize > 1, gsize, 0L)),
        .by = Employee
    )
all.equal(df$`Consecutive Streak`, test$`Consecutive Streak (Work days)`)
# TRUE
