#<p>The decimal number, $585 = 1001001001_2$ (binary), is palindromic in both bases.</p>
#<p>Find the sum of all numbers, less than one million, which are palindromic in base $10$ and base $2$.</p>
#<p class="smaller">(Please note that the palindromic number, in either base, may not include leading zeros.)</p>

upperLimit = 999999

def getBase(num):
    binum = ""
    while num > 0:
        if num%2 == 0:
            binum += "0"
        else:
            binum += "1"
        num = num//2
    return binum

sumCount = 0

for i in range(1,upperLimit):
    if str(i) == str(i)[::-1]:
        binum = getBase(i)
        if binum == binum[::-1]:
            sumCount += i

print(sumCount)
