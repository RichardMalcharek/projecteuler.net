#<p>Starting with $1$ and spiralling anticlockwise in the following way, a square spiral with side length $7$ is formed.</p>
#<p class="center monospace"><span class="red"><b>37</b></span> 36 35 34 33 32 <span class="red"><b>31</b></span><br>
#38 <span class="red"><b>17</b></span> 16 15 14 <span class="red"><b>13</b></span> 30<br>
#39 18 <span class="red"> <b>5</b></span>  4 <span class="red"> <b>3</b></span> 12 29<br>
#40 19  6  1  2 11 28<br>
#41 20 <span class="red"> <b>7</b></span>  8  9 10 27<br>
#42 21 22 23 24 25 26<br><span class="red"><b>43</b></span> 44 45 46 47 48 49</p>
#<p>It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that $8$ out of the $13$ numbers lying along both diagonals are prime; that is, a ratio of $8/13 \approx 62\%$.</p>
#<p>If one complete new layer is wrapped around the spiral above, a square spiral with side length $9$ will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below $10\%$?</p>


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

def getSpiral(target, size):
    Mx = size
    Matrix = [[None] * Mx for _ in range(Mx)]
    Center = Mx//2
    Matrix[Center][Center] = 1

    Count = 2
    CountPrime = 0
    i = 0

    print(f'start Testing')

    while True and i < Center:
        i += 1
        n = (i*2)+1
        for x in range(+i-1,-i,-1):
            Matrix[Center+x][Center+i] = Count
            Count += 1
        for x in range(i,-i-1,-1):
            Matrix[Center-i][Center+x] = Count
            Count += 1
        for x in range(-i+1,i):
            Matrix[Center+x][Center-i] = Count
            Count += 1
        for x in range(-i,i+1):
            Matrix[Center+i][Center+x] = Count
            Count+=1

        if isPrime(Matrix[Center-i][Center+i]):
            #print(f'{Matrix[Center-i][Center+i]} is prime')
            CountPrime += 1
        if isPrime(Matrix[Center-i][Center-i]):
            #print(f'{Matrix[Center-i][Center-i]} is prime')
            CountPrime += 1
        if isPrime(Matrix[Center+i][Center-i]):
            #print(f'{Matrix[Center+i][Center-i]} is prime')
            CountPrime += 1
        if isPrime(Matrix[Center+i][Center+i]):
            #print(f'{Matrix[Center+i][Center+i]} is prime')
            CountPrime += 1
        
        #print(f'tested n({n}): {CountPrime}/{n*2-1} = {CountPrime/(n*2-1)} ')

        if CountPrime/((n*2)-1) < target:
            print(f'n({n}): {CountPrime}/{n*2-1} = {CountPrime/(n*2-1)} ')
            break
    return

getSpiral(0.1, 30001)