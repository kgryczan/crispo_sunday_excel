import pandas as pd
import re
import numpy as np

input = pd.read_excel('files/Excel Challenge 2nd June.xlsx', usecols='C', skiprows=1, nrows = 6)
test  = pd.read_excel('files/Excel Challenge 2nd June.xlsx', usecols='D', skiprows=1, nrows = 6)

test['Last Correct Order'] = test['Last Correct Order'].replace(np.nan, '', regex=True)

def extract_after_last_letter(s):
    match = list(re.finditer(r'[A-Za-z]', s))
    if match:
        last_letter_pos = match[-1].end()
        return s[last_letter_pos:] if last_letter_pos < len(s) else ''
    return ''

input['answer'] = input['Customers & Orders'].apply(extract_after_last_letter)

print(input['answer'][0])
print(test['Last Correct Order'][0])

# merge two table column way
print(input.merge(test, left_index=True, right_index=True))

