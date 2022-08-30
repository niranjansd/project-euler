# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


import itertools
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

primes = SieveOfEratosthenes(10000)
squares = [i**2 for i in range(1, 1000)]


for i in range(5, 10000, 2):
    if i in primes:
        continue
    works = False
    sum = 0
    i1 = 0
    i2 = 0
    for i1 in primes:
        if i1 > i:
            break
        for i2 in squares:
            if i1+2*i2 > i:
                break
            if i1+2*i2 == i:
                works = True
    if not works:
        break
print(i)