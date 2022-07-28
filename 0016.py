# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?
import math

def digit_sum(n):
    return sum([int(i) for i in str(int(2**n))])

i = 1000
print(i, digit_sum(i))
