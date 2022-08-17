# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def check_palindrome(n):
    if len(n) == 1:
        return True
    if n[0] == n[-1]:
        if len(n) == 2:
            return True
        else:
            return check_palindrome(n[1:-1])

pals = []
for i in range(1, 1000000):
    if check_palindrome(str(i)) and check_palindrome(str(bin(i))[2:]):
        pals.append(i)

print(sum(pals))