__author__ = 'srs'

import os, sys

'''
Palindromic numbers - Output palindromic numbers.

Given: input: the minimum number of digits to consider

Output: A list of palindromic numbers. You can decide how (and if) to end the sequence.
'''

n = sys.argv[1]

def palindrome(n):
    count = 0
    for num in range(0, n):

        splitNum = list(str(num))
        splitNum = splitNum[::-1]
        #print "".join(splitNum)
        if "".join(splitNum) == str(num):
            print num

palindrome(int(n))