__author__ = 'rongzuoliu'

import couchdb
from textblob import TextBlob
from collections import Counter
from TextParser import *

# This file aims at finding out the most frequently mentioned words in a branch of tweets in a given view.
# It's used in the report of scenario analysis part.
def main():

    dbname = 'twitter_rest'
    viewname = 'C2E2View/C2E2'
    server = couchdb.Server(url= "http://115.146.95.53:5984/")
    db = server[dbname]

    TextParser.getStopWords()
    textParser = TextParser()

    words_dict = {}
    for row in db.view(viewname):
        text = row.value['what']['text']
        parsed_text = textParser.parsing(text)
        blob = TextBlob(parsed_text)
        words_list = blob.words
        for word in words_list:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    print words_dict
    words_Counter = Counter(words_dict)
    top_words = words_Counter.most_common(20)
    # print top_words


if __name__ == '__main__':
    main()