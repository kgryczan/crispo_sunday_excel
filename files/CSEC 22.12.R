library(tidyverse)
library(readxl)
library(janitor)

path = "files/Excel Challenge 22nd Dec.xlsx"
input = read_excel(path, range = "B3:B7")
test  = read_excel(path, range = "D3:G7")

rows = strsplit(input$Problem, "\r\n")[[1]]

process_row = function(row) {
  words = unlist(strsplit(row, " "))
  non_digits = grep("^[^0-9]+", words, value = TRUE)
  digits = grep("^[0-9]+", words, value = TRUE)
  
  n = length(non_digits)
  
  if (n == 2) {
    customer = non_digits[1]
    item = non_digits[2]
  } else if (n == 3) {
    customer = paste(non_digits[1:2], collapse = " ")
    item = non_digits[3]
  } else if (n == 4) {
    if (grepl("^[A-Z]\\.$", non_digits[2])) {
      customer = paste(non_digits[1:3], collapse = " ")
      item = non_digits[4]
    } else {
      customer = paste(non_digits[1:2], collapse = " ")
      item = paste(non_digits[3:4], collapse = " ")
    }
  }
  
  selling_price = digits[1]
  buying_price = digits[2]
  
  return(c(Customer = customer, Item = item, `Selling Price` = selling_price, `Buying Price` = buying_price))
}

processed_data = map_dfr(rows, ~ as.data.frame(t(process_row(.x)), stringsAsFactors = FALSE))

df = as.data.frame(processed_data, stringsAsFactors = FALSE) %>%
  rownames_to_column() %>%
  select(-1) %>%
  mutate(`Selling Price` = as.numeric(`Selling Price`),
         `Buying Price` = as.numeric(`Buying Price`))

all.equal(df, test, check.attributes = FALSE)
#> [1] TRUE