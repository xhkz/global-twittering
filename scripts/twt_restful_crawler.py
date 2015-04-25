#!/usr/bin/env python
import argparse
import time

import pycouchdb
import tweepy


# configuration
DB_NAME = 'twitter'
COUCHDB_URI = 'http://localhost:5984/'
CONSUMER_KEY = '04ERby2gwInEOTodxbLyGNbrZ'
CONSUMER_SEC = 'poVkXJvOhnuwlc1AkaQuDWpO4N6YNZEmlB0YgS4rCRM1GHhOMQ'
ACCESS_TOKEN = '2803020907-1d9ShXZ2tRzO1EzrP1QDyk42TpiOdubDnp7ekfa'
ACCESS_SEC = 'py2YB88r2YsP45gC7Fs3TbfVfxnG4Ef3gIn48gF5bepB0'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SEC)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SEC)
api = tweepy.API(auth)
server = pycouchdb.Server(COUCHDB_URI)

db = server.database(DB_NAME)
geo_code = '41.85,-87.650,10mi'
tweets_count = 10


def init_data():
    save_data(api.search(geocode=geo_code, count=1, result_type='recent'))


def init_doc():
    _doc = {
        "_id": "_design/twitter_doc",
        "views": {
            "stats": {
                "map": "function(doc) { emit(null, doc.id); }",
                "reduce": "_stats",
            }
        }
    }
    db.save(_doc)


def save_data(json_data):
    for item in json_data:
        db.save(item._json)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', action='store_true', help='init or not')
    args = parser.parse_args()

    if args.init:
        init_data()
        init_doc()
    else:
        # continuously get old tweets
        # max: 1 request per 5 seconds
        while True:
            min_id = list(db.query('twitter_doc/stats'))[0]['value']['min']
            data = api.search(geocode=geo_code, count=tweets_count, result_type='recent', max_id=min_id)
            save_data(data)
            time.sleep(10)






