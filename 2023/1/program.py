datalines = open("data.txt", "r").readlines()
sum_1 = 0
sum_2 = 0

textNums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for line in datalines :
    numsSTR_1 = []
    numsSTR_2 = []
    
    while line != "" :
        if line[0].isdigit() :
            numsSTR_1.append(line[0])
            numsSTR_2.append(line[0])
        for idx, tn in enumerate(textNums) :
            if line.startswith(tn) :
                numsSTR_2 += str(idx+1)
        line = line[1:]
    
    sum_1 += int(numsSTR_1[0] + numsSTR_1[-1])
    sum_2 += int(numsSTR_2[0] + numsSTR_2[-1])

print("p1:",sum_1)
print("p2:",sum_2)