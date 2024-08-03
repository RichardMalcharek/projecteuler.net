#<p>In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:</p>
#<ul><li><b>High Card</b>: Highest value card.</li>
#<li><b>One Pair</b>: Two cards of the same value.</li>
#<li><b>Two Pairs</b>: Two different pairs.</li>
#<li><b>Three of a Kind</b>: Three cards of the same value.</li>
#<li><b>Straight</b>: All cards are consecutive values.</li>
#<li><b>Flush</b>: All cards of the same suit.</li>
#<li><b>Full House</b>: Three of a kind and a pair.</li>
#<li><b>Four of a Kind</b>: Four cards of the same value.</li>
#<li><b>Straight Flush</b>: All cards are consecutive values of same suit.</li>
#<li><b>Royal Flush</b>: Ten, Jack, Queen, King, Ace, in same suit.</li>
#</ul><p>The cards are valued in the order:<br>2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.</p>
#<p>If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.</p>
#<p>Consider the following five hands dealt to two players:</p>
#<div class="center">
#<table><tr><td><b>Hand</b></td><td> </td><td><b>Player 1</b></td><td> </td><td><b>Player 2</b></td><td> </td><td><b>Winner</b></td>
#</tr><tr><td><b>1</b></td><td> </td><td>5H 5C 6S 7S KD<br><div class="smaller">Pair of Fives</div></td><td> </td><td>2C 3S 8S 8D TD<br><div class="smaller">Pair of Eights</div></td><td> </td><td>Player 2</td>
#</tr><tr><td><b>2</b></td><td> </td><td>5D 8C 9S JS AC<br><div class="smaller">Highest card Ace</div></td><td> </td><td>2C 5C 7D 8S QH<br><div class="smaller">Highest card Queen</div></td><td> </td><td>Player 1</td>
#</tr><tr><td><b>3</b></td><td> </td><td>2D 9C AS AH AC<br><div class="smaller">Three Aces</div></td><td> </td><td>3D 6D 7D TD QD<br><div class="smaller">Flush  with Diamonds</div></td><td> </td><td>Player 2</td>
#</tr><tr><td><b>4</b></td><td> </td><td>4D 6S 9H QH QC<br><div class="smaller">Pair of Queens<br>Highest card Nine</div></td><td> </td><td>3D 6D 7H QD QS<br><div class="smaller">Pair of Queens<br>Highest card Seven</div></td><td> </td><td>Player 1</td>
#</tr><tr><td><b>5</b></td><td> </td><td>2H 2D 4C 4D 4S<br><div class="smaller">Full House<br>With Three Fours</div></td><td> </td><td>3C 3D 3S 9S 9D<br><div class="smaller">Full House<br>with Three Threes</div></td><td> </td><td>Player 1</td>
#</tr></table></div>
#<p>The file, <a href="resources/documents/0054_poker.txt">poker.txt</a>, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.</p>
#<p>How many hands does Player 1 win?</p>

# region Cards
# Suits
# C
# H
# D
# S

# Values
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# T = 10
# J = 11
# Q = 12
# K = 13
# A = 14

# Ranks
# High Card:            = 0
# One Pair:             = 15
# Two Pairs:            = 16
# Three of a Kind:      = 17
# Straight:             = 18
# Flush:                = 19
# Full House:           = 20
# Four of a Kind:       = 21
# Straight Flush:       = 22
# Royal Flush:          = 23

# endregion        

