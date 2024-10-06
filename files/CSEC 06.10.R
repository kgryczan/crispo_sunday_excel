library(tidyverse)
library(readxl)

path = "files/Excel Challenge October 6th.xlsx"
input1 = read_excel(path, range = "B2:C5") %>% mutate(id = 1)
input2 = read_excel(path, range = "E2:E6") %>% mutate(id = 1)
test  = read_excel(path, range = "G2:I14") 

result = input1 %>% 
  full_join(input2, by = "id") %>%
  select(Staff, PPE, Size)

all.equal(result, test)
# [1] TRUE