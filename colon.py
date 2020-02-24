import sys, csv, fileop

source_f = open(str(sys.argv[1]), 'r')
r = csv.reader(source_f)
next(r)  # skip CSV headerline
dest_f = open(str(sys.argv[2]), 'a')
w = csv.writer(dest_f, dialect='excel', delimiter=' ', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
for row in r:
	w.writerow([row[int(sys.argv[3])]])
source_f.close()
dest_f.close()
