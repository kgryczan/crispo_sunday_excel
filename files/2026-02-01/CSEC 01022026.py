import pandas as pd

path = "2026-02-01\\Challenge 101.xlsx"
input1 = pd.read_excel(path, usecols= "B", nrows = 3, skiprows = 2)
input2 = pd.read_excel(path, usecols= "D:E", nrows = 2, skiprows = 1)
test = pd.read_excel(path, usecols= "G", nrows = 7, skiprows = 1)

result = pd.DataFrame({
    'items': [item for i, item in enumerate(input1['Items']) 
              for _ in range(input2.loc[input2['Item:'] == i+1, 'Repeats:'].values[0] 
                           if (i+1) in input2['Item:'].values else 1)]
})

print(result['items'].equals(test['Solution']))
# True