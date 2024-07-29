#<p>The first two consecutive numbers to have two distinct prime factors are:</p>
#\begin{align}
#14 &amp;= 2 \times 7\\
#15 &amp;= 3 \times 5.
#\end{align}
#<p>The first three consecutive numbers to have three distinct prime factors are:</p>
#\begin{align}
#644 &amp;= 2^2 \times 7 \times 23\\
#645 &amp;= 3 \times 5 \times 43\\
#646 &amp;= 2 \times 17 \times 19.
#\end{align}
#<p>Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?</p>

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

def factorization(num, Primes):
    factors = set()
    while num != 1:       
        for prime in Primes:
            if num%prime != 0:
                continue
            num //= prime
            factors.add(prime)
    return len(factors)

Primes = [2,3,5,7]
conInts = []

i = 7

while True:
    i += 1
    if isPrime(i):
        Primes.append(i)
    factors = factorization(i, Primes)
    if factors == 4:
        conInts.append(i)
    if factors != 4:
        conInts = []
    if len(conInts) == 4:
        break

print(conInts)