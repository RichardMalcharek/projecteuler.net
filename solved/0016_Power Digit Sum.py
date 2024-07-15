#<p>$2^{15} = 32768$ and the sum of its digits is $3 + 2 + 7 + 6 + 8 = 26$.</p>
#<p>What is the sum of the digits of the number $2^{1000}$?</p>

exp = 1000
pot = str(2**exp)
potSum = 0

for digit in range(0,len(pot)):
    potSum += int(pot[digit])

print(f"the sum of the digits of 2^{exp} is {potSum} ")