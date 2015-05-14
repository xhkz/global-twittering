__author__ = 'rongzuoliu'


import couchdb
from textblob.en.sentiments import NaiveBayesAnalyzer, PatternAnalyzer
from textblob import TextBlob

from TextParser import *



def main():

    dbname = 'twitter_rest'
    viewname = 'HashtagsView/Hashtags'

    server = couchdb.Server(url= "http://115.146.95.53:5984/")
    # server = couchdb.Server()
    # dbname = 'liberal_followers'
    # viewname = 'LaborView/Labor'

    db = server[dbname]

    # TextParser.getStopWords()
    # textParser = TextParser()

    for row in db.view(viewname):
        # print row.value
        id = row.id
        doc = db.get(id)
        text = row.value['what']['text']
        print text
        # parsed_text = textParser.parsing(text)
        # (sentiment, senti_score) = sentiAnalysisWithTextBlob(text, "NaiveBayesAnalyzer")
        (sentiment, senti_score) = sentiAnalysisWithTextBlob(text, "PatternAnalyzer")
        doc['sentiment'] = { "sentiment": sentiment, "sentiScore": senti_score}
        # # print doc
        db.save(doc)



def sentiAnalysisWithTextBlob(string, classifier):

    sentiment = ''
    senti_score = -100
    if (classifier == "NaiveBayesAnalyzer"):
        blob = TextBlob(string, analyzer= NaiveBayesAnalyzer())
        # pos/neg is rang from 0-1, the number is bigger, the feeling is stronger
        senti_score = blob.sentiment.p_pos
        if (senti_score == 0.5):
            sentiment = 'neu'
        else:
            sentiment = blob.sentiment.classification


    elif (classifier == "PatternAnalyzer"):
        blob = TextBlob(string)
        senti_score = blob.sentiment.polarity
        if (blob.sentiment.polarity > 0):
            sentiment = 'pos'
        elif (blob.sentiment.polarity == 0):
            sentiment = 'neu'
        elif (blob.sentiment.polarity < 0):
            sentiment = 'neg'

    # print sentiment
    # print senti_score

    return (sentiment, senti_score)



if __name__ == '__main__':
    main()