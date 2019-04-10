# Requires tweets from stream.py #
# Passes avg polarity to post #

import stream
from textblob import TextBlob
import numpy as np, time

# Maybe have one func that returns a tuple and then unpack it later


def get_polarity(arr_of_tweets):
    # return hash of tweet as key and polarity score as value
    pol_hash = {}
    print(type(arr_of_tweets))
    # for tweet in arr_of_tweets:
    #     tweet = str(tweet)
    #     temp_arr = TextBlob(tweet)
    #     pol_hash[tweet] = temp_arr.polarity



def get_avg_polarity(polarity_arr):
    # return mean of list from get_polarity
    avg_polarity = np.mean(polarity_arr)
    return avg_polarity


def get_subjectivity(arr_of_tweets):
    # return list of subjectivity scores
    sub_list = []


def get_avg_subjectivity(subjectivity_arr):
    # return mean of list from get_subjectivity
    avg_subjectivity = np.mean(subjectivity_arr)
    return avg_subjectivity



