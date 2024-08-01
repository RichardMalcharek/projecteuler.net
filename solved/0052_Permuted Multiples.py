#<p>It can be seen that the number, $125874$, and its double, $251748$, contain exactly the same digits, but in a different order.</p>
#<p>Find the smallest positive integer, $x$, such that $2x$, $3x$, $4x$, $5x$, and $6x$, contain the same digits.</p>

x = 9
while True:
    x += 1
    if sorted(list(str(x*1))) == sorted(list(str(x*2))) == sorted(list(str(x*3))) == sorted(list(str(x*4))) == sorted(list(str(x*5))) == sorted(list(str(x*6))):
        break

print(x)