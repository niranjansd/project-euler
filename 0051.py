# By replacing the 1st digit of the 2-digit number *3,
# it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit,
# this 5-digit number is the first example having seven primes among the ten generated numbers,
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number
# (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

import time
import numpy as np
import pandas as pd
import collections
def SieveOfEratosthenes(n = 1000000):
    prime = [True for i in range(n + 1)]
     
    p = 2
    while (p * p <= n):
        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return np.nonzero(prime)[0][2:]

primes = SieveOfEratosthenes(10000000)

sprimes = np.array(list(map(str, primes)))
lenprimes = np.array(list(map(len, sprimes)))

def strmatch(s1, s2):
    return "".join(['0' if s1[i] != s2[i] else '1' for i in range(len(s1))]) 

fam = 7
maxn = 5
# print(max(lenprimes))
start = time.time()
for k in range(5, max(lenprimes)):
    ttnums = []
    print(k)
    tprimes = primes[lenprimes==k]
    tsprimes = sprimes[lenprimes==k]
    jmat = {}
    dmat = {}
    done = False
    for i in range(len(tsprimes)-fam):
        print(k, i, time.time()-start)
        start = time.time()
        dmat[tsprimes[i]] = {}
        tsmat = np.array([[*m] for m in tsprimes[(i+1):]])
        ddmat = ((tsmat == np.array([[*tsprimes[i]]]))*1)  # [num primes x len primes] 1 for match 0 for not
        print(k, i, time.time()-start)
        start = time.time()
        # print(i, ddmat)
        # print(i, tsmat, np.array([[*tsprimes[i]]]))
        # print(tsprimes[i], tsprimes[(i+1):])
        tsddmat = np.sort(tsmat.astype(int)*(1-ddmat).astype(int)- ddmat, axis=1)  # keep non-matching nums and sort
        # tsddmatnz = np.count_nonzero(axis=1)
        # print(tsddmat.shape)
        tsddmatnz = np.amax((tsddmat<0)*1, axis=1) # If there are any nums that match, 1, else 0, should be 1
        tsddmat = np.diff(tsddmat, axis=1)>0  # distinct nums edges
        jmat = tsddmat.sum(axis=1) * tsddmatnz # num distinct nums, should be 1
        print(k, i, time.time()-start)
        start = time.time()
        # print(jmat)
        tsddmat = np.sort(np.array([[*tsprimes[i]]]).astype(int)*(1-ddmat).astype(int)- ddmat, axis=1) 
        # tsddmatnz = np.count_nonzero(axis=1)
        tsddmatnz = np.amax((tsddmat<0)*1, axis=1)
        tsddmat = np.diff(tsddmat, axis=1)>0
        jmat *= tsddmat.sum(axis=1) * tsddmatnz
        # df = pd.DataFrame((tsmat.astype(int)*ddmat.astype(int)).T)
        # jmat = df.nunique().values
        # print(jmat)
        # break
        # df = pd.DataFrame((np.array([[*tsprimes[i]]]).astype(int)*ddmat.astype(int)).T)
        # jmat *= df.nunique().values
        # print(tsprimes[i], tsprimes[(i+1):])
        # print(jmat)
        ddsmat = ((np.expand_dims(jmat, axis=1)==1)*ddmat).astype(str)
        # print(tsprimes[i], tsprimes[(i+1):])
        # print(jmat)
        # print(jmat)
        # print(ddmat)
        print(k, i, time.time()-start)
        start = time.time()
        nz = np.nonzero(ddmat.sum(axis=1))[0]
        if len(nz)+1 < fam:
            continue
        # print(tsprimes[i], nz)
        print(k, i, len(nz), time.time()-start)
        start = time.time()
        for ii in nz:
            # print(tsprimes[(i+1):][ii], jmat[ii], ddmat[ii, :])
            if jmat[ii] == 1 and ddmat[ii, :].sum():
                match = "".join(ddsmat[ii, :])
                if match in dmat[tsprimes[i]]:
                    dmat[tsprimes[i]][match].append(tsprimes[(i+1):][ii])
                else:
                    dmat[tsprimes[i]] = {match: [tsprimes[(i+1):][ii]]}
        print(k, i, time.time()-start)
        start = time.time()
        # print(tsprimes[i], dmat[tsprimes[i]])
        # matcharr = ["".join(ddmat[ii, :]) for ii in range(ddmat.shape[0]) if jmat[ii] == 1]
        # print(matcharr)
        # matchcnt = collections.Counter(matcharr)
        # matchmax = max(matchcnt.values())
        # if matchmax+1 < fam:
        #     continue
        # print(tsprimes[i], matchmax)
        # for j in range(i+1, len(tsprimes)):
        #     x = len(set([tsprimes[i][ii]+tsprimes[j][ii] for ii in range(len(tsprimes[i])) if tsprimes[i][ii] != tsprimes[j][ii]]))
        #     if x != 1:
        #         continue
        #     match = "".join(['0' if tsprimes[i][ii] == tsprimes[j][ii] else '1' for ii in range(len(tsprimes[i]))])
        #     if match in dmat[tsprimes[i]]:
        #         dmat[tsprimes[i]][match].append(tsprimes[j])
        #         # dmat[tsprimes[i]][tsprimes[j]] = [0 if tsprimes[i][ii] == tsprimes[j][ii] else 1 for ii in tsprimes[i]]
        #         # dmat[tsprimes[i]][tsprimes[j]] = [0 if tsprimes[i][ii] == tsprimes[j][ii] else 1 for ii in tsprimes[i]]
        #     else:
        #         dmat[tsprimes[i]] = {match: [tsprimes[j]]}
        #         # dmat[tsprimes[i]] = {tsprimes[j]: [0 if tsprimes[i][ii] == tsprimes[j][ii] else 1 for ii in tsprimes[i]]}
        if not dmat[tsprimes[i]]:
            continue
        matchmax = max(len(v) for _, v in dmat[tsprimes[i]].items())
        print(k, i, matchmax, time.time()-start)
        start = time.time()
        if matchmax+1 < fam:
            del dmat[tsprimes[i]]
            continue
        # print(tsprimes[i])
        # print(dmat[tsprimes[i]])
        for match in dmat[tsprimes[i]]:
            if len(dmat[tsprimes[i]][match]) == matchmax:
                ttnumone = sorted([tsprimes[i]]+dmat[tsprimes[i]][match])
                if ttnumone not in ttnums:
                    ttnums.append(ttnumone)
                    done = True
                    break
        if done:
            break
        print(k, i, time.time()-start)
        start = time.time()
        break
    print(ttnums)
    print(k, time.time()-start)
    start = time.time()

    # print(dmat.sum(axis=(1,2)))
    # print(np.nonzero(dmat.sum(axis=2))[0].shape)
    if k == maxn:
        break
    # jmat = np.array([[len(set([i[ii]+j[ii] for ii in range(len(i))
    #                  if i[ii]!= j[ii]])) for i in tsprimes] for j in tsprimes])
    # jmat = np.array([[len(set([i[ii]+j[ii] for ii in range(len(i))
    #                  if i[ii]!= j[ii]])) for i in tsprimes] for j in tsprimes])
    # jmat = (jmat == 1)*1
    # jmat1 = np.array([[len(set(i)-set(j)) for i in tsprimes] for j in tsprimes])
    # jmat2 = np.array([[len(set(j)-set(i)) for i in tsprimes] for j in tsprimes])
    # jmat = 1-np.logical_or(jmat1>1, jmat2>1)*1
    # print(jmat1)
    # print(jmat2)
    # print(jmat)
    # print(len(tsprimes))
    # dmat = np.array([[*i] for i in tsprimes])
    # dmat = (np.expand_dims(dmat, axis=1) == np.expand_dims(dmat, axis=0))
    # dmat = dmat*np.expand_dims(jmat, axis=2)
    # nz = np.nonzero(dmat.sum(axis=2))
    # print(len(nz[0]))
    # pnums = []
    # ttnums = []
    # for i in np.unique(nz[0]):
    #     # nnz = (nz[0][nz[0]==i], nz[1][nz[0]==i])
    #     tnum = [tsprimes[i]]
    #     tnums = list(tsprimes[nz[1][nz[0]==i]])
    #     if len(tnums)+1 < fam:
    #         if k >5:
    #             print(k,k)
    #         continue
    #     # print(tnum[0], len(tnums))
    #     matches = {}
    #     for j in nz[1][nz[0]==i]:
    #         match = "".join(dmat[i, j, :].astype(str))
    #         if match in matches:
    #             matches[match] += 1
    #         else:
    #             matches[match] = 1
    #     matchmax = max(matches.values())
    #     matchlist = [k for k in matches if matches[k] == matchmax]
    #     if matchmax+1 < fam:
    #         if k >5:
    #             print(k,k)
    #         continue
    #     # print(tnum[0], matchmax, matchlist)
    #     for match in matchlist:
    #         nnz = ([i]*matchmax,
    #             [j for j in nz[1][nz[0]==i]
    #                 if "".join(dmat[i, j, :].astype(str)) == match])
    #         ttnumone = sorted([tsprimes[i]] + list(tsprimes[nnz[1]]))
    #         if ttnumone not in ttnums:
    #             ttnums.append(ttnumone)
        # print(nnz)
        # break
    # break
    # print(tnums)
    # print(ttnums)

    # # print(dmat.sum(axis=(1,2)))
    # # print(np.nonzero(dmat.sum(axis=2))[0].shape)
    # if k == 4:
    #     break

    # ddmat = np.matmul(dmat, np.transpose(dmat, axes=(0,2,1)))#.sum(axis=-1)
    # # ddmat = ddmat * np.expand_dims(jmat, axis=2)
    # ddmat = (ddmat == dmat.sum(axis=2, keepdims=True)).sum(axis=-1)
    # ddmat *= (dmat.sum(axis=2)!=0)
    # # ddmat = np.matmul(np.transpose(dmat, axes=(0,2,1)), dmat)#.sum(axis=-1)
    # # eqmat = dmat.sum(axis=1)
    # eqmat = ddmat + 0
    # slprimes = tprimes[eqmat.max(axis=1) >= fam]
    # slsprimes = tsprimes[eqmat.max(axis=1) >= fam]
 

    # if k == 5:
    #     # print(ddmat)
    #     # print(ddmat[1,:])
    #     # print(tprimes[np.nonzero(ddmat[1,:])[0]])
    #     # print(eqmat.max(axis=1))
    #     # print(tsprimes)
    #     print(slsprimes)
    #     break

print(max(lenprimes))
