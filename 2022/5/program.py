data = open("data.txt", "r").read()

boxesOriginal, commands = data.split("\n\n")
numberOfCols = int(boxesOriginal[-2].strip())

columnsData = [[], [], [], [], [], [], [], [], []]
columnsData_2 = [[], [], [], [], [], [], [], [], []]

boxesOriginal = boxesOriginal.split("\n")
for row in reversed(boxesOriginal[:-1]) :
    for idx in range(1, len(row), 4) :
        if row[idx] != " " :
            columnsData[int((idx-1)/4)].append(row[idx])
            columnsData_2[int((idx-1)/4)].append(row[idx])

for command in commands.split("\n") :
    _, boxesToMove, _, moveFrom, _, moveTo = command.split(" ")
    boxesToMove, moveFrom, moveTo = int(boxesToMove), int(moveFrom), int(moveTo)

    for i in range(boxesToMove) :
        columnsData[moveTo-1].append(columnsData[moveFrom-1][-1])
        columnsData[moveFrom-1] = columnsData[moveFrom-1][:-1]
    
    print(columnsData_2)
    print(moveTo-1)
    columnsData_2[moveTo-1].append(columnsData_2[moveFrom-1][-boxesToMove])
    columnsData_2[moveFrom-1] = (columnsData_2[moveFrom-1][-boxesToMove])

ans_1 = ""
for l in columnsData :
    ans_1 += l[-1]
ans_2 = ""
for l in columnsData_2 :
    ans_2 += l[-1]

print("p1:",ans_1)
print("p2:",ans_2)
