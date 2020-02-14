import csv
import re
import sys

regex = '^RT @.*'
source_f = open(str(sys.argv[1]), mode='r')
r = csv.reader(source_f)
next(r)  # skip CSV headerline
dest_f = open(str(sys.argv[2]), mode='w')
w = csv.writer(dest_f, dialect='excel', delimiter=' ', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
for row in r:
    twt = [row[int(sys.argv[3])]]  # int is col to append
    if not re.match(regex, twt[0]):  # skip retweet
        w.writerow(twt)
