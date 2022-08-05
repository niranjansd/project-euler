# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# nperm(n) = n!
# nperm(9) = 40320 
# nperm(9) = 362880 
# nperm(10) = 3628800 
# So 9! factorial is under 1 million and 10th factorial is over 1 million.
# 1 millionth number will be 3rd set of 9! numbers. So in increasing order the first number wll be 2.
import math

from sympy import N

n = 1000000
print([math.perm(i) for i in range(1, 10)])
def find_len(n):
    if n > math.perm(10):
        raise ValueError("number too large")
    lessn = 0
    moren = 1
    for i in range(1, n):
        if math.perm(i) < n:
            lessn = i
            moren = i + 1
        else:
            return i
            
# print(find_len(n))

def findfirst(n):
    moren = find_len(n)
    # print(moren)
    if moren == 1:
        return n, 0
    lessnperm = math.perm(moren-1)
    for i in range(10):
        # print(n, lessnperm)
        if n > lessnperm:
            n -= lessnperm
        elif n == lessnperm:
            n -= lessnperm
            break
        else:
            break
    return i, n

def findfull(n):
    num = ""
    remains = list(range(10))
    while n:
        start = find_len(n)
        print(start)
        for i in range(len(remains)-start):
            # print(i, remains, start)
            num += str(remains.pop(0))
        print(n, num)
        i, n = findfirst(n)
        print(i, n)
        num += str(remains.pop(i))
        if n == 0:
            num += "".join(map(str, remains[::-1]))
            remains = []
    for i in remains:
        num += str(i)
    return num

print('first', findfirst(n=4))
print('first', findfull(n=4))
print(findfull(n=1000000))
