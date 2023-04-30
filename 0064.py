#All square roots are periodic when written as continued
# fractions and can be written in the form:
# For example, let us consider 
 
# If we continue we would get the following expansion:
# The process can be summarised as follows:
# It can be seen that the sequence is repeating.
# For conciseness, we use the notation 
# , to indicate that the block (1,3,1,8) repeats indefinitely.

# The first ten continued fraction representations of (irrational) square roots are:
# Exactly four continued fractions, for 
# , have an odd period.

# How many continued fractions for 
#  have an odd period?

import numpy as np
nmax = 10
odds = 0

def cf(n):
    mn = 0.0
    dn = 1.0
    a0 = int(np.sqrt(n))
    an = int(np.sqrt(n))
    period = 0
    if a0 != np.sqrt(n):
        while an != 2*a0:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            period += 1
    return period

odds = 0
nmax = 10001
for i in range(2, nmax):
    period = cf(i)
    if period % 2:
        odds += 1
print(odds)
