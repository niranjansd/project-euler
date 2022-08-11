

nums = []
for i in range(2, 100000000):
    si = str(i)
    sump = sum([int(k)**5 for k in si])
    if sump == i:
        nums.append(i)

print(nums)
print(sum(nums))
