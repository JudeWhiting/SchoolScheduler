import pandas as pd
import numpy as np
import random

vals = {'hi':[1,2,3,4,5,2,7,8,9]}
amount = [9,8,7,6,5,4,3,2,1]
ls = []
df = pd.DataFrame(vals)
print(df)
row, col = np.where(df.values == 2)
print(row)
print(col)

for i in range(0):
    print('hiiiii')

df = pd.DataFrame(vals)
ddf = pd.DataFrame()
if df.equals(ddf):
    print('woohoo')