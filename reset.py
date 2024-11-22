import pickle
player = {}
outcomes = {}
stats = {"rs":1,"ra":1,"cd":0}
with open("stats.bin","bw") as file:
     pickle.dump(stats,file)
with open("outcomes.bin","br") as file:
     outcomes = pickle.load(file)
with open("colors.txt","r") as file:
     for line in file:
          print(line)
          player[line.replace("\n","")] = 0
     sorted(player.items(), key=lambda x: x[1])
     print("done")
with open("player.bin","bw") as file:
     pickle.dump(player,file)