# region GENERAL FUNCTIONS
def openTxt(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines_lower = [value.strip().lower() for value in lines]
    return lines_lower

def createHands(filename):
    Player1 = []
    Player2 = []
    
    lines = openTxt(filename)
    for line in lines:
        Player1.append([line[0:2], line[3:5], line[6:8], line[9:11], line[12:14]])
        Player2.append([line[15:17], line[18:20], line[21:23], line[24:26], line[27:29]])
    
    return Player1, Player2

def getHandValue(Hand):
    
    ### Dictionary to get Cards Value und Value of Rank
    RankDic = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            't': 10,
            'j': 11,
            'q': 12,
            'k': 13,
            'a': 14
        }
    
    #### Get Value for each Card in sorted List
    CardValues = [RankDic[Hand[0][0]], RankDic[Hand[1][0]], RankDic[Hand[2][0]], RankDic[Hand[3][0]], RankDic[Hand[4][0]]]
    CardValues.sort()


    ### identifie Ranks and value of Rank
    values = str(Hand[0][0]) + str(Hand[1][0]) + str(Hand[2][0]) + str(Hand[3][0]) + str(Hand[4][0])
    suits = str(Hand[0][1]) + str(Hand[1][1]) + str(Hand[2][1]) + str(Hand[3][1]) + str(Hand[4][1])

    if findRoyalFlush(CardValues, suits) != False:          # Royal Flush
        rank = 23 + findRoyalFlush(CardValues, suits)/100
        #print(f'{Hand} =  Royal Flush ranked: {rank} ') 
    elif findStraightFlush(CardValues,suits) != False:      # Straight Flush
        rank = 22 + findStraightFlush(CardValues,suits)/100
        #print(f'{Hand} =  Straigt Flush ranked: {rank} ') 
    elif findFourofaKind(values) != False:                  # Four of a kind
        rank = 21 + RankDic[findFourofaKind(values)]/100
        #print(f'{Hand} = Four of a Kind ranked: {rank} ') 
    elif findFullHouse(values,RankDic) != False:            # Full House                     eventuell nachkommastellen korrigieren !!!     
        rank = 20 + findFullHouse(values,RankDic)/10000
        #print(f'{Hand} = Full House ranked: {rank} ') 
    elif findFlush(suits, CardValues) != False:             # Flush
        rank = 19 + findFlush(suits, CardValues)/100
        #print(f'{Hand} = Flush ranked: {rank} ') 
    elif findStraight(CardValues) != False:                 # Straight
        rank = 18 + findStraight(CardValues)/100
        #print(f'{Hand} = Straight ranked: {rank} ')   
    elif findThreeofaKind(values) != False:        # Three of a Kind
        rank = 17 + RankDic[findThreeofaKind(values)]/100
        #print(f'{Hand} = Three of a Kind ranked: {rank} ')     
    elif findTwoPair(values, RankDic) != False:             # Two Pais
        rank = 16 + findTwoPair(values, RankDic)/100
        #print(f'{Hand} = Two Pairs ranked: {rank} ')
    elif findPair(values) != False:                # One Pair
        rank = 15 + RankDic[findPair(values)]/100
        #print(f'{Hand} = One Pair ranked: {rank} ')
    else:                                                   # Nothing
        rank = 0
        #print(f'{Hand} = NOTHING: {rank} ')

    return rank, CardValues

# endregion

# region FIND RANKS
def findRoyalFlush(CardValues, suits):
    if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        if CardValues[0]+4 == CardValues[1]+3 == CardValues[2]+2 == CardValues[3]+1 == CardValues[4] == 14:
            return CardValues[4]
    return False

def findStraightFlush(CardValues, suits):
    if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        if CardValues[0]+4 == CardValues[1]+3 == CardValues[2]+2 == CardValues[3]+1 == CardValues[4]:
            return CardValues[4]
    return False

def findFourofaKind(Values):
    for char in Values:
        if Values.count(char) == 4:
            return char
    return False

def findFullHouse(Values, dict):
    if findThreeofaKind(Values,) != False:
        char = findThreeofaKind(Values)
        maxValue = dict[char]
        Values = Values.replace(char,'')
        if findPair(Values) != False:
            maxValue = int(str(maxValue)+str(dict[findPair(Values)]))
            return maxValue
    return False

def findFlush(suits, CardValues):
    if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        return max(CardValues)
    return False

def findStraight(CardValues):
    if CardValues[0]+4 == CardValues[1]+3 == CardValues[2]+2 == CardValues[3]+1 == CardValues[4]:
        return CardValues[4]
    return False

def findThreeofaKind(Values):
    for char in Values:
        if Values.count(char) == 3:
            return char
    return False
    
def findTwoPair(Values, dict):
    maxpair = 0
    for char in Values:
        if Values.count(char) == 2:
            maxpair = dict[char]
            Values = Values.replace(char,'')
            break
    if maxpair != 0:
        for char in Values:
            if Values.count(char) == 2:
                maxpair = max(maxpair, dict[char])
                return maxpair
    return False

def findPair(Values):
    for char in Values:
        if Values.count(char) == 2:
            return char
    return False

# endregion

# region MAIN FUNCTION

### name file 
filename = '0054_poker.txt'

### create Handy for each Player
Player1, Player2 = createHands(filename)

### run through Hands and identifie winner
CountP1 = 0
CountP2 = 0
for i in range(0,len(Player1)):
    P1Rank, P1Values = getHandValue(Player1[i])
    P2Rank, P2Values = getHandValue(Player2[i])
   
    if P1Rank > P2Rank:
        CountP1 += 1
    elif P1Rank < P2Rank:
        CountP2 += 1
    else:
        for x in range(4,-1,-1):
            if P1Values[x] > P2Values[x]:
                CountP1 += 1
                break
            elif P1Values[x] < P2Values[x]:
                CountP2 += 1
                break

print(f'Ergebnis: P1: {CountP1} vs. P2: {CountP2} ( = {CountP1+CountP2} )')

# endregion
