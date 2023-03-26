# A number chain is created by continuously adding the
# square of the digits in a number to form a new number
# until it has been seen before.
# For example,
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
# Therefore any chain that arrives at 1 or 89 will become stuck in
# an endless loop.
# What is most amazing is that EVERY starting number will eventually
# arrive at 1 or 89.
# How many starting numbers below ten million will arrive at 89?

import numpy as np
s89 = [89]
s1 = [1]

def chain(n, pastn=[], topn=1, s89=s89):
    pastn += [n]
    if n == 1:
        return 1, pastn
    if n in s89:
        return 89, pastn
    if n in s1:
        return 1, pastn
    ni = sum([int(d)**2 for d in str(n)])
    if ni < topn:
        if ni in s1:
            return 1, pastn
        return 89, pastn        
    else:
        return chain(ni, pastn=pastn, topn=topn, s89=s89)

topn = 1
lim = 10000000
len89 = 0
len1 = 0
for i in range(1, lim):
    k, ns = chain(i, pastn=[], topn=topn, s89=s89)
    if i < 1001:
        if k == 89:
            s89 += ns
        else:
            s1 += ns
        if not i % 100:
            s89 = list(set(s89))
            s1 = list(set(s1))
            len89 = len(s89)
            len1 = len(s1)
            topn = i
            if i == 1000:
                topn = 1000
    else:
        if k == 89:
            len89 += 1
        else:
            len1 += 1

print(i, len(s89), len89)
print(i, len(s1), len1)
