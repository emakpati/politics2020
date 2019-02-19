# Keys and API #
# Passes api to stream.py and post.py #

import tweepy

cons_key = "5du9HRI8VUyEz2w4Sde5YV97I"
cons_sec = "SPujaHr71WjMu86sImDQr83liqEm2utDJTqE1FTVgVknP2RF4b"

acc_key = "875013129356288000-PjXSBbMJRM8ZMvULQsNlIvz6EWNOpkU"
acc_sec = "3OlzlzSFzcZzzYU5mRD2hAWr3cMzRP6b6U37ciS0ru2rj"

auth = tweepy.OAuthHandler(cons_key, cons_sec)
auth.set_access_token(acc_key, acc_sec)

api = tweepy.API(auth)




