import csv
import fileop
import sys

source_f = open(str(sys.argv[1]), 'r')
r = csv.reader(source_f)
next(r)  # skip CSV headerline
print(fileop.contLines(r))
