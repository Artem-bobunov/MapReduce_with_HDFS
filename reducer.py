#!/usr/bin/python

import sys
import operator

oldKey = None
dicHour = {}

print ("ItemBarcode | \tHour")

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2: continue

    thisKey, thisHour = data_mapped

    if oldKey and oldKey != thisKey:
        sorted_hours = sorted(dicHour.items(), key = operator.itemgetter(1), reverse = True)
        topCount = sorted_hours[0][1]
        for tuple in sorted_hours:
            if tuple[1]==topCount: print ("{0}\t{1}".format(oldKey,tuple[0]))

        oldKey = thisKey;
        dicHour = {}

    oldKey = thisKey
    if thisHour in dicHour:
        dicHour[thisHour] += 1
    else:
        dicHour[thisHour] = 1

if oldKey != None:
    sorted_hours = sorted(dicHour.items(), key = operator.itemgetter(1), reverse = True)
    topCount = sorted_hours[0][1]
    for tuple in sorted_hours:
        if tuple[1]==topCount: print ("{0}\t{1}".format(oldKey,tuple[0]))
