#<p>The number $3797$ has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: $3797$, $797$, $97$, and $7$. Similarly we can work from right to left: $3797$, $379$, $37$, and $3$.</p>
#<p>Find the sum of the only eleven primes that are both truncatable from left to right and right to left.</p>
#<p class="smaller">NOTE: $2$, $3$, $5$, and $7$ are not considered to be truncatable primes.</p>

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


count = 0
sumCount = 0
num = 8
primes = ["2","3","5","7"]
status = True

while count < 11:
    num += 1
    print(f"{count} || {num}")
    status = True
    if isPrime(num) == True:
        if str(num)[0] in primes and str(num)[-1] in primes:
            for i in range(1,len(str(num))):
                if isPrime(int(str(num)[i:len(str(num))]))==False or isPrime(int(str(num)[0:len(str(num))-i]))==False :
                    status = False
            if status == True:
                count += 1
                sumCount += num

print()
print(f"sum: {sumCount}")