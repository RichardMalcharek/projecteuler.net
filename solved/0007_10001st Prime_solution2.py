#<p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, 
# we can see that the $6$th prime is $13$.</p>
#<p>What is the $10\,001$st prime number?</p>

def is_prime(num):
    """ Funktion zur Überprüfung, ob eine Zahl eine Primzahl ist """
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def find_nth_prime(n):
    """ Funktion zur Suche der n-ten Primzahl """
    count = 0
    candidate = 2
    while True:
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate
        candidate += 1

# Finden der 10001. Primzahl
result = find_nth_prime(10001)
print(result)  # Output: 104743
