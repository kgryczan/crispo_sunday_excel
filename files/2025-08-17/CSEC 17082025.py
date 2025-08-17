import pandas as pd
import string

df1 = pd.read_excel("files/2025-08-17/Challenge 51.xlsx", usecols="B:D", skiprows=1, nrows=1)
df2 = pd.read_excel("files/2025-08-17/Challenge 51.xlsx", usecols="F:G", skiprows=1, nrows=6)

def col(i): return "" if i == 0 else col((i-1)//26) + string.ascii_uppercase[(i-1)%26]
def idx(x): return [col(i) for i in range(1,16385)].index(x)+1
def excel_cols(a,b): return [col(i) for i in range(idx(a),idx(b)+1)]

seqs = sum([excel_cols(r['From Column'], r['To Column']) for _,r in df1.iterrows()], [])
groups = [(i//3)+1 for i in range(len(seqs))]
res = (
    pd.DataFrame({'seq': seqs, 'GROUP': groups})
      .groupby('GROUP')['seq']
      .apply(lambda x: ','.join(x))
      .reset_index()
      .rename(columns={'seq': 'COLUMNS'})
)

print(res['COLUMNS'].equals(df2['COLUMNS'])) # True