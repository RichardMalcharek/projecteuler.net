#<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
#<p>What is the largest prime factor of the number $600851475143$?</p>

Number = 600851475143
Primes = []
x = 2

while Number > 1:
    if Number%x == 0:
        Primes.append(x)
        Number //= x
    x += 1

#print(Primes)
print(Primes[len(Primes)-1])