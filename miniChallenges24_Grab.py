__author__ = 'srs'

from os.path import join
import os, sys


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