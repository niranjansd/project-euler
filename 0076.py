# It is possible to write five as a sum in exactly six different ways:
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
# How many different ways can one hundred be written as a
# sum of at least two positive integers?

# Partition function
# p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - p(n-22) - ...

p0 = 1
p1 = 1
p2 = 2
p3 = 3
p4 = 5
p5 = 7
p6 = 11
p7 = 15
p8 = 22
p9 = 30
p10 = 42
p11 = 56
p12 = 77
p13 = 101
p14 = 135
p15 = 176
p16 = 231
p17 = 297
p18 = 385
p19 = 490
p20 = 627
p21 = 792
p22 = 1002
p23 = 1255
p24 = 1575
p25 = 1958
p26 = 2436
p27 = 3010
p28 = 3718
p100 = 190569292

