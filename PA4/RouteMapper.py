#!/usr/bin/env python3

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    line = line.split(",")
    # increase counters
    for airline in line: 
        airline = line[1]
        #print(airline,len(airline))
        origin = line[4]
        destination = line[9]
        delay = line[14]
        if delay == "":
            continue
        if airline == "\"B6\"" or airline == "\"G4\"" or airline == "\"MQ\"":
            print ("{0}\t{1}\t{2}\t{3}".format(airline, origin, destination, delay))