# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
# For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?


import itertools

def isprime(num):
    if not num % 2:
        return False
    if not num % 3:
        return False
    p = 5
    while (p <= num//3): 
        if not num % p:
            return False
        p += 2
    return True


largest = 0
for l in range(9, 0, -1):
    numlist = [str(i) for i in range(1, l+1)]
    nums = list(itertools.permutations(numlist))
    nums = sorted([int("".join(ns)) for ns in nums], reverse=True)
    for n in nums:
        if isprime(n):
            largest = n
        if largest:
            break
    if largest:
        break

print(largest)