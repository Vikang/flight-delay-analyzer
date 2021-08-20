#!/usr/bin/env python3

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    line = line.split(",")
    # increase counters

    for code in line:
        if line[16] is not None: 
                code = line[16]

        print ("{0}\t1".format(code))