# We shall say that an n-digit number is pandigital if it makes use
# of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254,
# containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product
# identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.

# There are 9 numbers and 2 symbols (x,=). So 11! permutations.
# We can eliminate most of them by an orders of magnitude comparision.
# len(RHS)-1 < len(LHS) <= len(RHS)+1
# len(LHS)+len(RHS) = 9
# => LHS:RHS = (5,4)

import math
import itertools
pds = []
for p in itertools.permutations('123456789'):
    m1, p1 = p[:5], p[5:]
    for i in range(4):
        m11, m12 = m1[:(i+1)], m1[(i+1):]
        if int(''.join(m11))*int(''.join(m12)) == int(''.join(p1)):
            pds.append(int(''.join(p1)))
print(set(pds))
print(sum(set(pds)))