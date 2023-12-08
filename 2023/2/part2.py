data = open("data.txt", "r").read()
games = data.split("\n")

totalPower = 0
for game in games :
    allsetsString = game.split(":")[1].strip()

    eachSet = allsetsString.split(";")

    mostColors = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for set in eachSet :
        colors = set.split(",")
        for color in colors :
            number = int(color.strip().split(" ")[0])
            col = color.strip().split(" ")[1]

            if number > mostColors[col] :
                mostColors[col] = number
    
    power = mostColors["red"] * mostColors["green"] * mostColors["blue"]
    totalPower += power

print("ans:",totalPower)