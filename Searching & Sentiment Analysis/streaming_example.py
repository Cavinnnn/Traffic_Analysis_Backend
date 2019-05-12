from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

access_token = "1072207016297402380-ShTAjonc5atsJchW5rhsKDVzP1uuN6"
access_token_secret = "I5oV6Fg4Z07zHansLPpXjncsCGBbnFgxiSBzbVgQYOri8"
consumer_key = "Q1mPVE7Bt6uUD1zVt9UWgp6G3"
consumer_secret = "yPqlL0tdmFztCu2zzIy0eYU4NeZWMp9tO5p38i79V4YC04eZrT"

class StdOutListener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        x = open("streaming.txt", "w")
        print >> x, all_data["text"].encode("utf-8")
        x.close()
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords:
    stream.filter(track=['M50 Dublin'])
