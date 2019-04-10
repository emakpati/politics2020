# Stream limited number of tweets, filter them (language,location, etc) #
# Passes filtered tweets to sentiment.py #

import setup
import csv
import json
import tweepy
from tweepy import StreamListener


class Streamer(StreamListener):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.limit = 10
        self.statuses = []

    def on_status(self, status):

        if status.retweeted or "RT @" in status.text or status.lang != "en":  # May be an issue
            return
        if len(self.statuses) < self.limit:
            self.statuses.append(status)
            print(len(self.statuses))
        if len(self.statuses) == self.limit:
            with open("/Users/Ekene/Desktop/Yang_Tweets.csv", "w") as file:
                writer = csv.writer(file)
                for status in self.statuses:
                    writer.writerow([status.user.screen_name, status.text, status.created_at, status.user.location,
                                     status.id_str])
            print(self.statuses)
            print("*** Limit of " + str(self.limit) + " met ***")
            return False
        if len(self.statuses) > self.limit:
            streaming.disconnect()


streaming = tweepy.Stream(auth=setup.api.auth, listener=Streamer())

stream_data = streaming.filter(track=["Trump"])

