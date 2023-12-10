data = open("data.txt", "r").read().strip()
data = data.split("\n")

total = 0
total2 = 0

for line in data :
    half = int(len(line)/2)
    piece1, piece2 = line[:half], line[half:]
    sP1, sP2 = set(piece1), set(piece2)
    cha = sP1.intersection(sP2)
    cha = cha.pop()
    if cha.isupper() :
        total += ord(cha) - 38
    else :
        total += ord(cha) - 96

for idx in range(0, len(data), 3) :
    piece1, piece2, piece3 = data[idx], data[idx+1], data[idx+2] 
    sP1, sP2, sP3 = set(piece1), set(piece2), set(piece3)
    cha = sP1.intersection(sP2)
    cha = cha.intersection(sP3)
    cha = cha.pop()
    if cha.isupper() :
        total2 += ord(cha) - 38
    else :
        total2 += ord(cha) - 96

print("p1:", total)
print("p2:", total2)