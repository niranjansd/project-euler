# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    num = str(num)
    if len(num) == 1:
        return True
    if len(num) == 2:
        if num[0] == num[1]:
            return True
        else:
            return False
    if num[0] == num[-1]:
        return is_palindrome(num[1:-1])
    else:
        return False

def largest_pal(n=3):
    n1 = int("".join(['9']*n))
    n2 = int("".join(['9']*n))
    pal = (999, 999, 0)
    for i in range(n1):
        if (n1-i)*(n2) < pal[2]:
            continue
        for j in range(i):
            if (n1-i)*(n2-j) < pal[2]:
                continue
            if is_palindrome((n1-i)*(n2-j)):
                if (n1-i)*(n2-j) > pal[2]:
                    pal = n1-i, n2-j, (n1-i)*(n2-j)
    return pal

print(largest_pal(3))
