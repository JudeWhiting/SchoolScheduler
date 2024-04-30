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


class teste:
    def __init__(self,hi):
        self.hi = hi


poop = teste(1)
print(poop.hi)
pee = poop
pee.hi = 4
print(poop.hi)
print(pee.hi)

print(any(element in z for element in [7,8,9,10,11,4]))

def fart():
    df.iloc[1,1] = 100


fart()
print(df)

for x in range(100):
    print(x)
    x = x%5
    print(x)

print(max([1,2,3,4,5,5]))
print([1,2,3,5,4,5].index(5))

df.iloc[:, 1] = df.iloc[:, 0]
print(df)

import threading
import time

# Define a function that each thread will execute
def task(name, delay):
    print(f"Thread {name} started")
    print(delay + 100)  # Simulate some task that takes time
    print(f"Thread {name} finished")

# Create multiple threads
threads = []
for i in range(3):
    t = threading.Thread(target=task, args=(i, 2))  # Each thread will execute 'task' function with arguments
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All threads have finished")

df = pd.DataFrame({
    'hi': [1,2,3],
    'bye' : [4,5,6],
    'wee' : [7,8,9],
})

df.loc[1,'hi'] = 3
print(df)
print(np.where([0,0,0,1] == 0)[0])