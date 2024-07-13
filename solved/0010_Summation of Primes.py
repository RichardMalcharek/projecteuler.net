#<p>The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.</p>
#<p>Find the sum of all the primes below two million.</p>

def is_prime(candidate):
    if candidate <= 1:
        return False
    elif candidate <= 3:
        return True
    elif candidate%2 == 0 or candidate%3 ==0:
        return False
    i = 5
    while i*i <= candidate:
        if candidate%i == 0:
            return False
        i += 1
    return True

lim = 2000000
sum = 0

for i in range(1,lim+1):
    if is_prime(i):
        sum += i
print(sum)

