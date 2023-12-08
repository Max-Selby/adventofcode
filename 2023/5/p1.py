data = open("data.txt", "r").read().strip()
data = data.split("\n\n")
data = list(map(lambda x: x.split("\n"), data))

seeds = data[0][0][6:].strip().split(" ")
conversions = []

for piece in data[1:] :
    conv = []
    for rang in piece[1:] :
        conv.append(tuple(rang.split(" ")))
    conversions.append(conv)

###############################################
# seeds - list of seeds
# conversions - list of lists (conversion type) of tuples (specific range conversion) in form (destination, source, length)

postConversion = []

for seed in seeds :
    print("starting seed", seed)

    seedNew = int(seed)
    for conversionType in conversions :
        
        for rangeConv in conversionType :
            dest, src, len_ = list(map(lambda x: int(x), rangeConv))
            if seedNew in range(src, src + len_) :
                seedNew += dest - src
                break

    postConversion.append(seedNew)

print("p1:", min(postConversion))