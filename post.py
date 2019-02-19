# Requires api from setup.py and avg polarity from sentiment.py #
# Updates status #

import setup, stream, topics, sentiment as snt

setup.api.update_status("Twitter's sentiment about " + str(topics.topic) + ": n = " + stream.n + ", avg polarity = " +
                        snt.get_avg_polarity() + "avg subjectivity = " + snt.get_avg_subjectivity())

