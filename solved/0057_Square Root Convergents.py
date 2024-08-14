#<p>It is possible to show that the square root of two can be expressed as an infinite continued fraction.</p>
#<p class="center">$\sqrt 2 =1+ \frac 1 {2+ \frac 1 {2 +\frac 1 {2+ \dots}}}$</p>
#<p>By expanding this for the first four iterations, we get:</p>
#<p>$1 + \frac 1 2 = \frac  32 = 1.5$<br>
#$1 + \frac 1 {2 + \frac 1 2} = \frac 7 5 = 1.4$<br>
#$1 + \frac 1 {2 + \frac 1 {2+\frac 1 2}} = \frac {17}{12} = 1.41666 \dots$<br>
#$1 + \frac 1 {2 + \frac 1 {2+\frac 1 {2+\frac 1 2}}} = \frac {41}{29} = 1.41379 \dots$<br></p>
#<p>The next three expansions are $\frac {99}{70}$, $\frac {239}{169}$, and $\frac {577}{408}$, but the eighth expansion, $\frac {1393}{985}$, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.</p>
#<p>In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?</p>


# region complex solution

#from fractions import Fraction
#from sympy import sympify
#
#formula = str(f'1+(1/(2')
#count = 0
#
#for i in range(1,1000+2):
#    formula = f'{formula}' + f'+(1/(2' 
#    finalForm = f'{formula}' + '))' + ')'*(i*2)
#    calcForm = str(finalForm)
#    result = sympify(calcForm)
#    fraction = Fraction(result).limit_denominator()
#    countZ = len(str(fraction)[0:str(fraction).find('/')])
#    countN = len(str(fraction)[str(fraction).find('/')+1:len(str(fraction))])
#    if countZ > countN:
#        count += 1
#
#print(count)

# endregion

Zähler = 3
Nenner = 2
Count = 0

for _ in range(2,1000+1):
    Zähler, Nenner = Zähler + 2* Nenner, Zähler + Nenner
    if len(str(Zähler)) > len(str(Nenner)):
        Count += 1

print(Count)
