__author__ = 'rongzuoliu'

import couchdb
from textblob.en.sentiments import NaiveBayesAnalyzer
from textblob import TextBlob

from TextParser import *


def main():
    dbname = 'twitter_rest'
    viewname = 'HashtagsView/Hashtags'

    server = couchdb.Server(url="http://115.146.95.53:5984/")
    db = server[dbname]

    for row in db.view(viewname):
        id = row.id
        doc = db.get(id)
        text = row.value['what']['text']
        print text
        (sentiment, senti_score) = sentiAnalysisWithTextBlob(text, "PatternAnalyzer")
        doc['sentiment'] = {"sentiment": sentiment, "sentiScore": senti_score}
        db.save(doc)


def sentiAnalysisWithTextBlob(string, classifier):
    sentiment = ''
    senti_score = -100
    if classifier == "NaiveBayesAnalyzer":
        blob = TextBlob(string, analyzer=NaiveBayesAnalyzer())
        senti_score = blob.sentiment.p_pos
        if senti_score == 0.5:
            sentiment = 'neu'
        else:
            sentiment = blob.sentiment.classification

    elif classifier == "PatternAnalyzer":
        blob = TextBlob(string)
        senti_score = blob.sentiment.polarity
        if blob.sentiment.polarity > 0:
            sentiment = 'pos'
        elif blob.sentiment.polarity == 0:
            sentiment = 'neu'
        elif blob.sentiment.polarity < 0:
            sentiment = 'neg'

    return sentiment, senti_score


if __name__ == '__main__':
    main()
