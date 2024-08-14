#<p>A googol ($10^{100}$) is a massive number: one followed by one-hundred zeros; $100^{100}$ is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only $1$.</p>
#<p>Considering natural numbers of the form, $a^b$, where $a, b \lt 100$, what is the maximum digital sum?</p>

maxDigitSum = 0
for a in range(1,100):
    for b in range(1,100):
        num = a**b
        DigitSum = 0
        for digit in str(num):
            DigitSum += int(digit)
        maxDigitSum = max(maxDigitSum, DigitSum)

print(maxDigitSum)