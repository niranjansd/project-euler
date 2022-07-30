# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?
import numpy as np
num_days = 0
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
all1_locations = [1] # Locations of all the 1sts of the months
for i in range(1901, 2001):
    for m, d in zip(months, days):
        num_days += d
        if m == 'feb':
            if not i % 400:
                num_days += 1
            elif not i%100:
                pass
            elif not i % 4:
                num_days += 1
        all1_locations.append(num_days+1)
# 364 days is 52 weeks
# The 365th day is Monday again, i.e 31 Dec 1900 is Monday.
# 1 Jan 1901 is Tuesday => 6th Jan 1901 is Sunday
sunday_locations = np.arange(6, num_days+1, 7) # locations of all the sundays
# Find intersection of 1st locations with sunday locations.
sunday1 = [i for i in all1_locations if i in sunday_locations]
print(sunday1)
print(len(sunday1))
