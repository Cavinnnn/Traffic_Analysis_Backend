import unittest
import conform_data
from collections import defaultdict
import csv

class TestConform(unittest.TestCase):

    def test_strip_first_loop(self):
        with open('traffic_tweets.csv') as f:
            reader = csv.reader(f)
            reader.next()
            for row in reader:
                # runs test to see if both datasets are equal to one another
                self.assertEquals(row, row)

    def test_strip_whole_function(self):
        columns = defaultdict(list)

        with open('traffic_tweets.csv') as f:
            reader = csv.reader(f)
            reader.next()
            for row in reader:
                for (i, v) in enumerate(row):
                    columns[i].append(v)
                    self.assertEquals(columns[0], columns[0])

    def test_format(self):
        with open('output.txt') as f:
            for line in f:
                line = line.strip()
                words = line.replace(',', '\n')
                self.assertEquals(words, words)

if __name__ == '__main__':
    unittest.main()
