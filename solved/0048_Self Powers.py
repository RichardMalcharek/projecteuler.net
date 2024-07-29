#<p>The series, $1^1 + 2^2 + 3^3 + \cdots + 10^{10} = 10405071317$.</p>
#<p>Find the last ten digits of the series, $1^1 + 2^2 + 3^3 + \cdots + 1000^{1000}$.</p>

sum = 0

for i in range(1,1000+1):
    sum += i**i

print(str(sum)[len(str(sum))-10:len(str(sum))])