# region Quest
#<p>The $5$-digit number, $16807=7^5$, is also a fifth power. Similarly, the $9$-digit number, $134217728=8^9$, is a ninth power.</p>
#<p>How many $n$-digit positive integers exist which are also an $n$th power?</p>
#
# endregion

import time
import sys

# Grenze für die maximale Anzahl von Ziffern für die Umwandlung festlegen
sys.set_int_max_str_digits(10_000)

start_time = time.time()


#every number 10 or high can not have length = powers               ->  n range(2,10)
# n = 1 or powers = 1 can never end in anything else then 1 or n    ->  p >= 2

count = 0
p = 0

while True:
    p += 1
    for i in range(1,100):
        result = i**p
        if len(str(result)) == p:
            count += 1
            print(f'{i}({p})={result} || p <= {p}: {count}')

print(count)
end_time = time.time()
print(f'\n average runtime: {end_time - start_time}')