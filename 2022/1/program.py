data = open("data.txt", "r").read().strip()
data = data.split("\n\n")

inventories = list(map(lambda x: tuple(map(int, x.split("\n"))), data))

totals = list(map(lambda x: sum(x), inventories))

print("p1:",max(totals))
print("p2:",sum(sorted(totals)[-3:]))