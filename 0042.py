# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import numpy as np
with open('p042_words.txt') as f:
    words = f.read()

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
words = words.replace('"',"").replace("'","").split(",")

triangles = 0
for i, word in enumerate(words):
    try:
        num = [ALPHABET.index(l.upper())+1 for l in word]
    except:
        print(i, word)
        continue
    nsum = sum(num)
    nsumroot = np.sqrt(nsum*2)
    n = int(nsumroot) + 0
    while n*(n-1) < nsum*2:
        n += 1
        if n*(n-1) == nsum*2:
            triangles += 1
            break
print(triangles)