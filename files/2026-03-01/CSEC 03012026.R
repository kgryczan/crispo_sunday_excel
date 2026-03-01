library(tidyverse)
library(readxl)
library(igraph)

path <- "2026-03-01/Challenge 105.xlsx"
input <- read_excel(path, range = "B3:E19")
test <- read_excel(path, range = "G3:I7")

edges <- input %>%
  filter(!is.na(`Manager ID`)) %>%
  transmute(from = `Manager ID`, to = `Staff ID`)

g <- graph_from_data_frame(edges, directed = TRUE)

managers <- input %>%
  filter(Position == "Manager")

result <- managers %>%
  mutate(
    vertex = as.character(`Staff ID`),
    all_reports = map(
      vertex,
      ~ ego(g, order = Inf, nodes = .x, mode = "out")[[1]] %>% setdiff(.x)
    ),
    total_n = map_int(all_reports, length),
    direct_n = map_int(vertex, ~ degree(g, v = .x, mode = "out")),
    indirect_n = total_n - direct_n,
    `Direct & Indirect` = paste0(
      direct_n,
      " direct : ",
      indirect_n,
      " Indirect"
    )
  ) %>%
  select(Manager = Name, `Direct & Indirect`, `Total Reports` = total_n)

result
plot(g, vertex.label = V(g)$name, main = "Graph Visualization")
