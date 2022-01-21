#!/usr/bin/env python
import sys

ItemTypeCount = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        ItemTypeCount[word] = ItemTypeCount[word]+count
    except:
        ItemTypeCount[word] = count

for word in ItemTypeCount.keys():
    print ('%s\t%s'% ( word, ItemTypeCount[word] ))
