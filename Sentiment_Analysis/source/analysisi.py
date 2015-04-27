__author__ = 'rongzuoliu'

from source.Classifier import *


if __name__ == '__main__':

    classifier = Classifier('train_and_test_tweets/rt-polarity.pos', 'train_and_test_tweets/rt-polarity.neg')

    fp = open('train_and_test_tweets/test_tweets.txt', 'r')
    for line in fp:
        classifier.predict_tweet(line)

    # tweet = 'I love you'
    # classifier.predict_tweet(tweet)

