import csv
from textblob import TextBlob
import os.path

with open('output split by line.txt', mode='r') as f:
    reader = csv.reader(f)
    for num, row in enumerate(reader):
        if 'M50' in row[0]:
            line = (" ".join(row))
            line = line.strip()
            completeName = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/all', "m50.txt")
            x = open(completeName, "a")
            print >> x, line
            x.close()

with open('output split by line.txt', mode='r') as f:
    reader = csv.reader(f)
    for num, row in enumerate(reader):
        if 'Chapelizod' in row[0]:
            line = (" ".join(row))
            line = line.strip()
            completeName = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/all', "chapelizod_bypass.txt")
            x = open(completeName, "a")
            print >> x, line
            x.close()

with open('output split by line.txt', mode='r') as f:
    reader = csv.reader(f)
    for num, row in enumerate(reader):
        if 'Navan' in row[0]:
            line = (" ".join(row))
            line = line.strip()
            completeName = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/all', "navan_rd.txt")
            x = open(completeName, "a")
            print >> x, line
            x.close()

with open('output split by line.txt', mode='r') as f:
    reader = csv.reader(f)
    for num, row in enumerate(reader):
        if 'M1' in row[0]:
            line = (" ".join(row))
            line = line.strip()
            completeName = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/all', "m1.txt")
            x = open(completeName, "a")
            print >> x, line
            x.close()

with open('output split by line.txt', mode='r') as f:
    reader = csv.reader(f)
    for num, row in enumerate(reader):
        if 'Naas' in row[0]:
            line = (" ".join(row))
            line = line.strip()
            completeName = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/all', "naas_rd.txt")
            x = open(completeName, "a")
            print >> x, line
            x.close()