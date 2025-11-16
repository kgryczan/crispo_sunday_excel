library(tidyverse)
library(readxl)

# path <- "path/to/your/file.xlsx" 
# input <- read_excel(path, range = "")
# test  <- read_excel(path, range = "")
# to be replaced when file willbe provided

df <- tribble(
  ~Stock,                                        ~Seller,
  "Spoon Area-2 - Kitchen Item",                 "Aiden",
  "Forks - Dining Item : Silver Colour",         "Adrian",
  "Sofa: Recliner Area-5 - Lounge Item",         "Ericka",
  "King-Bed:Wide - Bedroom Item :Black-Lable",   "Emma"
)
test = tribble(
  ~`Item & Seller`,
  "Kitchen Item: Aiden",        
  "Dining Item: Adrian",        
  "Lounge Item: Ericka",        
  "Bedroom Item: Emma"  
)

result <- df %>%
  mutate(
    Item = str_extract(Stock, "([[:alnum:]_]+)\\s*Item"
  )) %>%
  transmute(`Item & Seller` = glue::glue("{Item}: {Seller}")) %>% 
  mutate(`Item & Seller` = as.character(`Item & Seller`))

all.equal(result, test, check.attributes = FALSE)
