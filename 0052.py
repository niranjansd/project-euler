# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

multiples = [2, 3, 4, 5, 6]
start = 100000
end = 1000000
for i in range(start, end):
    si = str(i)
    it = True
    for k in multiples:
        if set(str(k*i)) != set(si):
            it = False
            break
    if it:
        break

print([i]+ [k*i for k in multiples])