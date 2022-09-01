# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
# is unusual in two ways: 
# (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
# exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

import collections
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

primes = primes[primes>1000]

sprimes = ["".join(sorted(str(i))) for i in primes]
sprimescounter = collections.Counter(sprimes)
sprimescounter = {k: v for k, v in sprimescounter.items() if v >= 3}

ans = []
for k in sprimescounter:
    ns = []
    for p in itertools.permutations(k):
        n = int("".join(p))
        if n in primes:
            ns.append(n)
    diffs = [(abs(a -b), min(a, b), max(a,b)) for a, b in itertools.combinations(ns, 2) if a != b]
    diffs = set(diffs)
    diffcounts = collections.Counter([i[0] for i in diffs])
    diffcountmax = max(diffcounts.values())
    diffs = [i for i in diffs if diffcounts[i[0]] >= 2]
    if len(diffs):
        for j in np.unique([i[0] for i in diffs]):
            pairs = [p for p in diffs if p[0] == j]
            for i in range(len(pairs)):
                for j in range(i+1, len(pairs)):
                    if pairs[i][1] in pairs[j] or pairs[i][2] in pairs[j]:
                        ans.append([pairs[i], pairs[j]])
for n in ans:
    print(n)
