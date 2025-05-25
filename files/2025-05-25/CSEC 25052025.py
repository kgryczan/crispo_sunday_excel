import pandas as pd
import re
import string

path = "files/2025-05-25/Challenge25.xlsx"
input = pd.read_excel(path, usecols="B", skiprows=2, nrows=10)
test = pd.read_excel(path, usecols="D", skiprows=2, nrows=3).rename(columns=lambda col: col.replace('.1', ''))

seqs = [string.ascii_lowercase * 2][0]
seqs = [seqs[i:i+4] for i in range(26)]

def has_seq(word):
    return any(re.search(seq, word) for seq in seqs)

result = input[input['Words'].apply(has_seq)][['Words']].reset_index(drop=True)

print(result.equals(test))