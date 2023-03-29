# It is possible to write five as a sum in exactly six different ways:
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
# How many different ways can one hundred be written as a
# sum of at least two positive integers?



def break_two(n):
    '''List all possible ways to split n into 2.
    '''
    n = int(n)
    if n < 2:
        raise ValueError('n must be >= 2, was {}.'.format(n))
    n2 = int(n / 2)
    return [','.join([str(i),str(n-i)]) for i in range(1, n2+1)]


def break_three(n):
    '''List all possible ways to split n into 3.'''
    n2 = break_two(n)
    n3 = []
    for i in n2:
        isp = i.split(',')
        try:
            i20 = break_two(isp[0])
        except ValueError:
            continue
        for j in i20:
            n3.append(','.join([j]+isp[1:]))
        try:
            i21 = break_two(i[1])
        except ValueError:
            continue
        for j in i21:
            n3.append(','.join([j]+isp[0:1]))
            # n3.append(','.join(list(map(str, sorted(j+[i[0]])))))
        # print(n3)
    n3 = set(n3)
    return n3


def break_m(n, m, cache={}):
    '''List all possible ways to split n into m.'''
    if m in cache:
        if n in cache[m]:
            return cache[m][n]
    if m < 2:
        raise ValueError('m must be >= 2, was {}.'.format(m))
    if m == 2:
        # print(cache)
        if n in cache:
            if 2 in cache[n]:
                return cache
        cache[int(n)][m] = break_two(n)
        return cache
    n2 = break_two(n)
    cache[int(n)][2] = n2
    n3 = []
    # print(m, 'n2', n2)
    for i in n2:
        isp = i.split(',')
        # print(m, 'n2', n2, 'iii', i)
        n33 = []
        for k in range(len(isp)):
            ik = [isp[l] for l in range(len(isp)) if k != l]
            # print(m, 'n2', n2, 'iiik', ik)
            i20 = []
            try:
                if isp[k] not in cache:
                    cache.update(break_m(isp[k], m - 1, cache=cache))
                elif m - 1 not in cache[isp[k]]:
                    cache.update(break_m(isp[k], m - 1, cache=cache))
                i20 = cache[int(isp[k])][m - 1]

                if not len(i20):
                    raise ValueError
            except ValueError:
                continue
            # print(m, 'n2', n2, 'i', i, 'i20', i20)
            for j in i20:
                n33.append(','.join([str(j)]+ik))
                # n33.append(','.join(list(map(str, sorted(j + ik)))))
            # print(n33)
            n33 = list(set(n33))
            # print(m, 'n2', n2, 'i', i, 'i20', i20, 'k', n33)
        if not len(n33):
            continue
        # print(n33)
        # n33 = [list(map(int, p.split(','))) for p in n33]
        n3 += n33
        # print(m, 'n2', n2, 'i', i, 'n33', n33)
        # break
        # n33.append(','.join(list(map(str, sorted(j + ik)))))
    n3 = set(n3)
    # n3 = [list(map(int, i.split(','))) for i in n3]
    cache[int(n)][m] = list(set([','.join(sorted(i.split(','))) for i in n3]))

    return cache


cache = {5: {}, 100: {}}
cache = {i: {} for i in range(2, 101)}

print(break_two(5))
print(len(break_two(5)))
# print(break_three(5))
# print(len(break_three(5)))
print(break_m(5, 3, cache=cache))
print(len(break_m(5, 3, cache=cache)))
print(break_m(5, 4, cache=cache))
print(len(break_m(5, 4, cache=cache)))
print(break_m(5, 5, cache=cache))

s = []
for i in range(2, 101):
    print(i)
    cache.update(break_m(100, i, cache=cache))
    s += cache[100][i]

# print([sorted(i.split(',')) for i in s if sum(list(map(int, i.split(',')))) == 100])
print(len(set([','.join(sorted(i.split(','))) for i in s if sum(list(map(int, i.split(',')))) == 100])))
# print(len(s))
