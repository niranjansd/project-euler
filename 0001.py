# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


import math
# O(N)
limit = 1000
sum = 0
for i in range(1, limit):
    if not (i%3)*(i%5):
        sum += i

print(sum)

# O(1)
limit = 1000
quotient3 = limit // 3
quotient5 = limit // 5 - 1 # subtract 1 To skip 1000
quotient15 = limit // 15
sum_of_5_multiples = 5 * quotient5 * (quotient5 + 1) / 2
sum_of_3_multiples = 3 * quotient3 * (quotient3 + 1) / 2
sum_of_15_multiples = 15 * quotient15 * (quotient15 + 1) / 2
sum = sum_of_5_multiples + sum_of_3_multiples - sum_of_15_multiples

print(sum)
