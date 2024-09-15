library(tidyverse)
library(readxl)

path = "files/Excel Challenge September 15th.xlsx"
input = read_excel(path, range = "B2:C9")
test  = read_excel(path, range = "E2:F6") %>% na.omit()

result = input %>%
  mutate(`Salary Range` = cut(x = Salary, 
                      breaks = c(-Inf, 1000, 5000, 10000, 15000, Inf), 
                      labels = c("<1000", "1000 - 4999", "5000 - 9999", "10000 - 14999", "> 15000"))) %>%
  summarise(Staffs = paste0(Staff, collapse = ", "), 
            .by = `Salary Range`)

cbind(result, test)
# identical, order of names in concatenation is different.
