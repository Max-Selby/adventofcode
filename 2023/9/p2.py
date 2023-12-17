data = open('data.txt').read()
data = data.split("\n")

sum1 = 0
for line in data :
    row = list(map(lambda x: int(x), line.split(" ")))
    
    rows = [row]

    while rows[-1] != [0] * len(rows[-1]) :
        new = []
        for index in range(len(rows[-1]) - 1) :
            new.append(rows[-1][index + 1] - rows[-1][index])
        rows.append(new)

    rr = []
    for i in reversed(rows) :
        n = []
        for p in reversed(i) :
            n.append(p)
        rr.append(n)

    rr[0].append(0)

    for indx, row in enumerate(rr) :
        if indx == 0 :
            continue

        row.append(row[-1] - rr[indx - 1][-1])

    sum1 += rr[-1][-1]

print("p2:",sum1)