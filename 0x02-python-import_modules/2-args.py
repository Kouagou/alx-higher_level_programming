#!/usr/bin/python3
import sys
if len(sys.argv) == 1:
    print('{:d} argument'.format(len(sys.argv)))
else:
    print('{:d} arguments'.format(len(sys.argv) -1))

for i in range(1, len(sys.argv)):
    print('{:d}: {}'.format(i, sys.argv[i]))
