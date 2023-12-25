data = open("data.txt", "r").read().strip()
data = data.split("\n")

cardStrength = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
}

cardsAndBids = []
fiveOfAKinds, fourOfAKinds, fullHouses, threeOfAKinds, twoPairs, onePairs, highCards = [], [], [], [], [], [], []

for handbid in data :
    hand, bid = handbid.split(" ")
    cards = list(hand)
    
    cardsGroups = [(x, cards.count(x)) for x in set(cards)]
    cardsGroups = sorted(cardsGroups, key=lambda x: x[1], reverse=True)

    numJokers = 0
    numHighestNonJokers = 0
    num_2nd_HighestNonJokers = 0
    for i in cardsGroups :
        if i[0] == 'J' :
            numJokers = i[1]
        else :
            if i[1] >= numHighestNonJokers :
                num_2nd_HighestNonJokers = numHighestNonJokers
                numHighestNonJokers = i[1]
                
    # Five of a kind
    if cardsGroups[0][1] == 5 or (numHighestNonJokers + numJokers == 5) :
        fiveOfAKinds.append((hand, bid))
        continue

    # Four of a kind
    if cardsGroups[0][1] == 4 or (numHighestNonJokers + numJokers == 4) :
        fourOfAKinds.append((hand, bid))
        continue

    # Full house
    if (cardsGroups[0][1] == 3 and cardsGroups[1][1] == 2) or (numHighestNonJokers + numJokers == 3 and num_2nd_HighestNonJokers == 2) :
        fullHouses.append((hand, bid))
        continue

    # Three of a kind
    if cardsGroups[0][1] == 3 or (numHighestNonJokers + numJokers == 3) :
        threeOfAKinds.append((hand, bid))
        continue


    # Two pair
    if cardsGroups[0][1] == 2 and cardsGroups[1][1] == 2 :
        twoPairs.append((hand, bid))
        continue

    # One pair
    if cardsGroups[0][1] == 2 or (numJokers == 1) :
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

print("p2:", totalWinnings)