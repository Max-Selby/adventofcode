data = open('data.txt', 'r').read().strip()
tttt, rrrr = data.split("\n")

tttt = tttt.split(" ")
rrrr = rrrr.split(" ")
times = []
distances = []
for i in tttt :
    if i.isdigit() :
        times.append(int(i))
for i in rrrr :
    if i.isdigit() :
        distances.append(int(i))

#################
        
totals = []

for idx, time in enumerate(times) :
    toBeat = distances[idx]
    wins = []
    for milis_held in range(time) :
        if milis_held * (time - milis_held) > toBeat :
            wins.append(milis_held)
    totals.append(len(wins))

m = 1
for t in totals :
    m *= t

print("p1:", m)
