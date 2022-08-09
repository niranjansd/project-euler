

def divisors(n):
    divs = []
    if n < 0: n *= -1
    for i in range(2, n//2 + 1):
        if not n % i:
            divs.append(i)
    return divs

def fn(a,b,n):
    return n*(n +a)+b

nprimes = [0, 0, 0]
AS = []
for a in range(-999, 1000):
    if not a%100: print(a)
    for b in range(-999, 1000):
        for n in range(500):
            if len(divisors(fn(a,b,n))):
                if n-1 > nprimes[0]:
                    nprimes = [n-1, a, b, a*b,  fn(a,b,n), divisors(fn(a,b,n))]
                    print(nprimes)
                break

