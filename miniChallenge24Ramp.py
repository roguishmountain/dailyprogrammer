__author__ = 'srs'

'''
Ramp Numbers - A ramp number is a number whose digits from left to right either only rise or stay the same. 1234 is a ramp number as is 1124. 1032 is not.

Given: A positive integer, n.

Output: The number of ramp numbers less than n.
'''

import sys

n = sys.argv[1]

def ramp(n):
    count = 0
    for num in range(0, n):

        splitNum = list(str(num))

        if "".join(sorted(splitNum)) == str(num):
            count += 1

    print "there were", count, "ramp numbers"

ramp(int(n))