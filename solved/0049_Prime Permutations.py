#<p>The arithmetic sequence, $1487, 4817, 8147$, in which each of the terms increases by $3330$, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the $4$-digit numbers are permutations of one another.</p>
#<p>There are no arithmetic sequences made up of three $1$-, $2$-, or $3$-digit primes, exhibiting this property, but there is one other $4$-digit increasing sequence.</p>
#<p>What $12$-digit number do you form by concatenating the three terms in this sequence?</p>

def isPrime(num):                           #### if num is Prime returns True, else False
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def getPrimeList(start,ending):
    Primes = []
    for i in range(start,ending+1):
        if isPrime(i):
            Primes.append(i)
    return Primes

def getconPerms(i, x, Primes):
    P1 = Primes[i]
    P2 = None
    while P2 == None:
        x += 1
        if set(str(Primes[i])) == set(str(Primes[x])):
            P2 = Primes[x]

    return P1, P2, x

Primes = getPrimeList(1000,9999)
i = -1

while i< len(Primes):
    i += 1    
    x = i
    while True:
        try:
            P1, P2, x = getconPerms(i, x, Primes)
            P3 = P2 + (P2-P1)
            if isPrime(P3) and set(str(P3)) == set(str(P1)) and len(str(P3)) == 4:
                print(f"Candidates: {P1} : {P2} : {P3}")
                print(f"joint: {P1}{P2}{P3}")
        except:
            break

