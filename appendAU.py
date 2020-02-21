import csv, sys, fileop

fp = open(str(sys.argv[1]), 'r')
r = csv.reader(fp)
start = int(sys.argv[4])
i = 0 
while i < start:
	i+=1
	next(r)
dest_f = open(str(sys.argv[2]), 'w')
w = csv.writer(dest_f, dialect='excel', delimiter=' ', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
fileop.addLines(r, w)
fp.close()
dest_f.close()
