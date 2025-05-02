library(tidyverse)
library(readxl)

path = "files/Excel Challenge Nov 3rd.xlsx"
input = read_excel(path, range = "B3:I8")
test  = read_excel(path, range = "K3:M15")

result = input %>%
  pivot_longer(cols = -c(1), names_to = "Month", values_to = "HC") %>%
  replace_na(list(HC = 0)) %>%
  mutate(Month = my(Month)) %>%
  mutate(Hire = HC - lag(HC, default = 0), .by = Position) %>%
  filter(Hire > 0) %>%
  select(-HC)

all.equal(result, test, check.attributes = FALSE) 
# False, one value is different. Mistake in construction of challenge.
