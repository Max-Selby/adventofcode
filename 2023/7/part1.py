data = open("data.txt", "r").read().strip()
data = data.split("\n")

cardStrength = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1
}

cardsAndBids = []
fiveOfAKinds, fourOfAKinds, fullHouses, threeOfAKinds, twoPairs, onePairs, highCards = [], [], [], [], [], [], []

for handbid in data :
    hand, bid = handbid.split(" ")
    cards = list(hand)

    # Five of a kind
    if len(set(cards)) == 1 :
        fiveOfAKinds.append((hand, bid))
        continue
    
    cardsGroups = [(x, cards.count(x)) for x in set(cards)]
    cardsGroups = sorted(cardsGroups, key=lambda x: x[1], reverse=True)

    # Four of a kind
    if cardsGroups[0][1] == 4 :
        fourOfAKinds.append((hand, bid))
        continue

    # Full house, Three of a kind
    if cardsGroups[0][1] == 3 :
        if cardsGroups[1][1] == 2 :
            fullHouses.append((hand, bid))
        else :
            threeOfAKinds.append((hand, bid))
        continue

    # Two pair, One pair
    if cardsGroups[0][1] == 2 :
        if cardsGroups[1][1] == 2 :
            twoPairs.append((hand, bid))
        else :
            onePairs.append((hand, bid))
        continue

    # High card
    highCards.append((hand, bid))

# ------------------------------------------------------------------------------
# now sort cards based on strength

typesSorted = []
for llist in (fiveOfAKinds, fourOfAKinds, fullHouses, threeOfAKinds, twoPairs, onePairs, highCards) :
    
    stuff = []
    for handbid in llist :
        hand, bid = handbid[0], handbid[1]
        cards = list(hand)

        strengths = list(map(lambda x: cardStrength[x], cards))
        
        stuff.append([strengths, handbid])

    stuff = sorted(stuff)

    stuff = list(map(lambda x: x[1], stuff))

    typesSorted.append(stuff)

totalWinnings = 0
rankk = 1
for kind in reversed(typesSorted) :
    for handd in kind :
        totalWinnings += int(handd[1]) * rankk
        rankk += 1

print("p1:", totalWinnings)