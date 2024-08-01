#<p>By replacing the 1<sup>st</sup> digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.</p>
#<p>By replacing the 3<sup>rd</sup> and 4<sup>th</sup> digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.</p>
#<p>Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.</p>

def isPrime(num):                           #### if num is Prime returns True, else False
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def replacing(num, target):
    for a in range(0,len(str(num))-2):
        for b in range(a+1,len(str(num))-1):
            for c in range(b+1,len(str(num))):
                minPrime = 0
                count = 0
                for i in range(1,10):
                    newNum = int(str(num)[:a] + str(i) + str(num)[a+1:b] + str(i) + str(num)[b+1:c]+ str(i) + str(num)[c+1:])
                    if isPrime(newNum):
                        count +=1
                        if minPrime == 0:
                            minPrime = newNum 
                result = count >= target
                if result:
                    break
            if result:
                break
        if result:
            break

    return result, minPrime

i = 99
target = 8

while True:
    i += 1
    if isPrime(i) == False and len(str(i))-1 != len(set(str(i))):
        continue
    result, minPrime = replacing(i,target)
    if result == True:
        print(f"result: {minPrime}")
        break
