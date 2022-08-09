
def sumofdiag(n):
    sumd = 1
    num = 1
    for i in range(n):
        inc = 2*(i+1)
        for _ in range(4):
            num += inc
            sumd += num
    return sumd

print(sumofdiag(500))