import random
import pickle
import os
import time
import numpy as np
from scipy.stats import rv_discrete
from colorist import hex
name = []



#load any save data and the dictionary of colors
with open("player.bin","br") as file:
    player = (pickle.load(file))
with open("stats.bin","br") as file:
    stats = (pickle.load(file))
with open("outcomes.bin","br") as file:
    outcomes = pickle.load(file)
    for value in outcomes:
        name.append(value)
with open("hex.bin","br") as file:
    hexdic = pickle.load(file)
#due to rainbow being multicolored it requires its own way of being outputted
red ='\033[0;31m'
orange ='\033[38;5;214m'
yellow ='\033[1;33m'
green ='\033[0;32m'
blue ='\033[0;34m'
indigo ='\033[38;5;57m'
violet ='\033[0;35m'
reset ='\033[0m'

rainbow =f"{red}r{orange}a{yellow}i{green}n{blue}b{indigo}o{violet}w{red} ({orange}1{yellow}/{green}1{blue}0{indigo}0{violet}0{red}0{orange}0{yellow}0{green}0{blue}0{indigo}0{violet}0{red}0{orange}0{yellow}0{green}0{blue}0{indigo}){violet}:{reset}"

global tempoutcomes
tempoutcomes = outcomes
global items
global probs


#make sures the probability math used by the roll function is up to date
def probreset():
    global items,probs
    items = list(tempoutcomes.keys())
    probs = list(tempoutcomes.values())
    probs = np.array(probs)
    probs /= probs.sum()


#clear the console
def clr():
    os.system("cls")


#get the rarity of the item rolled
#chooses a color in outcomes based on the chances given to them
def getroll(probabilities):
    global items,probs, tempoutcomes
    custom_dist = rv_discrete(name='custom', values=(range(len(items)), probs))
    chosenindex = custom_dist.rvs(size=1)[0]
    tempoutcomes = outcomes
    return items[chosenindex]


#save any new data to the binary files
def save():
    with open("player.bin","bw") as file:
       pickle.dump(player,file)
    with open("stats.bin","bw") as file:
       pickle.dump(stats,file)


while True:
    save()
    probreset()
    clr()
    #user will choose from a menu of things to do
    try:
      choice = 0
      cd = stats["cd"]
      ra = stats["ra"]
      print(f"Color drops: {cd}\nRoll amount: {ra}\n")
      choice = int(input(f"{reset}1: Roll\n2: View inventory\n3: upgrades\n4: Roll juicer\n"))
    except ValueError:
        pass


    #choice 1 is rolling
    if choice == 1:
        clr()
        #speed of the roll is based on the rs stat
        if stats["rs"] >= 51:
            speed = 0
        else:
            speed = 51 - stats["rs"]
        for i in range(speed):
            while True:
              rand = random.choice(name)
              if rand != "rainbow":
                  break
            hex(rand,hexdic[rand])
            time.sleep(0.1)
            clr()
        rarestroll = ["",1]
        for j in range(stats["ra"]):
            roll = getroll(outcomes)
            if roll != "rainbow":
               if player[roll] < 100:
                print("You got:")
                hex(f"{roll}(1/{(round(1/outcomes[roll]))})",hexdic[roll])
                print(f"You have gained {round(0.5/outcomes[roll])} color drops")
                stats["cd"] += round(0.5/outcomes[roll])
                if outcomes[roll] < rarestroll[1]:
                    rarestroll = [roll, outcomes[roll]]
                if roll in player:
                  player[roll] += 1
                else:
                  player[roll] = 1  
                                
            else:
                print(f"You got:")
                print(f"{rainbow}!!!!")
                print("You have gained 9999999999999999999999999999999999999999999999 color drops!!!!!")
                stats["cd"] += 9999999999999999999999999999999999999999999999
                player["rainbow"] += 1 
                
        if stats["ra"] >=10 and roll != "rainbow":
            print("\nYour rarest roll was:")
            hex(f"{rarestroll[0]}(1/{(round(1/rarestroll[1]))})",hexdic[rarestroll[0]])
        print("Press enter to continue")
        input()



    #choice 2 shows the user their inventory/stats
    elif choice == 2:
       clr()
       debug = "rainbow"
       with open("colors.txt","r") as file:
          for line in file:
             if line != "rainbow":
                value = line.replace("\n","")
                hex(f"{value} (1/{round(1/outcomes[value])}): {player[value]}",hexdic[value])
          print(f"{rainbow} {player[debug]}")
       print("\nPress enter to return\n")
       input()


    #choice 3 bring up the upgrade menu
    elif choice == 3:
        clr()
        maxed = ""
        if stats["rs"] >= 51:
           maxed = " -- max"
        try:
         print(f"1: roll speed{maxed}\n2: roll amount\n")
        except ValueError:
            pass
        choice = input()
        #choice 1 is to roll faster
        if choice == "1":
           if stats["rs"] < 51:
            try:
              amount = int(input("How many would you like to purchase?\n"))
            except ValueError:
                amount = 1
            cost = stats["rs"] * 32 * amount
            print(f"This will cost {cost} color drops\n(y/n)\n")
            choice = input()
            clr()
            if choice == "y":
                if stats["cd"] <cost:
                    print("Error - insufficient color drops")
                    time.sleep(2)
                    clr()
                else:
                    stats["cd"] -= cost
                    stats["rs"] += 1 * amount
                    print("Transaction complete!")
                    time.sleep(2)
                    clr()
        elif choice == "2":
            try:
              amount = int(input("How many would you like to purchase?\n"))
            except ValueError:
                amount = 1
            cost = stats["ra"] * 124 * amount
            print(f"This will cost {cost} color drops\n(y/n)\n")
            choice = input()
            clr()
            if choice == "y":
                if stats["cd"] <cost:
                    print("Error - insufficient color drops")
                    time.sleep(2)
                    clr()
                else:
                    stats["cd"] -= cost
                    stats["ra"] += 1 * amount
                    print("Transaction complete!")
                    time.sleep(2)
                    clr()
            else:
                pass


    #option 4 allows the user to exchange 25 of a color to remove that color and all above it in rarity, increasing the chance of everything else
    elif choice == 4:
     if tempoutcomes == outcomes:
        print("25 of any color can be exchanged for 1 roll where that color and all above it in rarity are removed.")
        print("(press enter to continue)")
        input()
        clr()
        best = ''
        for key in player:
            if key == "rainbow":
               pass
            elif player[key] >= 25:
                best = key
        print(f"Your rarest avaiable color to juice is: {best}")
        color = input("Please enter a color:\n")
        try:
            if player[color] < 10:
                print("Error -- insufficient amount of color")
                time.sleep(2)
            else:
               if color != "rainbow":
                player[color] -= 10
                tempoutcomes = {}
                for value in outcomes:
                    if outcomes[value] < outcomes[color]:
                        tempoutcomes[value] = outcomes[value]
                print("Transaction complete!")
                time.sleep(2)
                clr()
               else:
                  clr()
                  print("No")
                  time.sleep(2)
                  clr()
        except KeyError:
            print("Error -- Invalid color")
            time.sleep(2)
     else:
        print("Error -- Juicer already active")
        time.sleep(2)
        clr()