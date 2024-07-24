#<p>If $p$ is the perimeter of a right angle triangle with integral length sides, $\{a, b, c\}$, there are exactly three solutions for $p = 120$.</p>
#<p>$\{20,48,52\}$, $\{24,45,51\}$, $\{30,40,50\}$</p>
#<p>For which value of $p \le 1000$, is the number of solutions maximised?</p>

List = {f'{i}':0 for i in range(3, 1001)}

for a in range (1,998):
    for b in range(1,998-a):
        c = ((a**2) + (b**2))**0.5
        if c%1 == 0 and a+b+c <= 1000:
            p = str(int(a+b+c))
            List[p] += 1

print(f"p = {max(List, key=List.get)}")