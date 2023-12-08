data = open("data.txt", "r").read()

sum = 0
basement = -1

for idx, c in enumerate(data) :
    sum += (c  == "(") - (c == ")")
    if basement == -1 and sum == -1 :
        basement = idx + 1

print("p1:",sum)
print("p2:",basement)