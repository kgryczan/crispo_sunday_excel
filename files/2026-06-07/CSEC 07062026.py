import pandas as pd
import networkx as nx

path = "2026-06-07/Challenge 134.xlsx"
input = pd.read_excel(path, usecols="B:C", nrows=13, skiprows=1)
test = pd.read_excel(path, usecols="E:G", nrows=13, skiprows=1).fillna("")

edges = (
    input.dropna(subset=["Depends On"])
    .assign(**{"Depends On": lambda x: x["Depends On"].str.split(",")})
    .explode("Depends On")
    .assign(**{"Depends On": lambda x: x["Depends On"].str.strip()})
    .query("`Depends On` != ''")
)
G = nx.DiGraph()
G.add_nodes_from(input["Task ID"])
G.add_edges_from(zip(edges["Depends On"], edges["Task ID"]))
result = pd.DataFrame({"Task": input["Task ID"]})
result["Downstream"] = result["Task"].apply(lambda x: sorted(nx.descendants(G, x)))
result["Count"] = result["Downstream"].str.len()
result["Descendants"] = result["Downstream"].apply(", ".join)
result = result[["Task", "Count", "Descendants"]]
print(result.equals(test))
# True
