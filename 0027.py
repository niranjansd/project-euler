

def divisors(n):
    divs = []
    if n < 0: n *= -1
    for i in range(2, n//2 + 1):
        if not n % i:
            divs.append(i)
    return divs

def fn(a,b,n):
    return n*(n +a)+b

# If n and b has common divisors, it is not prime.
# If n+a and b have common divisors, it is not prime.

def coprime(a, b):
    ad = divisors(a)
    bd = divisors(b)
    abd = [i for i in ad if i in bd]
    if len(abd):
        return False
    return True


# for a in range(-999, 1000):
#     for b in range(-999, 1000):
nprimes = [0, 0, 0]
AS = []
for a in range(-999, 1000):
    if not a%100: print(a)
    for b in range(-999, 1000):
        # if not b%200: print(b)
        for n in range(500):
            if n == 3 and a == -498 and b == -495:
                print([n-1, a, b, fn(a,b,n), a*b, divisors(fn(a,b,n))])
            if len(divisors(fn(a,b,n))):
                if n-1 > nprimes[0]:
                    nprimes = [n-1, a, b, a*b,  fn(a,b,n), divisors(fn(a,b,n))]
                    print(nprimes)
                break
            if n == 499:
                nprimes = [n, a, b, a*b, fn(a,b,n), divisors(fn(a,b,n))]

            # if n ==1 and a == 0 and b == 49:
            #     print("wut")
            # if coprime(n, b) and coprime(b, n+a) and b!= (n+a) and b!=n:
            #     continue
            # else:
            #     if n-1 > nprimes[0]:
            #         nprimes = [n-1, a, b]
            #         print(nprimes)
            #     break

# print(AS)
# print(coprime(39, 41), coprime(40, 41))
