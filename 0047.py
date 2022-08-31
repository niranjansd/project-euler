# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

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

def primefactors(num):
    factors = []
    while not num % 2:
        factors.append(2)
        num = num // 2
    primes = [2]

    p = 3
    isprime = True
    while (p <= num+1): 
        for prim in primes:
            if not p%prim:
                isprime = False
                break
        if not isprime:
            continue
        while not num % p:
            factors.append(p)
            # factors[p] = 1
            num = num // p        
        p += 2
        isprime = True
    return factors

primes = SieveOfEratosthenes(1000000)


def consec(nconsec=2, nfactors=2, min=8, max=1000000):
    nums = []
    for i in range(min, max):
        if i in primes:
            nums = []
            continue
        factors = primefactors(i)
        if len(set(factors)) == nfactors:
            nums.append(i)
            if len(nums) == nconsec:
                break
        else:
            nums = []
    return nums

print(consec(4,4))