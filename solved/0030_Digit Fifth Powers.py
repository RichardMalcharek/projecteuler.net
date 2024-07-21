#<p>Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#\begin{align}
#1634 &amp;= 1^4 + 6^4 + 3^4 + 4^4\\
#8208 &amp;= 8^4 + 2^4 + 0^4 + 8^4\\
#9474 &amp;= 9^4 + 4^4 + 7^4 + 4^4
#\end{align}
#</p><p class="smaller">As $1 = 1^4$ is not a sum it is not included.</p>
#<p>The sum of these numbers is $1634 + 8208 + 9474 = 19316$.</p>
#<p>Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.</p>

valList =[]

# upper Limit is calculated by hand
# Argument:
# 999.999 = 6 digits long
# 6* 9**5 = 354.294      (highest possible value with 6 digits and powers 5)
# fifth power is longer able to reach the number

upperLimit = 354294
powers = 5

for i in range(2, upperLimit+1):
    val = 0
    for digit in str(i):
        val += int(digit)**powers
    if val == i:
        valList.append(i)

valSum = 0
for val in valList:
    valSum += val

print(valList)
print(valSum)