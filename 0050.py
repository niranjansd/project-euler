# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import numpy as np

def SieveOfEratosthenes(n = 1000000):
    prime = [True for i in range(n + 1)]
     
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return np.nonzero(prime)[0][2:]

primes = SieveOfEratosthenes(1000000)

sum = 0
limit = 1000000

limit = 1000
maxn = np.sum(np.cumsum(primes)<limit)
ans = 0
for i in range(maxn):
    summ = np.sum(primes[:(maxn-i)])
    start = 0
    end = maxn-1-i
    if summ in primes:
        ans = summ
        print(summ)
        break
    for j in range(1, len(primes)-maxn):
        summ += primes[end+j] - primes[start+j-1]
        if summ > limit:
            break
        if summ in primes:
            ans = summ
            print(summ, j, maxn-i)
            break
    if ans:
        break
