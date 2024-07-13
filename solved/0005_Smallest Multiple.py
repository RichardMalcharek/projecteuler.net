#<p>$2520$ is the smallest number that can be divided by each of the numbers from 
# $1$ to $10$ without any remainder.</p>
#<p>What is the smallest positive number that is <strong class="tooltip">
# evenly divisible<span class="tooltiptext">divisible with no remainder</span></strong> 
# by all of the numbers from $1$ to $20$?</p>

import math

n = 1
for i in range(1, 21):
    n = abs(n * i) // math.gcd(n, i)

print(n)

