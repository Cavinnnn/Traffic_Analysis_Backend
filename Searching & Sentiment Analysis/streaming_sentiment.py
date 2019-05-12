from firebase import firebase
from textblob import TextBlob

class Example:
    def __init__(self):
        streaming()
        pass

def streaming():
    with open('streaming.txt', mode='r') as f:
        content = f.readlines()
        line = ', '.join(line.rstrip() for line in content)
        analysis = TextBlob(line)

        print analysis.sentiment.polarity
        if (analysis.sentiment.polarity < 0):
            var = "red"
        elif (analysis.sentiment.polarity > 1):
            var = "green"
        else:
            var = "yellow"

    fire = firebase.FirebaseApplication('https://finalyearproject-dfb47.firebaseio.com/')
    fire.post('/streaming', var)

if __name__ == "__main__":
    Example()