#!/usr/bin/env python
import argparse
import time
import datetime

import pycouchdb
import tweepy

from settings import app_auth, couchdb_uri, db_name


auth = tweepy.OAuthHandler(app_auth['xin'].ckey, app_auth['xin'].csec)
auth.set_access_token(app_auth['xin'].atoken, app_auth['xin'].asec)
api = tweepy.API(auth)
server = pycouchdb.Server(couchdb_uri)
if db_name not in server:
    server.create(db_name)

db = server.database(db_name)

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
        j = item._json
        data = {
            "id": j["id"],
            "user": {
                "name": j["user"]["name"],
                "screen_name": j["user"]["screen_name"],
                "followers_count": j["user"]["followers_count"],
                "location": j["user"]["location"],
                "description": j["user"]["description"],
                "statuses_count": j["user"]["statuses_count"],
                "friends_count": j["user"]["friends_count"],
                "listed_count": j["user"]["listed_count"]
            },
            "where": {
                "coordinates": j["coordinates"]["coordinates"] if j["coordinates"] else None
            },
            "what": {
                "text": j["text"],
                "entities": j["entities"],
                "lang": j["lang"]
            },
            "about": {
                "retweet_count": j["retweet_count"],
                "source": j["source"],
                "favorite_count": j["favorite_count"]
            },
            "when": {
                "created_at_str": j["created_at"],
                "created_at_timestamp": time.mktime(
                    datetime.datetime.strptime(j["created_at"], "%a %b %d %H:%M:%S +0000 %Y").timetuple())
            }
        }
        db.save(data)


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






