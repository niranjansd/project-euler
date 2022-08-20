#If p is the perimeter of a right angle triangle with integral length sides, 
#{a,b,c}, there are exactly three solutions for p = 120.
#{20,48,52}, {24,45,51}, {30,40,50}
#For which value of p ≤ 1000, is the number of solutions maximised?
import numpy as np
largest = 0
largestp = 0
for p in range(1, 1001):
    sols = []
    nope = False
    for i in range(1, int(p/2)):
        for j in range(i, int(p/2)):
            k = np.sqrt(i**2+j**2)
            if i+j+k > p:
                nope = True
                break
            if i+j+k == p:
                sols.append(tuple(sorted([i,j,k])))
    numsols = len(set(sols))
    if numsols > largest:
        largest = numsols
        largestp = p
        print(largest, p)
