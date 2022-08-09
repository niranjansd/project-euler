# There are 4*4 =16 is the example but 1 is a dup so 15.
# In the quetions we will have 99*99 = 9801 numbers. gotta remove dups.

maxn = 100
nums = []
for i in range(2, maxn+1):
    for j in range(2, maxn+1):
        nums.append(i**j)
print(len(set(nums)))