# Consider quadratic Diophantine equations of the form:

# x2 – Dy2 = 1

# For example, when D=13, the minimal solution
# in x is 6492 – 13×1802 = 1.

# It can be assumed that there are no solutions in
# positive integers when D is square.

# By finding minimal solutions in x for D = {2, 3, 5, 6, 7},
#     we obtain the following:

# 32 – 2×22 = 1
# 22 – 3×12 = 1
# 92 – 5×42 = 1
# 52 – 6×22 = 1
# 82 – 7×32 = 1

# Hence, by considering minimal solutions in x for D ≤ 7,
#     the largest x is obtained when D=5.

# Find the value of D ≤ 1000 in minimal solutions of x for
# which the largest value of x is obtained.

D = 1
x = 1
Dall = [i for i in range(1001) if D**0.5 != int(D**0.5)]
xs = []
Ds = {}
# while D<1000:
#     D += 1
#     x = 1
#     if D**0.5 == int(D**0.5):
#         # print('D is square')
#         continue
#     while True:
#         x += 1
#         if (x**2 - 1) % D == 0:
#             y = ((x**2 - 1) / D)**0.5
#             if y == int(y):
#                 print(x, D, y)
#                 Ds[x] = D
#                 break
#         # if D%100 == 0:
#         #     print(D)

while True:
    x += 1
    for D in Dall:
        if (x**2 - 1) % D == 0:
            y = ((x**2 - 1) / D)**0.5
            if y == int(y):
                print(x, D, y)
                Ds[x] = D
                break
    Dall.pop(Dall.index(D))


print(max(Ds.keys()), Ds[max(Ds.keys())])
