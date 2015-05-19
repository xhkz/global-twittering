"""
Author: Team 8
City: Chicago
Subject: COMP90024
"""

from collections import Counter

import couchdb
from textblob import TextBlob

from TextParser import *


# This file aims at finding out the most frequently mentioned words in a branch of tweets in a given view.
# It's used in the report of scenario analysis part.
if __name__ == '__main__':
    server = couchdb.Server('http://115.146.95.53:5984/')
    db = server['twitter_rest']

    TextParser.getStopWords()
    textParser = TextParser()

    counter = Counter()
    for row in db.view('C2E2View/C2E2'):
        blob = TextBlob(textParser.parsing(row.value['what']['text']))
        for word in blob.words:
            counter[word] += 1
    top_words = counter.most_common(20)
