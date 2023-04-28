# The primes 3, 7, 109, and 673, are quite remarkable.
# By taking any two primes and concatenating them in any order
# the result will always be prime. For example, taking 7 and 109,
# both 7109 and 1097 are prime. The sum of these four primes, 792,
# represents the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two
#     primes concatenate to produce another prime.
import math
import utils
import time

pmax = 10000
primes = utils.SieveOfEratosthenes(pmax)

def cond(a, b):
    len_a = math.floor(math.log10(a))+1
    len_b = math.floor(math.log10(b))+1
    if utils.isprime(int(a*(10**len_b)+b)) and utils.isprime(int(b*(10**len_a)+a)):
        return True
    return False

def find_prime5(primes):
    for i, p1 in enumerate(primes):
        for j, p2 in enumerate(primes[i:]):
            if cond(p1, p2):
                for k, p3 in enumerate(primes[j:]):
                    if cond(p1, p3) and cond(p2, p3):
                        for l, p4 in enumerate(primes[k:]):
                            if cond(p1, p4) and cond(p2, p4) and cond(p3, p4):
                                for m, p5 in enumerate(primes[l:]):
                                    if cond(p1, p5) and cond(p2, p5) and cond(p3, p5) and cond(p4, p5):
                                        print(p1, p2, p3, p4, p5, p1+p2+p3+p4+p5)
                                        return p1+p2+p3+p4+p5

print(find_prime5(primes))
