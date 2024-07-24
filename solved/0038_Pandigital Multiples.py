#<p>Take the number $192$ and multiply it by each of $1$, $2$, and $3$:</p>
#\begin{align}
#192 \times 1 &amp;= 192\\
#192 \times 2 &amp;= 384\\
#192 \times 3 &amp;= 576
#\end{align}
#<p>By concatenating each product we get the $1$ to $9$ pandigital, $192384576$. We will call $192384576$ the concatenated product of $192$ and $(1,2,3)$.</p>
#<p>The same can be achieved by starting with $9$ and multiplying by $1$, $2$, $3$, $4$, and $5$, giving the pandigital, $918273645$, which is the concatenated product of $9$ and $(1,2,3,4,5)$.</p>
#<p>What is the largest $1$ to $9$ pandigital $9$-digit number that can be formed as the concatenated product of an integer with $(1,2, \dots, n)$ where $n \gt 1$?</p>

def isPandigital(num):                      #### returns "True" if a number is Pandigital. It contains each number 1 - 9 exactly once
    strNum = str(num)
    return len(strNum) == 9 and set(strNum) == set("123456789")

maxCon = 0

for num in range(1,27161):
    con = ""
    i = 1
    while len(con) < 9:
        con += str(num*i)
        i += 1
    if len(con) == 9 and set(con) == set("123456789"):
        maxCon = max(maxCon, int(con))

print(f"found max: {maxCon}")

