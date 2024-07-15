#<p>Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$).<br>
#If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers.</p>
#<p>For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ and $110$; therefore $d(220) = 284$. The proper divisors of $284$ are $1, 2, 4, 71$ and $142$; so $d(284) = 220$.</p>
#<p>Evaluate the sum of all the amicable numbers under $10000$.</p>


def d(n):
    result = 0
    for i in range(1,n):
        if n%i == 0:
            result += i
    return result

lim = 10000
Count = 0
amiSum = 0

for i in range(1,lim+1):
    j = d(i)
    if i == d(j) and i != j :
        Count += 1
        amiSum += i
        print(f"{i} : {d(i)}")
print(f"Count: {Count} || Sum: {amiSum} ")