# The 5-digit number, 16807=7^5, is also a fifth power.
# Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

# print(7**5, 8**9)
basemin = 1
basemax = 100
expmin = 1
expmax = 100

num = 0
nums = []
for base in range(basemin, basemax):
    for exp in range(expmin, expmax):
        if len(str(base**exp)) == exp:
            num += 1
            nums.append(base**exp)
print(num)
print(len(set(nums)))
