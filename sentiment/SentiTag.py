"""
Author: Team 8
City: Chicago
Subject: COMP90024
"""

import couchdb
from textblob import TextBlob

from TextParser import *


def analyze(string):
    sentiment = ''
    blob = TextBlob(string)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = 'pos'
    elif polarity == 0:
        sentiment = 'neu'
    elif polarity < 0:
        sentiment = 'neg'

    return sentiment, polarity


if __name__ == '__main__':

    server = couchdb.Server('http://115.146.95.53:5984')
    db = server['twitter_rest']

    TextParser.getStopWords()
    textParser = TextParser()
    for row in db.view('C2E2View/C2E2'):
        doc = db.get(row.id)
        (tag, score) = analyze(textParser.parsing(row.value['what']['text']))
        doc['sentiment'] = {'sentiment': tag, 'sentiScore': score}
        db.save(doc)
