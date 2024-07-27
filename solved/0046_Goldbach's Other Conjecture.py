#<p>It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.</p>
#\begin{align}
#9 = 7 + 2 \times 1^2\\
#15 = 7 + 2 \times 2^2\\
#21 = 3 + 2 \times 3^2\\
#25 = 7 + 2 \times 3^2\\
#27 = 19 + 2 \times 2^2\\
#33 = 31 + 2 \times 1^2
#\end{align}
#<p>It turns out that the conjecture was false.</p>
#<p>What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?</p>

def isPrime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def Goldbach(num,Primes):
    for prime in Primes:
        for j in range(1,int(((num-prime)/2)**0.5)+1):
            if prime + 2 * j**2 == num:
                return True
    return False

Primes = []
i = 1

while True:
    i += 1
    if i%2 == 0:
        pass
    elif isPrime(i):
        Primes.append(i)
    else:
        if Goldbach(i,Primes) == False:
            break
        
print(f"smallest odd composite is: {i}")