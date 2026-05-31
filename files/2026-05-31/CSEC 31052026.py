import pandas as pd
import re

path = "2026-05-31/Challenge 128.xlsx"
input = pd.read_excel(path, usecols="B", nrows=7, skiprows=1)
test = pd.read_excel(path, usecols="D:E", nrows=7, skiprows=1)

result = (
	input.copy()
	.pipe(lambda df: df.assign(word=df['Sentence'].apply(lambda x: re.findall(r'\b\w+\b', str(x)))))
	.assign(
		**{
			'Longest Word': lambda df: df['word'].apply(lambda x: max(x, key=len) if x else ''),
			'Length': lambda df: df['Longest Word'].apply(len),
		}
	)
	[['Longest Word', 'Length']]
)

print(result.equals(test))
# True