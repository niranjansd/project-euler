

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