#<p>$n!$ means $n \times (n - 1) \times \cdots \times 3 \times 2 \times 1$.</p>
#<p>For example, $10! = 10 \times 9 \times \cdots \times 3 \times 2 \times 1 = 3628800$,<br>and the sum of the digits in the number $10!$ is $3 + 6 + 2 + 8 + 8 + 0 + 0 = 27$.</p>
#<p>Find the sum of the digits in the number $100!$.</p>


def factorial(num):
    result = 1
    if num == 0 or num == 1:
        return result
    for i in range(1,num+1):
        result *= i
    return result

def Add(num):
    num = factorial(num)
    result = 0
    for i in range(0,len(str(num))):
        result += int(str(num)[i])
    return result

num = 100
print(f"The sum of the digits of the factorial of {num} is {Add(num)}")
