# By replacing the 1st digit of the 2-digit number *3,
# it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit,
# this 5-digit number is the first example having seven primes among the ten generated numbers,
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number
# (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

import time
import numpy as np
import pandas as pd
import collections
import utils

primes = utils.SieveOfEratosthenes(10000000)

# last digit cannot be 2, 4, 5, 6, 8, 0
def prime_replacer(ndigit, nprimes):
    prim5 = primes[(primes < 10**ndigit) & (primes > 10**(ndigit-1))]
    sprim5 = np.array(list(map(str, prim5)))

    ans = {}
    ans[1] = {}
    for i in range(ndigit-1):
        tsprim5 = collections.Counter([s[:i]+s[(i+1):] for s in sprim5])
        a = {k: v for k, v in tsprim5.items() if v >= nprimes}
        if a:
            ans[1] = utils.add_to_dict_list(ans[1], i, a)

    ans[2] = {}
    for i in range(ndigit-1):
        for j in range(ndigit-1):
            if i >= j:
                continue
            tsprim5 = collections.Counter([s[:i]+s[(i+1):j]+s[(j+1):] for s in sprim5 if s[i]==s[j]])
            a = {k: v for k, v in tsprim5.items() if v >= nprimes}
            if a:
                ans[2] = utils.add_to_dict_list(ans[2], str(i)+str(j), a)

    ans[3] = {}
    for i in range(ndigit-1):
        for j in range(i+1, ndigit-1):
            for k in range(j+1, ndigit-1):
                tsprim5 = collections.Counter([s[:i]+s[(i+1):j]+s[(j+1):k]+s[(k+1):]
                                            for s in sprim5 if (s[i]==s[j]) and (s[k]==s[j])])
                a = {k: v for k, v in tsprim5.items() if v >= nprimes}
                if a:
                    ans[3] = utils.add_to_dict_list(ans[3], str(i)+str(j)+str(k), a)
    return {k: v for k, v in ans.items() if len(v)}

print(prime_replacer(5, 7))
print(prime_replacer(6, 8))
