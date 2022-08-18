# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right, and
# remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from
# left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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

tprimes = []
for p in primes:
    s = str(p)
    if len(s) == 1:
        continue
    tp = True
    for i in range(1, len(s)):
        if int(s[i:]) not in primes:
            tp = False
            break
        if int(s[:-i]) not in primes:
            tp = False
            break
    if tp:
        tprimes.append(p)

print(tprimes)
print(sum(tprimes))
