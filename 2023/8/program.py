data = open('data.txt', 'r').read()
commands, nodes = data.split("\n\n")

commands = list(commands)
nodes = nodes.split("\n")

nodeDict = {}

for node in nodes :
    start = node[:3]
    place1 = node[7:][:3]
    place2 = node[12:][:3]
    nodeDict[start] = (place1, place2)

# -------------------------------------
    
steps = 0
nodeOn = nodeDict["AAA"]

while nodeOn != nodeDict["ZZZ"] :
    steps += 1
    togo = 0 if commands[0] == 'L' else 1
    
    nodeOn = nodeDict[nodeOn[togo]]

    commands.append(commands[0])
    commands.pop(0)

print("p1:",steps)