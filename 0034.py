# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the
# sum of the factorial of their digits.
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.
import math
nums = []
for i in range(10, 10000000):
    s = str(i)
    if sum([math.factorial(int(j)) for j in s]) == i:
        nums.append(i)

print(nums)
print(sum(nums))