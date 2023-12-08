data = open("data.txt", "r").read()
games = data.split("\n")

sumIDs = 0

mostColors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

for idminusone, game in enumerate(games) :
    allsetsString = game.split(":")[1].strip()

    eachSet = allsetsString.split(";")
    possible = True
    for set in eachSet :
        colors = set.split(",")
        for color in colors :
            number = int(color.strip().split(" ")[0])
            col = color.strip().split(" ")[1]
            
            if number > mostColors[col] :
                possible = False
            
    if (possible) :
        sumIDs += idminusone + 1

print("ans:",sumIDs)