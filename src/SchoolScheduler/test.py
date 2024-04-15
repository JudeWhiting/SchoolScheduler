import pandas as pd
import numpy as np
import random

class poo():
    
    def __init__(self, name):
        self.name = name

pp = poo('hi')
ppp = poo('bye')
bbb = pd.DataFrame([pp, ppp])
print(bbb)
if pp not in bbb:
    print('hi')