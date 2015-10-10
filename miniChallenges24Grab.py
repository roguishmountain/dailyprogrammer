__author__ = 'srs'

from os.path import join
import os, sys

'''
Grab - like grep but simpler.

Input - a single line of text and a file name. You can take input via command line arguments or stdin, whichever is easier for you. You can also just take a single word instead of a line.

Output - all lines of the checked file which contain this piece of text, along with line numbers. Make it work case-insensitive.
'''

search = sys.argv[1]

def searchLines(fname):
    lineCount = 0

    for line in open(fname, "r"):
        if search.lower() in line.lower():
            print fname, ":", lineCount, ":", line.lstrip().rstrip()
        lineCount += 1


if len(sys.argv) > 2:
    fileName = sys.argv[2]
    searchLines(fileName)


else:
    for root, dirs, files in os.walk('.'):
        for name in files:
            if not name.startswith("."):
                searchLines(join(root, name))