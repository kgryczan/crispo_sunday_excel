library(tidyverse)
library(readxl)

input = read_excel("files/Excel Challenge 12th May.xlsx", range = "B3:E13")

result = input %>%
  pivot_longer(cols = -c("Doctors", "Session"), names_to = "Day", values_to = "Patient") %>%
  unite("Appointment", c("Doctors", "Session", "Day"), sep = " - ") %>%
  arrange(Patient, Appointment) %>%
  select(Patient, Appointment)
