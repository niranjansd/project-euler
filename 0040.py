# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

d1 = 1
def dn(n):
    start = 0
    lennum = 1
    while n >= 0:
        end = int("".join(['9']*lennum))
        numnum = ((end-start)+1)*lennum
        if n <= numnum:
            nth = n // lennum + start
            return int(str(nth)[n % lennum])
        start = end+1
        n -= numnum
        lennum += 1

print(dn(1)*dn(10)*dn(100)*dn(1000)*dn(10000)*dn(100000)*dn(1000000))