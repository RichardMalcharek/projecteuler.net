#<p>If the numbers $1$ to $5$ are written out in words: one, two, three, four, five, then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total.</p>
#<p>If all the numbers from $1$ to $1000$ (one thousand) inclusive were written out in words, how many letters would be used? </p>
#<br><p class="note"><b>NOTE:</b> Do not count spaces or hyphens. For example, $342$ (three hundred and forty-two) contains $23$ letters and $115$ (one hundred and fifteen) contains $20$ letters. 
# The use of "and" when writing out numbers is in compliance with British usage.</p>

Bib1 = {
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
}

Bib2 = {
    '10':'ten',
    '11':'eleven',
    '12':'twelve',
    '13':'thirteen',
    '14':'fourteen',
    '15':'fifteen',
    '16':'sixteen',
    '17':'seventeen',
    '18':'eighteen',
    '19':'nineteen'
}

Bib2b = {
    '2':'twenty',
    '3':'thirty',
    '4':'forty',
    '5':'fifty',
    '6':'sixty',
    '7':'seventy',
    '8':'eighty',
    '9':'ninety'
}

Words = []
lim = 1000

def NumbersWord(num):
    if len(str(num)) == 4:
        Word = Bib1[str(num)[0]]+'thousand'
        if str(num)[1] != '0':
            Word += Bib1[str(num)[1]]+'hundred'
        if str(num)[2] != '0':
            if str(num)[2] == '1':
                Word += 'and'+Bib2[str(num)[2:4]]
            else:
                Word += 'and'+Bib2b[str(num)[2]]
                if str(num)[3] != '0':
                    Word += Bib1[str(num)[3]]
        elif str(num)[3] != '0':
            Word += 'and'+Bib1[str(num)[3]]

    if len(str(num)) == 3:
        Word = Bib1[str(num)[0]]+'hundred'
        if str(num)[1] != '0':
            if str(num)[1] == '1':
                Word += 'and'+Bib2[str(num)[1:3]]
            else:
                Word += 'and'+Bib2b[str(num)[1]]
                if str(num)[2] != '0':
                    Word += Bib1[str(num)[2]]
        elif str(num)[2] != '0':
            Word += 'and'+Bib1[str(num)[2]]
    if len(str(num)) == 2:
        if str(num)[0] == '1':
            Word = Bib2[str(num)]
        else:
            Word = Bib2b[str(num)[0]]
            if str(num)[1] != '0':
                Word += Bib1[str(num)[1]]
    if len(str(num)) == 1:
        Word = Bib1[str(num)]
    return Word
def Count(Words):
    count = 0
    for word in Words:
        count += len(word)
    return count

for num in range(1,lim+1):
    Words.append(NumbersWord(num))

print(f"The length of all number words fron {1} to {lim} is {Count(Words)}")