import pandas as pd
import numpy as np

path = "files/2025-07-20/Challenge 45.xlsx"

input1 = pd.read_excel(path, header=None, usecols="B", skiprows=1, nrows=1).iloc[0, 0]
input2 = pd.read_excel(path, header=None, usecols="B:J", skiprows=2, nrows=1).transpose().set_axis(["Data"], axis=1)
test = pd.read_excel(path, header=None, usecols="B:J", skiprows=3, nrows=1).transpose().set_axis(["res"], axis=1)

def reset_tracker(data, threshold):
    running, counter, result = 0, 0, []
    for value in data:
        running += value
        if running >= threshold:
            counter, running = counter + 1, 0
        result.append(counter if running == 0 else running)
    return result

result = reset_tracker(input2["Data"], input1)

print(result == test['res'].tolist()) #True
