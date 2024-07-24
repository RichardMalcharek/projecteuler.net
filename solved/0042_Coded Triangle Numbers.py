#<p>The $n$<sup>th</sup> term of the sequence of triangle numbers is given by, $t_n = \frac12n(n+1)$; so the first ten triangle numbers are:
#$$1, 3, 6, 10, 15, 21, 28, 36, 45, 55, \dots$$</p>
#<p>By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is $19 + 11 + 25 = 55 = t_{10}$. If the word value is a triangle number then we shall call the word a triangle word.</p>
#<p>Using <a href="resources/documents/0042_words.txt">words.txt</a> (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?</p>

def openTxt(filename):
    with open(filename, 'r') as datei:
        werte_list = [wert.strip('"') for wert in datei.read().split(',')]
    werte_list_klein = [wert.lower() for wert in werte_list]
    werte_list_klein.sort()
    return werte_list_klein

def wordValue(word):                        #### calculates the word-value and returns the value
    Bib = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26
        }
    value = 0
    for digit in word:
        value += Bib[digit]
    return value

def getTriangleNumbers(upperLimit):
    x=0
    i = 1
    List = []
    while x < upperLimit:
        x = int(0.5*i*(i+1))
        List.append(x)
        i += 1
    return List


words = openTxt("0042_words.txt")
maxlength = 0

for word in words:
    maxlength = max(maxlength, len(word))

ListTriNums = getTriangleNumbers(wordValue("z"*maxlength))
count = 0

for word in words:
    if wordValue(word) in ListTriNums:
        count += 1

print(count)