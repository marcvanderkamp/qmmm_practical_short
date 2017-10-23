#!/c/CCP4/python2.7/python.exe

print "* CHORISMATE MUTASE WITH CHORISMATE"
print "******"
print "* ATOMS IN QM-REGION ONLY"
print "* "
print "   24 "

n = 1

import sys

lines = open(sys.argv[1], "r").readlines()

for line in lines:
    words = line.split()

    if (len(words) > 3 and words[2] == "CHO"):
        print "%5d    1 %s" % (n, line[11:]),
        n = n + 1
