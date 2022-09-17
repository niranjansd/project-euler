
import math

nums = 0
for n in range(101):
    inums = []
    mid = int(n//2)
    cmax = math.comb(n, mid)
    if cmax < 1e6:
        continue
    for i in range(mid):
        if math.comb(n, mid-i) > 1e6:
            inums.append([n, mid-i])
        else:
            continue
    if n % 2:
        nums += 2*len(inums)
    else:
        nums += 2*len(inums)-1
print(nums)
