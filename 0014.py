# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

# I dont think there is any way to solve this analyically.
# Except if there is a loop somewhere. But there shoudl not be, becaus ethat would disprove collatxz theorem.

def ncollatz(n):
    numlen = 0
    if n <= 1:
        return 1
    numlen += 1
    if n % 2:
        n = 3*n + 1
        numlen += ncollatz(n)
    else:
        n /= 2
        numlen += ncollatz(n)
    return numlen

maxn = 1
numn = 1
for i in range(1, 1000000):
    n = ncollatz(i)
    if n > maxn:
        maxn = n+0
        numn = i
print(maxn, numn)
