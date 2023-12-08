data = open("data.txt", "r").readlines()
data = list(map(str.strip, data))
data = [s.split("x") for s in data]
data = [list(map(int, dim)) for dim in data]

sum_p1 = 0
sum_p2 = 0

for dimensions in data :
    sm = None
    ribbon = None
    for a, b in [(0,1), (0,2), (1,2)] :
        sum_p1 += 2*dimensions[a]*dimensions[b]
        if sm == None or dimensions[a]*dimensions[b] < sm :
            sm = dimensions[a]*dimensions[b]

        if ribbon == None or (2*dimensions[a]) + (2*dimensions[b]) < ribbon :
            ribbon = (2*dimensions[a]) + (2*dimensions[b])
    sum_p2 += ribbon + dimensions[0]*dimensions[1]*dimensions[2]
    sum_p1 += sm

print("p1:",sum_p1)
print("p2:",sum_p2)
