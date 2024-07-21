#<p>We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once; for example, the $5$-digit number, $15234$, is $1$ through $5$ pandigital.</p>
#<p>The product $7254$ is unusual, as the identity, $39 \times 186 = 7254$, containing multiplicand, multiplier, and product is $1$ through $9$ pandigital.</p>
#<p>Find the sum of all products whose multiplicand/multiplier/product identity can be written as a $1$ through $9$ pandigital.</p>
#<div class="note">HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.</div>


def isPandigital(num):
    strNum = str(num)
    return len(strNum) == 9 and set(strNum) == set("123456789")

valList =[]
valSum = 0

for a in range(1,9999):
    for b in range(a,9999):
        c = a*b
        num = f"{a}{b}{c}"
        if isPandigital(num) == False or c in valList:
            continue
        valList.append(c)
        valSum += c

print(valSum)