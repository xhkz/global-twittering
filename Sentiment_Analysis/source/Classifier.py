__author__ = 'rongzuoliu'

import nltk

from source.TweetParser import *


class Classifier:
    tweets = []
    training_set = []

    def __init__(self, pos_tweets_file, neg_tweets_file):
        # initiate positive tweets
        self.self = self

        parser = TweetParser()
        with open(pos_tweets_file) as pos:
            pos_tweets = islice(pos, 5000) # 5330 items in total
            for line in pos_tweets:
                self.tweets.append((parser.parser_tweets(line), 'positive'))
                # self.tweets.append(([line], 'positive'))

        with open(neg_tweets_file) as neg:
            neg_tweets = islice(neg, 5000) # 5330 items in total
            for line in neg_tweets:
                self.tweets.append((parser.parser_tweets(line), 'negative'))
                # self.tweets.append(([line], 'negative'))

        # for t in self.tweets:
        #     print t

        # initiate the training set
        print 'Initiating training tweets...'
        self.init_training_set()
        # for word, is_contain in self.training_set:
        #     print '%s       %s\n' %(word, is_contain)

        print 'Processing with Naive Bayes Classifier...'
        self.classifier = nltk.NaiveBayesClassifier.train(self.training_set)
        # print classifier.show_most_informative_features(40)
        # print classifier._label_probdist
        # print classifier._label_probdist.prob('positive')
        # print classifier._label_probdist.prob('negative')



    # get all words in tweets, return a words of list
    def get_words_in_tweets(self):
        all_words = []
        for (words, sentiment) in self.tweets:
            all_words.extend(words)
        return all_words

    # get the frequencies of the words in the word list, return a word-features list
    def get_word_features(self, words_list):
        word_freq_dict = nltk.FreqDist(words_list) # word_freq_dict is a dic with word-feature as key, its frequency as value
        word_features = word_freq_dict.keys()
        return word_features

    # extract the word-features a doc/tweet contains.
    # return a dictionary features, whose key is 'contains(some_word)', value is True/False
    def extract_features(self, a_tweet):
        words_list = self.get_words_in_tweets()
        word_features = self.get_word_features(words_list)
        a_tweet_words = set(a_tweet)
        features = {}
        for word in word_features:
            features['contains(%s)' % word] = (word in a_tweet_words)
        return features

    # initiate training set
    def init_training_set(self):
        self.training_set = nltk.classify.apply_features(self.extract_features, self.tweets)


    def predict_tweet(self, a_tweet):
        result = self.classifier.classify(self.extract_features(a_tweet.split()))
        print result
        return result


if __name__ == '__main__':
    print 'error!!!'
    print 'The \'Classifier.py\' is a class, which shouldn\'t be called alone!'

















