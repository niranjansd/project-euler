# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?


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
palprimes = []
for i in primes:
    s = str(i)
    if s in palprimes:
        continue
    pal = [s]
    sp = s[1:]+s[0]
    if sp == s:
        palprimes += pal
        continue
    while sp != s:
        if int(sp) in primes:
            pal.append(sp)
        sp = sp[1:]+sp[0]
    if len(pal) == len(s):
        palprimes += pal

print(palprimes)
print(len(palprimes))