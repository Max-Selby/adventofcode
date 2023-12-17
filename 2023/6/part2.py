data = open('data.txt', 'r').read().strip()
tttt, rrrr = data.split("\n")

tttt = int(tttt.replace(" ", "").split(":")[1])
rrrr = int(rrrr.replace(" ", "").split(":")[1])

totals = []

toBeat = rrrr
wins = []
for milis_held in range(tttt) :
    # print(milis_held)
    if milis_held * (tttt - milis_held) > toBeat :
        wins.append(milis_held)
totals.append(len(wins))

m = 1
for t in totals :
    m *= t

print("p2:", m)
