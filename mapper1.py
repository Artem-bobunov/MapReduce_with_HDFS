#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',')
    if len(columns) == 6:
        try:
            print ("{}\t{}".format(columns[2],1))
        except ValueError:
            pass
