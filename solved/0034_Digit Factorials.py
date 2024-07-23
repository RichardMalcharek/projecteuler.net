#<p>$145$ is a curious number, as $1! + 4! + 5! = 1 + 24 + 120 = 145$.</p>
#<p>Find the sum of all numbers which are equal to the sum of the factorial of their digits.</p>
#<p class="smaller">Note: As $1! = 1$ and $2! = 2$ are not sums they are not included.</p>


def factorialSum(num,factorials):
    return sum(factorials[int(digit)] for digit in str(num))

valSum = 0
upperLimit = 2540160        # 9! * 7 = 2.540.160 < 9.999.999

factorials = [1] * 10

for i in range(2,10):
    factorials[i] = factorials[i-1]*i

for i in range(3,upperLimit):
    print(i)
    if i == factorialSum(i,factorials):
        valSum += i

print(valSum)