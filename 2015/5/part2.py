datalines = open("data.txt", "r").readlines()
datalines = list(map(str.strip, datalines))

num = 0

for string_ in datalines :
    passedBetween = False
    passedPairs = False
    
    pairs = []
    for idx in range(len(string_)-1) :
        pairs.append(string_[idx] + string_[idx+1])

    while string_ != "" :
        if len(string_) > 2 and string_[0] == string_[2] :
            passedBetween = True

        string_ = string_[1:]
    
    for idx, pair in enumerate(pairs) :
        for idx2, pair2 in enumerate(pairs) :
            if pair == pair2 and not (idx - idx2) in range(-1,2) : # (not inclusive)
                passedPairs = True
    
    if passedBetween and passedPairs :
        num += 1
    

print("p2:",num)