# It is possible to show that the square root of two can be 
# expressed as an infinite continued fraction.
# By expanding this for the first four iterations, we get:
# The next three expansions are  
# but the eighth expansion, is the first example where
# the number of digits in the numerator exceeds
# the number of digits in the denominator.
# In the first one-thousand expansions,
# how many fractions contain a numerator with more digits
#     than the denominator?

def rep(n):
    if n in reps:
        return reps[n]
    if n > 1:
        return (rep(n-1)[1], 2*rep(n-1)[1]+rep(n-1)[0])
    else:
        return (1, 2)

num = 0
reps = {}
for i in range(1, 1001):
    r = rep(i)
    reps[i] = r
    if len(str(r[0]+r[1])) > len(str(r[1])):
        num += 1
print(num)
