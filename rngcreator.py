import pickle
outcomes = {}
totalprob = 0
#  with open("outcomes.bin","br") as file:
#      outcomes = pickle.load(file)
#     for value in outcomes:
#        totalprob += outcomes[value]
with open("outcomes.bin","bw") as file:
    while True:
        name = input("Enter new item name:\n")
        if name !="stop":
            chance = float(input("Enter the chance:\n"))
            if chance + totalprob <=1:
               totalprob+=chance
               outcomes[name] = chance
            else:
                print("Error -- total probability is over 100%")
        else:
            break
    pickle.dump(outcomes, file)
