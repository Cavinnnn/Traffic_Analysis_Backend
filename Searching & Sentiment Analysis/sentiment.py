from textblob import TextBlob
from firebase import firebase
import os.path

class sentiment:
    def __init__(self):
        m50()
        m1()
        chapelizod()
        navan()
        naas()
        pass

def m50():
    completeName = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/all', "m50.txt")
    with open(completeName) as f:
        content = f.readlines()
        line = ', '.join(line.rstrip() for line in content)
        analysis = TextBlob(line)

        if(analysis.sentiment.polarity < 0):
            var = "red"
        elif(analysis.sentiment.polarity > 1):
            var = "green"
        else:
            var = "yellow"

    fire = firebase.FirebaseApplication('https://finalyearproject-dfb47.firebaseio.com/')
    fire.post('/sentiment/all/m50', var)

def m1():
    completeName = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/all', "m1.txt")
    with open(completeName) as f:
        content = f.readlines()
        line = ', '.join(line.rstrip() for line in content)
        analysis = TextBlob(line)

        if(analysis.sentiment.polarity < 0):
            var = "red"
        elif(analysis.sentiment.polarity > 1):
            var = "green"
        else:
            var = "yellow"

    fire = firebase.FirebaseApplication('https://finalyearproject-dfb47.firebaseio.com/')
    fire.post('/sentiment/all/m1', var)

def chapelizod():
    completeName = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/all', "chapelizod_bypass.txt")
    with open(completeName) as f:
        content = f.readlines()
        line = ', '.join(line.rstrip() for line in content)
        analysis = TextBlob(line)

        if (analysis.sentiment.polarity < 0):
            var = "red"
        elif (analysis.sentiment.polarity > 1):
            var = "green"
        else:
            var = "yellow"

    fire = firebase.FirebaseApplication('https://finalyearproject-dfb47.firebaseio.com/')
    fire.post('/sentiment/all/chapelizod', var)

def navan():
    completeName = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/all', "navan_rd.txt")
    with open(completeName) as f:
        content = f.readlines()
        line = ', '.join(line.rstrip() for line in content)
        analysis = TextBlob(line)

        if (analysis.sentiment.polarity < 0):
            var = "red"
        elif (analysis.sentiment.polarity > 1):
            var = "green"
        else:
            var = "yellow"

    fire = firebase.FirebaseApplication('https://finalyearproject-dfb47.firebaseio.com/')
    fire.post('/sentiment/all/navan', var)

def naas():
    completeName = os.path.join('C:/Code/Traffic_Analysis/Searching & Sentiment Analysis/all', "naas_rd.txt")
    with open(completeName) as f:
        content = f.readlines()
        line = ', '.join(line.rstrip() for line in content)
        analysis = TextBlob(line)

        if (analysis.sentiment.polarity < 0):
            var = "red"
        elif (analysis.sentiment.polarity > 1):
            var = "green"
        else:
            var = "yellow"

    fire = firebase.FirebaseApplication('https://finalyearproject-dfb47.firebaseio.com/')
    fire.post('/sentiment/all/naas', var)

if __name__ == "__main__":
    sentiment()