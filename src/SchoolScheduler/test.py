import pandas as pd
import numpy as np
import random

vals = {'hi':[0,7,0],
        'bye': [4, 0, 1]}
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



# Read the Excel file
# df = pd.read_excel('/home/jw/Documents/teechers.xlsx')

# Print the contents of the DataFrame
print(df.iloc[0].tolist())

print(df.eq(0).all().all())
z = [1,2,3,4,5,6,1]
if z.count(1) > 2:
    print('aaaaaaaaaaaaa')

for i, j in enumerate(z):
    i +=1
    print(i)

print((1,2,3)[1])
print('a')
print(df.sum().sum())