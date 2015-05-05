__author__ = 'rongzuoliu'

from textblob.en.sentiments import NaiveBayesAnalyzer, PatternAnalyzer
from textblob import Word
from textblob import TextBlob

def sentiAnalysisWithTextBlob(string, classifier):

    sentiment = ''
    if (classifier == "NaiveBayesAnalyzer"):
        blob = TextBlob(string, analyzer= NaiveBayesAnalyzer())
        # print blob.tags
        # print blob.sentiment
        sentiment = blob.sentiment.classification

    elif (classifier == "PatternAnalyzer"):
        blob = TextBlob(string)
        # print blob.sentiment
        if (blob.sentiment.polarity > 0):
            sentiment = 'pos'
        elif (blob.sentiment.polarity == 0):
            sentiment = 'neu'
        elif (blob.sentiment.polarity < 0):
            sentiment = 'neg'

    return sentiment

