#<p>The prime $41$, can be written as the sum of six consecutive primes:</p>
#$$41 = 2 + 3 + 5 + 7 + 11 + 13.$$
#<p>This is the longest sum of consecutive primes that adds to a prime below one-hundred.</p>
#<p>The longest sum of consecutive primes below one-thousand that adds to a prime, contains $21$ terms, and is equal to $953$.</p>
#<p>Which prime, below one-million, can be written as the sum of the most consecutive primes?</p>

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

def getconPrimes(primeIndex, Primes):

    for i in range(0,primeIndex):
        num = Primes[primeIndex]
        count = 0
        x = i

        twoTrue = False

        while num > 0:
            if num - Primes[x] < 0:
                break
            else:
                num -= Primes[x]
                if Primes[x] == 2:
                    twoTrue = True
                x +=1
                count += 1
        if num == 0:    
            return count, twoTrue
    return 0, False

print("get Prime-List")
Primes = getPrimeList(0, 1000000)

maxPrime = 0
maxlength = 0

print("start searching")
for i in range(len(Primes)-1,0, -1):
    print(f"checking prime {Primes[i]} | progress: {((len(Primes)-i)/len(Primes))*100} %")
    length, twoTrue = getconPrimes(i,  Primes)
    if length > maxlength:
        maxlength = length
        maxPrime = Primes[i]
    if twoTrue == True:
        break

print(f"Prime {maxPrime} with length {maxlength}")