import pandas as pd

path = "files/2025-11-02/Challenge 73.xlsx"
input = pd.read_excel(path, usecols="B:F", skiprows=2, nrows=7)
test = pd.read_excel(path, usecols="H:I", skiprows=2, nrows=3).rename(columns=lambda col: col.replace('.1', ''))
test['Experience'] = test['Experience'].str.replace('-Twitter', '- Twitter', regex=False)

input.columns = [c.strip().lower().replace(' ', '_') for c in input.columns]
input['rn'] = input.groupby('candidate').cumcount() + 1
input['Experience'] = input.apply(
    lambda r: f"{r['rn']}. {r['from_date']}:{r['to_date']} - {r['past__position']} - {r['past__employer']}", axis=1
)
result = input.groupby('candidate')['Experience'].apply('\n'.join).reset_index()
result.columns = ['Candidate', 'Experience']

print(result.equals(test)) # True