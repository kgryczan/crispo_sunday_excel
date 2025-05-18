library(tidyverse)
library(readxl)

path = "files/2025-05-18/Challenge24.xlsx"
start = 2
end = 7
skip = 4
repetition = 3
test = read_excel(path, range = "G3:G18")

result = data.frame(List = rep(setdiff(start:end, skip), each = repetition))

all.equal(result, test, check.attributes = FALSE)
#> [1] TRUE
