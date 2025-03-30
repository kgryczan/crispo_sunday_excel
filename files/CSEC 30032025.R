library(tidyverse)
library(readxl)

path = "files/Challenge1325.xlsx"
input = read_excel(path, range = "B3:D19")
test  = read_excel(path, range = "F3:I17") %>%
  mutate(across(starts_with("Time"), ~hms::as_hms(.))) 

expanded = expand.grid(unique(input$`Staff No.`), unique(input$Date)) %>%
  left_join(input, by = c("Var1" = "Staff No.", "Var2" = "Date")) %>%
  mutate(Time = hms::as_hms(Time)) %>%
  arrange(Var1, Var2, Time) %>% 
  mutate(n = n(),
         rn = row_number(),
         .by = c("Var1", "Var2")) %>%
  filter(rn == 1|rn == n) %>%
  mutate(rn = row_number(), .by = c(Var1, Var2)) %>%
  select(-n) %>%
  pivot_wider(names_from = rn, values_from = Time) %>%
  arrange(Var2, Var1)

colnames(expanded) = colnames(test)
print(expanded)
