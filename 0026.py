# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

cyclenums = []
for d in range(1, 1000):
    orem = [1]
    rem = 1
    cycle = 0
    frac = True
    while rem:
        if rem in orem or rem/10 in orem or rem/100 in orem or rem/1000 in orem:
            if cycle:
                break
        else:
            orem.append(rem)
        if rem*10 > d:
            rem = (rem*10) % d
            if rem:
                cycle += 1
            else:
                cycle = 0
                frac = False 
                break
        elif rem*100 > d:
            rem = (rem*100) % d
            if rem:
               cycle += 2
            else:
                cycle = 0
                frac = False 
                break
        elif rem*1000 > d:
            rem = (rem*1000) % d
            if rem:
               cycle += 2
            else:
                cycle = 0
                frac = False 
                break
    cyclenums.append([cycle, d])
print(sorted(cyclenums)[-1])
