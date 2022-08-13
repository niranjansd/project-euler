fracs = []
frac = 1
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            num = int(str(i)+str(j))
            den = int(str(j)+str(k))
            frac1 = num/den
            frac2 = i/k
            if frac1 ==  frac2 and frac2 < 1:
                fracs.append([i, k])
                frac *= i/k

print(fracs)
print(frac)
