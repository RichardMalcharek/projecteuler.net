#<p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
#<p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>

lim =100
x = lim
y = lim
z = 0
max = 0

while x < lim*10:
    while y < lim*10:
        z = x * y
        CharZ = str(z)
        if CharZ == ''.join([CharZ[i] for i in range(len(CharZ)-1, -1, -1)]) and z > max:
            max = z
        y +=1
    x += 1
    y = lim
print(max)