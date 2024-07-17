#<p>A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of $28$ would be $1 + 2 + 4 + 7 + 14 = 28$, which means that $28$ is a perfect number.</p>
#<p>A number $n$ is called deficient if the sum of its proper divisors is less than $n$ and it is called abundant if this sum exceeds $n$.</p>

#<p>As $12$ is the smallest abundant number, $1 + 2 + 3 + 4 + 6 = 16$, the smallest number that can be written as the sum of two abundant numbers is $24$. 
# By mathematical analysis, it can be shown that all integers greater than $28123$ can be written as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.</p>
#<p>Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.</p>

def divsSum(num):
    result = 0
    for i in range(1,num):
        if num%i == 0:
            result += i
    return result

def cat(num):
    div = divsSum(num)
    if div > num:           # abundant
        return True
    else:
        return False
    
lim = 28123
result = 0
abNum = []

for i in range(1,lim+1):
    check = False
    print(i)
    if cat(i) == True:
        abNum.append(i)
    for j in range(1,(i//2)+1):
        if j in abNum and i-j in abNum :
            check = True
            break
    if check == False:
        result += i

print(result)