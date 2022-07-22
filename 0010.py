# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import numpy as np

def SieveOfEratosthenes(n = 2000000):
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

primes = SieveOfEratosthenes()
print(sum(primes))