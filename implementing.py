import pickle  #this is what adds the colors and their probabilities to the outcomes binary file
names = []
chances = []
outcomes = {}
total = 0
with open("colors.txt","r") as file:
    for line in file:
        names.append(line.replace("/n",""))
chances = []

chances = []

for i in range(1, 225):
    if i <= 12:
        chances.append(1 / (i + 1)) 
    elif i <= 21:
        chances.append(1 / (i * 2))  
    elif i <= 49:
        chances.append(1 / (i * 5)) 
    elif i <= 71:
        chances.append(1 / ((i - 25) * 25))  
    elif i <= 91:
        chances.append(1 / ((i - 70) * 150))
    elif i <= 105:
        chances.append(1 / ((i - 90) * 500))  
    elif i <= 145:
        chances.append(1 / ((i - 105) * 2000)) 
    elif i <= 190:
        chances.append(1 / ((i - 145) * 10000))
    elif i <= 198:
        chances.append(1 / ((i - 190) * 100000))
    elif i <= 206:
        chances.append(1 / ((i - 198) * 400000))
    else:
        chances.append(1 / ((i - 206) * 5000000)) 











chances.append(1/500000000)
chances.append(1/777777777)
chances.append(1/1000000000)
chances.append(1/1000000000000000)
for i in range(228):
    names[i] = names[i].replace("\n","")
for i in range(228):
    outcomes[names[i]] = chances[i]
with open("outcomes.bin","bw") as file:
    pickle.dump(outcomes,file)
print("done")