#<p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, 
# we can see that the $6$th prime is $13$.</p>
#<p>What is the $10\,001$st prime number?</p>

lim = 10001
prime = [2]
n = 3
check = True

while len(prime) < lim:
    for i in range(2,n):
        if n%i == 0:
            check = False
            break
    if check == True:
        print(f"{n} | pos. {len(prime)+1}")
        prime.append(n)
    n += 1
    check = True
print(f"Ergebnis: {prime[lim-1]}")
