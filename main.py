import random
import pickle
import os
import time
name = []
with open("player.bin","br") as file:
    player = (pickle.load(file))
with open("stats.bin","br") as file:
    stats = (pickle.load(file))
with open("outcomes.bin","br") as file:
    outcomes = pickle.load(file)
    for value in outcomes:
        name.append(value)
def clr():
    os.system("cls")
def getroll():
    rollnum = random.randint(1, 1000000)
    cumulativeprobability = 0
    for rarity, probability in outcomes.items():
        cumulativeprobability += probability * 1000000
        if rollnum <= cumulativeprobability:
            return rarity
    return "common"
while True:
    clr()
    choice = int(input("1: Roll\n2: View inventory\n3: upgrades\n"))
    if choice == 1:
        clr()
        for i in range(20):
            print(random.choice(name))
            time.sleep(0.1)
            clr()
        roll = getroll()
        print(f"You got {roll}")
        time.sleep(2)
        if roll in player:
            player[roll] += 1
        else:
            player[roll] = 1

        with open("player.bin","bw") as file:
            pickle.dump(player,file)
    elif choice == 2:
       for value in player:
           print(f"{value}: {player[value]}")
       print("\nPress enter to return\n")
       input()
    elif choice == 3:
        print("1: roll speed")