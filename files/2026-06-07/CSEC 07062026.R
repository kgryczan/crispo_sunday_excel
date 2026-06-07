library(tidyverse)
library(readxl)
library(igraph)

path <- "2026-06-07/Challenge 134.xlsx"
input <- read_excel(path, range = "B2:C14")
test <- read_excel(path, range = "E2:G14") %>%
  replace_na(list(Descendants = ""))

edges <- input %>%
  filter(!is.na(`Depends On`), `Depends On` != "") %>%
  transmute(from = `Depends On`, to = `Task ID`)
g <- graph_from_data_frame(edges, vertices = input$`Task ID`)
result <- tibble(Task = V(g)$name) %>%
  mutate(
    downstream = map(
      Task,
      ~ subcomponent(g, .x, mode = "out")$name |> setdiff(.x)
    ),
    Count = map_int(downstream, length),
    Descendants = map_chr(downstream, ~ str_c(.x, collapse = ", "))
  ) %>%
  select(Task, Count, Descendants)

all.equal(result, test)
