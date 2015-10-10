__author__ = 'srs'

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