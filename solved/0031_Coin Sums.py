#<p>In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:</p>
#<blockquote>1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).</blockquote>
#<p>It is possible to make £2 in the following way:</p>
#<blockquote>1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p</blockquote>
#<p>How many different ways can £2 be made using any number of coins?</p>


coins = [1, 2, 5, 10, 20, 50, 100, 200]
sum = 200

ways = [0] * (sum+1)
ways[0] = 1

for coin in coins:
    for amount in range(coin,sum+1):
        ways[amount] += ways[amount-coin]


print(ways[sum])