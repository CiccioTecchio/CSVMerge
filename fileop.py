import re
import sys


def addLines(r, w):
    regex = '^RT @.*'
    add_cont = 0
    for row in r:
        twt = [row[int(sys.argv[3])]]  # int is col to append
        if not re.match(regex, twt[0]):  # skip retweet
            w.writerow(twt)
            add_cont += 1
    return add_cont


def contLines(r):
    tot_line = -1
    for row in r:
        tot_line += 1
    return tot_line
