# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
# are all figurate (polygonal) numbers and are generated by the following
# formulae:

# Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
# Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
# Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
# Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has
# three interesting properties.

# The set is cyclic, in that the last two digits of each number is
# the first two digits of the next number (including the last number
#                                          with the first).
# Each polygonal type: triangle (P3,127=8128), square (P4,91=8281),
# and pentagonal (P5,44=2882), is represented by a different number in
# the set.
# This is the only set of 4-digit numbers with this property.
# Find the sum of the only ordered set of six cyclic 4-digit
# numbers for which each polygonal type: 
# triangle, square, pentagonal, hexagonal, heptagonal, and octagonal,
# is represented by a different number in the set.

import utils

def is_cyclic(a, b):
    return str(a)[-2:] == str(b)[:2]

# print(is_cyclic(8128, 2882))
# print(is_cyclic(2882, 8281))
# print(is_cyclic(8281, 8128))

triangles = [n*(n+1)//2 for n in range(25, 340)]
triangles = [n for n in triangles if len(str(n))==4]
squares = [n**2 for n in range(30, 340) ]
squares = [n for n in squares if len(str(n))==4]
pentagonals = [n*(3*n-1)//2 for n in range(18, 305)]
pentagonals = [n for n in pentagonals if len(str(n))==4]
hexagonals = [n*(2*n-1) for n in range(18, 305)]
hexagonals = [n for n in hexagonals if len(str(n))==4]
heptagonals = [n*(5*n-3)//2 for n in range(18, 305)]
heptagonals = [n for n in heptagonals if len(str(n))==4]
octagonals = [n*(3*n-2) for n in range(18, 305)]
octagonals = [n for n in octagonals if len(str(n))==4]

sets = [triangles, squares, pentagonals, hexagonals, heptagonals, octagonals]

for i in triangles:
    for ii in range(1, 6):
        for j in sets[ii]:
            if is_cyclic(i, j):
                for jj in range(1, 6):
                    if jj != ii:
                        for k in sets[jj]:
                            if is_cyclic(j, k):
                                for kk in range(1, 6):
                                    if kk != ii and kk != jj:
                                        for l in sets[kk]:
                                            if is_cyclic(k, l):
                                                for ll in range(1, 6):
                                                    if ll != ii and ll != jj and ll != kk:
                                                        for m in sets[ll]:
                                                            if is_cyclic(l, m):
                                                                for mm in range(1, 6):
                                                                    if mm != ii and mm != jj and mm != kk and mm != ll:
                                                                        for n in sets[mm]:
                                                                            if is_cyclic(m, n) and is_cyclic(n, i):
                                                                                print(i, j, k, l, m, n)
                                                                                print(i+j+k+l+m+n)


