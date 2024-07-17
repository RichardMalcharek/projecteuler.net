#<p>Using <a href="resources/documents/0022_names.txt">names.txt</a> (right click and 'Save Link/Target As...'), 
# a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.</p>
#<p>For example, when the list is sorted into alphabetical order, COLIN, which is worth $3 + 15 + 12 + 9 + 14 = 53$, is the $938$th name in the list. 
# So, COLIN would obtain a score of $938 \times 53 = 49714$.</p>
#<p>What is the total of all the name scores in the file?</p>

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

file = "0022_names.txt"

with open(file, 'r') as datei:
    werte_list = [wert.strip('"') for wert in datei.read().split(',')]
werte_list_klein = [wert.lower() for wert in werte_list]
werte_list_klein.sort()

valueSum = 0
for index, word in enumerate(werte_list_klein):
    value = 0
    for digit in word:
        value += Bib[digit]
    valueSum += value*(index+1)

print(valueSum)