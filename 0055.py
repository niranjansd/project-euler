
import numpy as np
import utils

def test_lychrel(inp, bag=[], debug=False):
    if len(bag) == 100:
        return True, bag
    bag += [inp]
    si = str(inp)
    sbi = si[::-1]
    bi = int(sbi)
    su = inp+bi
    if inp % 10:
        bag += [bi]
    if debug:
        print(inp, bi, bag)
    if utils.is_palindrome(su):
        if debug:
            print(su, list(set(bag)))
        return (False, list(set(bag)))
    else:
        if debug:
            print(su, list(set(bag)))
        return test_lychrel(su, bag, debug=debug)


maxn = 10000
testing = np.arange(10, maxn).astype(np.int64)
lychrel = []
while len(testing):
    i = testing[0]
    try:
        f, bag = test_lychrel(i, [])
    except:
        lychrel.append(i)
        if i % 10:
            lychrel.append(int(str(i)[::-1]))
            testing = testing[~np.isin(testing, np.array([i, int(str(i)[::-1])]))]
        if not i % 10:
            testing = testing[1:]
        continue
    if f:
        lychrel.append(i)
        if i % 10:
            lychrel.append(int(str(i)[::-1]))
            testing = testing[~np.isin(testing, np.array([i, int(str(i)[::-1])]))]
        if not i % 10:
            testing = testing[1:]
        continue
    if not f:
        testing = testing[~np.isin(testing, np.array(bag))]

print(len(set(lychrel)))#, lychrel)