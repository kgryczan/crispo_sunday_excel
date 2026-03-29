import pandas as pd

path = "Challenge 99.xlsx"
input_data = pd.read_excel(path, usecols="B:K", skiprows=2, nrows=6, header=None)
test = pd.read_excel(path, usecols="M:P", skiprows=3, nrows=5)
test.columns = ["1 lowest offer", "1 lowest Cost", "2 lowest offer", "2 lowest Cost"]

offers = input_data.iloc[0, 1:].tolist()
rows = []
for ridx in range(1, input_data.shape[0]):
    row = input_data.iloc[ridx, 1:].tolist()
    parsed = []
    for offer, value in zip(offers, row):
        cost = str(value)
        if cost == "0" or cost.upper() == "NA":
            cost = "NA"
            offer_name = "NA"
        else:
            offer_name = offer
        parsed.append((offer_name, cost))
    valid = [(o, c) for o, c in parsed if c != "NA"]
    valid = sorted(valid, key=lambda x: float(x[1]))[:2]
    while len(valid) < 2:
        valid.append(("NA", "NA"))
    rows.append({
        "1 lowest offer": valid[0][0],
        "1 lowest Cost": valid[0][1],
        "2 lowest offer": valid[1][0],
        "2 lowest Cost": valid[1][1],
    })

result = pd.DataFrame(rows)
print(result.equals(test))
