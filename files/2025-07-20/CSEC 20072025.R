library(tidyverse)
library(readxl)

path = "files/2025-07-20/Challenge 45.xlsx"
input1 = read_excel(path, range = "B2", col_names = FALSE) %>% pull()
input2 = read_excel(path, range = "B3:J3", col_names = FALSE) %>% t() %>% data.frame(Data = .)
test  = read_excel(path, range = "B4:J4", col_names = FALSE) %>% t() %>% data.frame(res = .)

reset_tracker = function(data, threshold) {
  running = 0
  counter = 0
  
  map_dbl(data, function(value) {
    running <<- running + value
    if (running >= threshold) {
      counter <<- counter + 1
      running <<- 0
      return(counter)
    } else {
      return(running)
    }
  })
}

result = input2 %>%
  mutate(res = reset_tracker(Data, input1)) 

all.equal(result$res, test$res)
# > [1] TRUE