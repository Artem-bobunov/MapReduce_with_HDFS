#!/usr/bin/python
import sys
import csv

def mapper():

    reader = csv.reader(sys.stdin, delimiter=',')
    writer = csv.writer(sys.stdout, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for line in reader:

        if len(line)!=6:
            continue
        # check bibnumber
        if str.isdigit(line[0]) == False:
            continue

        keyValPair = []
        keyValPair.append(line[0])
        keyValPair.append(1)

        writer.writerow(keyValPair)

def main():
    mapper()
    sys.stdin = sys.__stdin__

if __name__ == "__main__":
    main()
