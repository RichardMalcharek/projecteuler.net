#<p>The number, $1406357289$, is a $0$ to $9$ pandigital number because it is made up of each of the digits $0$ to $9$ in some order, but it also has a rather interesting sub-string divisibility property.</p>
#<p>Let $d_1$ be the $1$<sup>st</sup> digit, $d_2$ be the $2$<sup>nd</sup> digit, and so on. In this way, we note the following:</p>
#<ul><li>$d_2d_3d_4=406$ is divisible by $2$</li>
#<li>$d_3d_4d_5=063$ is divisible by $3$</li>
#<li>$d_4d_5d_6=635$ is divisible by $5$</li>
#<li>$d_5d_6d_7=357$ is divisible by $7$</li>
#<li>$d_6d_7d_8=572$ is divisible by $11$</li>
#<li>$d_7d_8d_9=728$ is divisible by $13$</li>
#<li>$d_8d_9d_{10}=289$ is divisible by $17$</li>
#</ul><p>Find the sum of all $0$ to $9$ pandigital numbers with this property.</p>

from itertools import permutations

ziffern = '0123456789'
pandigital_numbers = permutations(ziffern)

valSum = 0

for pandigital_tuple in pandigital_numbers:
    i = ''.join(pandigital_tuple)
    print(i)
    str_i = str(i)
    if len(set(str_i)) != 10:
        continue
    
    if int(str_i[1:4])%2 !=0:
        continue
    if int(str_i[2:5])%3 !=0:
        continue
    if int(str_i[3:6])%5 !=0:
        continue
    if int(str_i[4:7])%7 !=0:
        continue
    if int(str_i[5:8])%11 !=0:
        continue
    if int(str_i[6:9])%13!=0:
        continue
    if int(str_i[7:10])%17 !=0:
        continue
    
    valSum += int(i)

print(valSum)