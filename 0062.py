# The cube, 41063625 (345^3), can be permuted to produce
# two other cubes: 56623104 (384^3) and 66430125 (405^3).
# In fact, 41063625 is the smallest cube which has exactly
# three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations
#     of its digits are cube.

import numpy as np

fam = 5
i = 340
done = False
while True:
    scub = str(i**3)
    lenscub = len(scub)
    sorteds = {}
    while len(scub) == lenscub:
        i+=1
        cub = i**3
        scub = str(cub)
        scub = ''.join(sorted(scub))
        if scub in sorteds:
            if i not in sorteds[scub]:
                sorteds[scub].append(i)
        else:
            sorteds[scub] = [i]
        if len(sorteds[scub]) == fam:
            print(sorteds[scub], list(map(lambda x: x**3, sorteds[scub])))
            done = True
            break
    if done:
        break