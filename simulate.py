import pickle
import random
import os
player = {}
with open("outcomes.bin","br") as file:
    outcomes = pickle.load(file)
def clr():
    os.system("cls")
for item in outcomes:
     player[item] = 0
import numpy as np
from scipy.stats import rv_discrete

def getroll(probabilities):
    items = list(probabilities.keys())
    probs = list(probabilities.values())
    probs = np.array(probs)
    probs /= probs.sum()
    custom_dist = rv_discrete(name='custom', values=(range(len(items)), probs))
    chosen_index = custom_dist.rvs(size=1)[0]
    return items[chosen_index]

for i in range(100000):
     value = getroll(outcomes)

     if value in player:
         player[value] += 1
     else:
         player[value] = 1
for value in outcomes:
    print(f"{value}: {outcomes[value]* 100}%")
for items in player:
    print(f"{items}: {player[items]}")