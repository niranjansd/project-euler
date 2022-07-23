# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?


from math import comb
import numpy as np
def primefactors(num):
    factors = {}
    factors[2] = 0
    while not num % 2:
        # if 2 not in factors:
        factors[2] += 1
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
        factors[p] = 0
        while not num % p:
            # if p not in factors:
            factors[p] += 1
            num = num // p        
        p += 2
        isprime = True
    return factors


def getlenf(n):
    trin = n*(n+1)/2
    pf = primefactors(trin)
    lenf = 1
    for i in pf:
        lenf *= (pf[i]+1)
    return lenf

for i in range(500, 500000):
    lenf = getlenf(i)
    if lenf > 500:
        print(i, i*(i+1)/2, lenf)
        break