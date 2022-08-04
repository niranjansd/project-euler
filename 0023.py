# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and
# it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 28123 can be written 
# as the sum of two abundant numbers. 
# However, this upper limit cannot be reduced any further by analysis even though it is known that 
# the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import numpy as np
def divisors(n):
    divs = [1]
    for i in range(2, n//2 + 1):
        if not n % i:
            divs.append(i)
    return divs

const = 28123

abundants = [False]*const 
for i in range(1, const):
    if not abundants[i]:
        if sum(divisors(i)) > i:
            abundants[i] = True
    if abundants[i]:
        for k in range(1, const//i):
            abundants[int(i*k)] = True

abunds = np.nonzero(abundants)[0]
nonabundsumsind = [True]*const
for i in range(len(abunds)):
    for j in range(len(abunds)):
        if (abunds[i]+abunds[j]) < const:
            nonabundsumsind[abunds[i]+abunds[j]] = False
nonabundsums = np.nonzero(nonabundsumsind)[0]
nonabundsumsum = sum(nonabundsums)
print(nonabundsumsum)