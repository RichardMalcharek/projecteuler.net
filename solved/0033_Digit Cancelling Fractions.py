#<p>The fraction $49/98$ is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that $49/98 = 4/8$, which is correct, is obtained by cancelling the $9$s.</p>
#<p>We shall consider fractions like, $30/50 = 3/5$, to be trivial examples.</p>
#<p>There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.</p>
#<p>If the product of these four fractions is given in its lowest common terms, find the value of the denominator.</p>

def duplicate(num):
    seen = set()
    for char in str(num):
        if char in seen:
            return True
        seen.add(char)
    return False

def cancelling(a,b):
    seta = set(char for char in str(a))
    setb = set(char for char in str(b))

    a2 = seta - setb
    b2 = setb - seta

    a2 = int(''.join(a2))
    b2 = int(''.join(b2))

    return a2, b2

numers = []
denos = []
pnummers = 1
pdenos = 1

for a in range(10,98):
    for b in range(a+1,100):
        if duplicate(a) == True or duplicate(b) == True or "0" in str(a) or "0" in str(b):
            continue
        if set(str(a)).intersection(set(str(b))) and set(str(a)) != set(str(b)):
            a2, b2 = cancelling(a,b)
            if a/b == a2/b2:
                numers.append(a)
                denos.append(b)
                pnummers *= a
                pdenos *= b

print(numers)
print(denos)
print(f"{pnummers / (pnummers%pdenos) } / {pdenos/ (pnummers%pdenos)}")