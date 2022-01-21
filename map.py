#!/usr/bin/env python
import sys
from datetime import datetime

for line in sys.stdin:
    line = line.strip()
    columns = line.split(',') # split line into parts
    # the data is messy, only read those having correct column count
    if len(columns) == 6:
        try:
            #ata = [t for t in columns[5] datetime.strptime(t, "%m/%d/%Y %H:%M:%S %p").strftime("%Y%m%d %I:%M:%S")]
            #data = list(map(lambda x: datetime.strptime(x.split("/"), "%m/%d/%Y %I:%M:%S %p"),columns[5]))
            countUpVotes = datetime.strptime(columns[5], "%m/%d/%Y %I:%M:%S %p").hour
            print ("%s\t%s" % (columns[0],countUpVotes))
        except ValueError:
            pass
