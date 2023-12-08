data = open("data.txt", "r").read()

santaPos, santaPos2, roboPos2 = [0,0], [0,0], [0,0]

houses = {(0,0)}
houses2 = {(0,0)}

def newPos(pos, c) :
    x, y = pos
    x += (c == ">") - (c == "<")
    y += (c == "^") - (c == "v")
    return [x, y]

for indx, ch in enumerate(data) :
    santaPos = newPos(santaPos, ch)

    houses.add(tuple(santaPos))
    if indx % 2 == 0 :
        santaPos2 = newPos(santaPos2, ch)
        houses2.add(tuple(santaPos2))
    else :
        roboPos2 = newPos(roboPos2, ch)
        houses2.add(tuple(roboPos2))


print("p1:", len(houses))
print("p2:", len(houses2))