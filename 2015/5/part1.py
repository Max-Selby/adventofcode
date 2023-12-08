datalines = open("data.txt", "r").readlines()

disallowed = ["ab", "cd", "pq", "xy"]
vowelList = ["a", "e", "i", "o", "u"]

num = 0

for string_ in datalines :
    passedDouble = False
    vowels = 0
    ok = True
    while string_ != "" :
        for d in disallowed :
            if string_.startswith(d) :
                ok = False
                string_ = ""
                break
        for vowel in vowelList :
            if string_.startswith(vowel) :
                vowels += 1
        if len(string_) > 1 and string_[0] == string_[1] :
            passedDouble = True
        string_ = string_[1:]
    
    if ok and vowels >= 3 and passedDouble :
        num += 1

print("p1:",num)