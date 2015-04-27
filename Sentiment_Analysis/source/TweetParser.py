__author__ = 'rongzuoliu'

import re
from itertools import islice

class TweetParser:
    stop_words_file = 'train_and_test_tweets/stop_words.txt'
    stop_words = []
    reformed_tweet = []

    @staticmethod
    # get stop word list
    def get_stop_words():
        #read the stopwords file and build a list
        TweetParser.stop_words = []
        TweetParser.stop_words.append('AT_USER')
        TweetParser.stop_words.append('HASH_TAG')
        TweetParser.stop_words.append('URL')

        fp = open(TweetParser.stop_words_file, 'r')
        line = fp.readline()
        while line:
            word = line.strip()
            TweetParser.stop_words.append(word)
            line = fp.readline()
        fp.close()
        print 'Stop words are: %s' %TweetParser.stop_words


    def __init__(self):
        TweetParser.get_stop_words() # in case

    def parser_tweets(self, tweet):
        self.self = self
        tweet = self.replace_tags(tweet)
        self.reformed_tweet = self.get_feature_vector(tweet)
        # print 'Original tweet is: %s' %tweet
        # print 'Reformed tweet is: %s' %self.reformed_tweet
        return self.reformed_tweet

    # replace tags such as mentioned tweeters(@), hashtags(#), URL
    def replace_tags(self, tweet):

        #Convert to lower case
        tweet = tweet.lower()
        #Convert www.* or https?://* to URL
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
        #Convert @username to AT_USER
        tweet = re.sub('@[^\s]+','AT_USER', tweet)
        #Replace hashtag #word with the word
        # tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        tweet =  re.sub(r'#([^\s]+)', 'HASH_TAG', tweet)
        #Remove additional white spaces
        tweet = re.sub('[\s]+', ' ', tweet)
        #trim
        tweet = tweet.strip('\'"')
        return tweet


    # delete the repeated characters in a string. e.g. Baddddddddd! -> Bad!
    def delete_repeat_characters(self, s):
        #look for 2 or more repetitions of character and replace with the character itself
        pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
        return pattern.sub(r"\1\1", s)



    # parse tweet to a feature vector
    def get_feature_vector(self, tweet):
        feature_vector = []
        #split tweet into words
        words = tweet.split()

        for w in words:
            #replace two or more with two occurrences
            w = self.delete_repeat_characters(w)
            #strip punctuation
            w = w.strip('\'"?,.')
            #check if the word stats with an alphabet
            val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
            #ignore if it is a stop word
            if(w in TweetParser.stop_words or val is None):
                continue
            else:
                feature_vector.append(w.lower())
        return feature_vector




# def main():
#     tweets_file = 'rt-polarity.pos'
#     TweetParser.get_stop_words()
#     with open(tweets_file) as pos:
#             pos_tweets = islice(pos, 2)
#             for line in pos_tweets:
#                 print line
#                 TweetParser(line)


if __name__ == '__main__':
    # main()
    print 'error!!!'
    print 'The \'TweetParser.py\' is a class, which shouldn\'t be called alone!'
