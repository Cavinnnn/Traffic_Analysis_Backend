# taken from https://stackoverflow.com/questions/26384787/python-searches-csv-for-string-in-one-column-returns-string-from-another-column
import csv
from collections import defaultdict
import os.path
from firebase import firebase

class accident:
    def __init__(self):
        accidents()
        pass

def accidents():
    may = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/may', "output split by line.txt")
    april = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/april', "output split by line.txt")
    feb = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/febuary', "output split by line.txt")
    jan = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/january', "output split by line.txt")
    dec = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/december', "outputNewLine.txt")

    fin = open(may)
    words = ["accident"]

    found = defaultdict(int)
    for line in fin:
        for word in words:
            if word in line:
               found[word] += 1

    fire = firebase.FirebaseApplication('https://finalyearproject-dfb47.firebaseio.com/')
    fire.post('/accidents/', found[word])

if __name__ == "__main__":
    accident()
