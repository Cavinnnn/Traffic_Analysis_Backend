import csv
import re
from collections import defaultdict
import time

class Conform:
    def __init__(self):
        strip()
        format()
        pass

# https://stackoverflow.com/questions/43986126/how-to-search-for-a-text-or-number-in-a-csv-file-with-python-and-if-exists-p?rq=1

def strip():
    start = time.time()
    columns = defaultdict(list)

    with open('traffic_tweets.csv') as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            for (i,v) in enumerate(row):
                columns[i].append(v)
                x = open("output.txt", "w")
    print >> x, columns[0]
    x.close()
    end = time.time()
    print("Time for strip: ", end - start)


def format():
    start = time.time()
    with open('output.txt') as f:
        for line in f:
            line = line.strip()
            words = line.replace(',', '\n')
            x = open("outputNewLine.txt", "w")
    print >> x, words
    x.close()
    end = time.time()
    print("Time for format: ", end - start)

if __name__ == "__main__":
    Conform()
