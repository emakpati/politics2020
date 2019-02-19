# Requires api from setup.py #
# Stream limited number of tweets, filter them (language,location, ect) #
# Create list and check that tweets wont break #
# Passes limited list of filtered tweets to sentiment.py #

import setup, topics
import tweepy
from tweepy import StreamListener


class Streamer(StreamListener):

    def __init__(self):
        super().__init__()
        self.counter = 0
        self.limit = 100

    def on_status(self, status):
        if self.counter <= self.limit:
            self.counter += 1
            print(status.text)
            return status.text
        elif self.counter > self.limit:
            print("Limit of " + str(self.limit) + " met.")
            streaming.disconnect()


n = 500

streaming = tweepy.Stream(auth=setup.api.auth, listener=Streamer())
streaming.filter(track=["Bernie"])










