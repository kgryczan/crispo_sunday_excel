library(tidyverse)
library(readxl)
library(lubridate)

path <- "2026-06-28/Challenge 299.xlsx"
input <- read_excel(path, range = "B3:D15")
test <- read_excel(path, range = "F3:H15")

start <- as.Date("2026-01-01")
df <- input %>%
  mutate(
    Start = as.Date(NA),
    Finish = as.Date(NA)
  )

while (any(is.na(df$Finish))) {
  for (i in which(is.na(df$Finish))) {
    parent <- df$`Depends On`[i]

    if (is.na(parent) || !is.na(df$Finish[match(parent, df$Task)])) {
      df$Start[i] <- if (is.na(parent)) {
        start
      } else {
        df$Finish[match(parent, df$Task)] + 1
      }
      df$Finish[i] <- df$Start[i] + df$`Duration (Days)`[i] - 1
    }
  }
}

result <- df %>%
  select(-`Depends On`, -`Duration (Days)`) %>%
  mutate(across(c(Start, Finish), as.POSIXct))

all.equal(result, test, check.attributes = FALSE)
# True
