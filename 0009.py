# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# So a+b+c = 1000
# a*a+b*b = c*c

# By triangle inequality a + b > c => 1000 > 2c => c < 500 => a,b <= 500
# Also 3c > 1000, c>333
# Also 3a < 1000, a>333
import numpy as np
def find_triplet():
    minc = 333
    maxc = 500
    maxa = 333
    for c in range(minc, maxc):
        for a in range(1, maxa):
            b = np.sqrt(c*c - a*a)
            if not b % 1:
                if a+b+c == 1000:
                    print(a,b,c,a+b+c, a*b*c)

find_triplet()
