import pandas as pd
import networkx as nx

path = "2026-03-01/Challenge 105.xlsx"
input = pd.read_excel(path, sheet_name="Sheet2", usecols="B:E", skiprows=2, nrows=16)
test = pd.read_excel(path, sheet_name="Sheet2", usecols="G:I", skiprows=2, nrows=4)

df = pd.DataFrame(input, columns=["Staff ID", "Manager ID", "Name", "Position"])
G = nx.DiGraph()
G.add_edges_from(
    df.dropna(subset=["Manager ID"])[["Manager ID", "Staff ID"]].itertuples(index=False)
)
managers = df[df["Position"] == "Manager"]
results = []
for _, row in managers.iterrows():
    manager_id = row["Staff ID"]
    name = row["Name"]
    direct = list(G.successors(manager_id))
    all_reports = nx.descendants(G, manager_id)
    direct_n = len(direct)
    total_n = len(all_reports)
    indirect_n = total_n - direct_n
    results.append({
        "Manager": name,
        "Direct & Indirect": f"{direct_n} direct : {indirect_n} Indirect",
        "Total Reports": total_n
    })
result_df = pd.DataFrame(results)