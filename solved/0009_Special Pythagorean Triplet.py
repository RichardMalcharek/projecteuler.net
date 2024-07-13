#<p>A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
#$$a^2 + b^2 = c^2.$$</p>
#<p>For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.</p>
#<p>There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>
# Find the product $abc$.</p>

# a² + b² = c²
# a < b < c
# a + b + c = 1.000
# a * b * c = ???

#example
# 3² + 4² = 5²
# 3 + 4 + 5 = 12
# 3 * 4 * 5 = 48

sum = 1000

for a in range(1,sum):
    for b in range(a+1,sum-a):
        c = sum - a - b
        if (a*a)+(b*b)==(c*c):
            print()
            print(f"{a}² + {b}² = {c}²")
            print(f"{a*a} + {b*b} = {c*c}")
            print(f"{a} + {b} + {c} = {a+b+c}")
            print(f"{a} * {b} * {c} = {a*b*c}")