# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?

# Number divisible by 8 is also by 2 and 4
# Same with 9 and 3, and 8 and 4. and 6 comes for free with 9,8, 10 with 8,5.
print(5*9*8*7)
# Can we do the same with 20.
# Get all the primes first, 2,3,5,7,11,13,17,19.
# Use 16 instead of 2,4,6,8,16. 6,10,12,14,15,18,20 comes for free. Use 9 instead of 3.
# So 5,7,9,11,13,16,17,19.
print(5*7*9*11*13*16*17*19)
# Seems like the general formal for the smallest number is -
import numpy as np
def smallest_lcm(n):
    factors = np.ones(shape=(n+1,))
    for i in range(2, n+1): 
            if n < i*2:
                continue
            for k in range(2, 1+(n//i)): # Remove all multiples of i.
                factors[i*k] *= 0
    # Now we have all the prime factors.    
    # Now add the highest instead of the lowest power of the primes. 
    for i in range(2, n+1):
        if i*i > n:
            break
        if factors[i]:
            ifactor = i
            while ifactor*i < n: # Keep the highest exponentiation of i
                factors[ifactor] = 0
                factors[ifactor*i] = 1
                ifactor *= i
    return np.nonzero(factors)[0][2:]

print(smallest_lcm(20))