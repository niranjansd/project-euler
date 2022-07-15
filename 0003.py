# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def primefactors(num):
    factors = {}
    while not num % 2:
        factors[2] = 1
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
            factors[p] = 1
            num = num // p        
        p += 2
        isprime = True
    return factors

print(primefactors(13195))
print(primefactors(600851475143))

