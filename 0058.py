# Starting with 1 and spiralling anticlockwise in the following way,
# a square spiral with side length 7 is formed.
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
# It is interesting to note that the odd squares lie along
# the bottom right diagonal,
# but what is more interesting is that 8 out of the 13 numbers
# lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above,
# a square spiral with side length 9 will be formed.
# If this process is continued, what is the side length of the square
# spiral for which the ratio of primes along both diagonals
#     first falls below 10%?

import numpy as np
import utils
sidelengthsmin = 1
sidelengthsmax = 20000
primes = []
maxlast = 1
numdiagprimes = 0
numdiags = 1
sidelength = 2*sidelengthsmax+1
numnums = sum([4*i-4 for i in range(3, sidelength+1, 2)])+1
primes = utils.SieveOfEratosthenes(8000, primes)
for sidelength in range(sidelengthsmin, sidelengthsmax):
    sidelength = 2*sidelength+1
    numnewnums = np.arange(4*sidelength-4)+maxlast+1
    maxlast = numnewnums[-1]
    diags = [numnewnums[sidelength-2], numnewnums[2*sidelength-3],
             numnewnums[3*sidelength-4], numnewnums[-1]]
    numdiags += len(diags)
    if max(diags) > max(primes):
        numdiagprimes += len([d for d in diags if utils.isprime(d)])
    else:
        numdiagprimes += len([d for d in diags if d in primes])    
    if (numdiagprimes/numdiags) < 0.1:
        print(3, sidelength)
        break
