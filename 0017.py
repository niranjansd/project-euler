# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
# 23 letters and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance with British usage.
ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
exceptions = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
hundreds = ['hundred', 'thousand']
numstr = []
sumnumstr = 0
for i in range(1, 1001):
    num = str(i)
    num = num.zfill(4)
    numstr = ""
    if int(num[-2]) == 1:
        if int(num[-1]):
            numstr += exceptions[int(num[-1])-1]
        else:
            numstr += 'ten'
    else:
        if int(num[-1]):
            numstr += ones[int(num[-1])-1]
        if int(num[-2]):
            numstr += tens[int(num[-2])-1]
    if int(num[-3]):
        numstr += ones[int(num[-3])-1] + 'hundred'
        if int(num[-2:]):
            numstr += 'and'
    if int(num[-4]):
        numstr += ones[int(num[-4])-1] + 'thousand'
    sumnumstr += len(numstr)

print(sumnumstr)
