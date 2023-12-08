import numpy as np

datalines = open("data.txt", "r").readlines()
datalines = list(map(str.strip, datalines))

commandsList = []

cmdss = {
    "turn on ": "on",
    "turn off ": "off",
    "toggle ": "toggle"
}
for line in datalines :
    command = ""
    for cmd in cmdss :
        if line.startswith(cmd) :
            command = cmdss[cmd]
            line = line[len(cmd):]
    p = line.split(" ")
    startyx = tuple(p[0].split(","))
    endyx = tuple(p[2].split(","))

    startyx = tuple(map(lambda x: int(x), startyx))
    endyx = tuple(map(lambda x: int(x), endyx))
    commandsList.append((command, startyx, endyx))

lightsGrid = np.zeros((1000,1000), dtype=bool)

for cmd in commandsList :
    if cmd[0] != "toggle" :
        lightsGrid[cmd[1][0]:cmd[2][0]+1, cmd[1][1]:cmd[2][1]+1] = (cmd[0] == "on")
    else :
        lightsGrid[cmd[1][0]:cmd[2][0]+1, cmd[1][1]:cmd[2][1]+1] = ~lightsGrid[cmd[1][0]:cmd[2][0]+1, cmd[1][1]:cmd[2][1]+1]

print(np.count_nonzero(lightsGrid == True))