library(tidyverse)
library(readxl)

path = "files/Excel Challenge 18th August.xlsx"
input = read_excel(path, range = "B2:D6")

generate_dates <- Vectorize(function(start_date, n) {
  dates <- seq.Date(from = as.Date(start_date), 
                    by = "day", 
                    length.out = n * 2)
})

result = input %>%
  mutate(dates = generate_dates(Start, Days)) %>%
  unnest(dates) %>%
  complete(dates) %>%
  mutate(wday = ifelse(wday(dates) %in% c(1,7), "", "X"),
         dates = str_sub(as.character(dates), 6, 10)) %>%
  mutate(nrow = cumsum(wday == "X"),
         wday = ifelse(nrow > Days, "", wday), 
         .by = Project) %>%
  select(Project, dates, wday) %>%
  pivot_wider(names_from = dates, values_from = wday, values_fill = list(wday = "")) %>%
  select(1:14)

# # A tibble: 4 × 14
#   Project `08-16` `08-17` `08-18` `08-19` `08-20` `08-21` `08-22` `08-23` `08-24` `08-25` `08-26` `08-27` `08-28`
#   <chr>   <chr>   <chr>   <chr>   <chr>   <chr>   <chr>   <chr>   <chr>   <chr>   <chr>   <chr>   <chr>   <chr>  
# 1 A       "X"     ""      ""      "X"     "X"     "X"     X       ""      ""      ""      ""      ""      ""     
# 2 D       "X"     ""      ""      "X"     "X"     "X"     X       "X"     ""      ""      "X"     "X"     "X"    
# 3 B       ""      ""      ""      ""      "X"     "X"     X       "X"     ""      ""      "X"     ""      ""     
# 4 C       ""      ""      ""      ""      ""      ""      X       "X"     ""      ""      "X"     ""      ""     