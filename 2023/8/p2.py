data = open('test.txt', 'r').read()
commands, nodes = data.split("\n\n")

commands = list(commands)
nodes = nodes.split("\n")

nodeDict = {}
revDict = {}

for node in nodes :
    start = node[:3]
    place1 = node[7:][:3]
    place2 = node[12:][:3]
    nodeDict[start] = (place1, place2)
    revDict[(place1, place2)] = start

# -------------------------------------
    
steps = 0

nodesOn = []
for value in nodeDict :
    if value.endswith("A") :
        #nodesOn.append(nodeDict[value])
        nodesOn.append(value)

print(nodesOn)

multiples = []
for node in nodesOn :
    steps = 0
    currentNode = node

    while not currentNode.endswith("Z") :
        steps += 1
        togo = 0 if commands[0] == 'L' else 1
        
        currentNode = nodeDict[currentNode][togo]

        commands.append(commands[0])
        commands.pop(0)
    
    multiples.append(steps)

print("p2: LCM of ",multiples)
