library(xml2)
library(zip)
library(readxl)

path <- "2026-03-15/Challenge 107.xlsx"

unzip(path, exdir = "xlsx")
sheet <- read_xml("xlsx/xl/worksheets/sheet1.xml")
# creates additional files.
cols <- xml_find_all(sheet, ".//d1:col")
hidden <- xml_attr(cols, "hidden")
hidden = data.frame(hidden) %>%
  na.omit() %>%
  tibble::rownames_to_column("col_index")
cols_to_exclude = as.numeric(hidden$col_index)

df = read_excel(path, range = "A2:I6")
test = read_excel(path, range = "K2:K6")

result = df %>%
  select(-cols_to_exclude) %>%
  select(where(~ !all(is.na(.)))) %>%
  rowwise() %>%
  mutate(Total = sum(c_across(where(is.numeric)), na.rm = TRUE))

all.equal(result$Total, test$Total)
# [1] TRUE
