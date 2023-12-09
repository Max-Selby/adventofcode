data = open("data.txt", "r").readlines()
data = list(map(str.strip, data))

points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

elfMoves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors"
}

youMoves = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

win = {
    "rock": "paper",
    "paper": "scissors",
    "scissors": "rock"
}

total_1 = 0
total_2 = 0
for elfM, youM in map(lambda x: x.split(" "), data) :
    if youM == "X" :
        youM2 = list(win.keys())[list(win.values()).index(elfMoves[elfM])]
        score2 = 0
    elif youM == "Y" :
        youM2 = elfMoves[elfM]
        score2 = 3
    else :
        youM2 = win[elfMoves[elfM]]
        score2 = 6
    
    score = points[youMoves[youM]]
    score2 += points[youM2]
    

    if elfMoves[elfM] == youMoves[youM] :
        score += 3
    elif win[elfMoves[elfM]] == youMoves[youM] :
        score += 6
    
    total_1 += score
    total_2 += score2

print("p1:", total_1)
print("p2:", total_2)