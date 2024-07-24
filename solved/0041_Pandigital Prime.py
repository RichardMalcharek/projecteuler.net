#<p>We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once. For example, $2143$ is a $4$-digit pandigital and is also prime.</p>
#<p>What is the largest $n$-digit pandigital prime that exists?</p>

def isPrime(num):
    i = 5
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

pan = ["0","1","12","123","1234","12345","123456","1234567","12345678","123456789"]

maxPan = 0

for i in range(987654321,8,-1):
    if i%2 == 0 or i % 3 == 0:
        continue
    str_i = str(i)
    if "0" in str_i or len(set(str_i)) != len(str_i):
        continue
    len_i = len(str_i)
    if set(str_i) != set(pan[len_i]):
        continue
    if isPrime(i):
        maxPan = i
        print(maxPan)
        break

print(maxPan)