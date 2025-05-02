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

print(input.merge(test, left_index=True, right_index=True))

#                     Customers & Orders  answer Last Correct Order
# 0                  Emily15423Jake56243   56243              56243
# 1       Adrian Order not yet confirmed
# 2                           Amani#2546   #2546              #2546
# 3   25698 -To confirm if correct Order
# 4        Sean235Tyler58614Manito015236  015236             015236
# 5  Orders #564 and #5862 were rejected