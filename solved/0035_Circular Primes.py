#<p>The number, $197$, is called a circular prime because all rotations of the digits: $197$, $971$, and $719$, are themselves prime.</p>
#<p>There are thirteen such primes below $100$: $2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79$, and $97$.</p>
#<p>How many circular primes are there below one million?</p>

def isPrime(num):
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

def move(num,i):
    num = str(num)
    num = int(num[i:]+num[:i])
    return num

def moveChain(num):
    for i in range(0,len(str(num))):
        if isPrime(move(num,i)) == False:
            return False
    return True

upperLimit = 999999
numCircPrime = 0

for i in range(1,upperLimit+1):
    if isPrime(i):
        if moveChain(i) == True:
            numCircPrime += 1
            print(f"found circular prime: {i}")

print(f"found in total: {numCircPrime}")