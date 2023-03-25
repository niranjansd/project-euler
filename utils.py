import numpy as np

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
    

def isprime(num):
    if not num % 2:
        return False
    if not num % 3:
        return False
    if str(num)[-1] in ['0', '5']:
        return False
    p = 7
    while (p <= num//5): 
        if not num % p:
            return False
        p += 2
    return True


def is_palindrome(num):
    num = str(num)
    if len(num) == 1:
        return True
    if len(num) == 2:
        if num[0] == num[1]:
            return True
        else:
            return False
    if num[0] == num[-1]:
        return is_palindrome(num[1:-1])
    else:
        return False


def SieveOfEratosthenes(n = 1000000, primesinit=[]):
    ''' Returns  a list of primes < n
    primesinit is a list of primes upto max(primeinit) to start with.
    '''
    prime = [False, False]+[True for i in range(2, n + 1)]
    if not len(primesinit):
        primesinit = [2]
    for i in range(2, max(primesinit)+1):
        if i not in primesinit:
            prime[i] = False
        # Update all multiples of p
        for j in range(i * i, n + 1, i):
            prime[j] = False

    p = max(primesinit)
    while (p * p <= n):
        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return np.nonzero(prime)[0]
