
# (1+x)^200 x (1+x^2)^100 x (1+x^5)^40 x (1+x^10)^20 x (1+x^50)^4 x (1+x^100)^2 x (1+x^200)
# Coefficient of x^200.

# (200Ci x^i) x (100Cjx^2j) x 40Ckx^5k x 20Clx^10l x 4Cmx^50x x 2Cnx^100x *(1+x^200)

# Simplify last 3
# (1 + 1 + 1 + 2.6) x^200
# + (1 + 2 p^100 + 4 p^50 + 8 p ^150 + 4 p^150) x
# (1+x)^200 x (1+x^2)^100 x (1+x^5)^40 x (1+x^10)^20

# Join 1 &2 and 3 &4
# (1+ 2x^2 + 2x + 2x^3 + x^4)^100 x (1+2x^10+2x^5+x^20)^20
# This will take too long.

coins = [1,2,5,10,20,50,100,200]
maxn = [200, 100, 40, 20, 10, 4, 2, 1]
coins = coins[::-1]
maxn = coins[::-1]
combs = [[]]
for i, m in zip(coins, maxn):
    newcombs = []
    while combs:
        arr = combs.pop()
        sum = 0
        for ind, n in enumerate(arr):
            sum += n*coins[ind]
        for k in range(m+1):
            if i == 1 and sum+k*i != 200:
                continue
            if sum+k*i <= 200:
                if arr+[k] in newcombs:
                    continue
                newcombs.append(arr+[k])
            else:
                if arr+[0] in newcombs:
                    continue
                newcombs.append(arr+[0])
    combs = newcombs[:]


print(len(combs))




