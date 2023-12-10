data = open("data.txt", "r").read().strip()
data = data.split("\n")


total_1 = 0
total_2 = 0
for part in data :
    pairs = part.split(",")
    p1, p2 = pairs[0].split("-"), pairs[1].split("-")
    r1, r2 = range(int(p1[0]), int(p1[1])), range(int(p2[0]), int(p2[1]))

    flag = False
    flag2 = False
    for self_, other_ in [(r1, r2), (r2, r1)] :
        if self_.start <= other_.start and self_.stop >= other_.stop :
            flag = True
        if self_.start >= other_.start and self_.start <= other_.stop :
            flag2 = True
    
    if flag :
        total_1 += 1
    if flag2 :
        total_2 += 1

print("p1:",total_1)
print("p2:",total_2)
