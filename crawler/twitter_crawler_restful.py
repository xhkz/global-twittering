#!/usr/bin/env python
"""
Author: Team 8
City: Chicago
Subject: COMP90024
"""
import argparse
import time
from datetime import datetime

import pycouchdb
import tweepy

from settings import app_auth, couchdb_uri

db_name = 'twitter_rest'
db_org_name = 'twitter_org'
user = 'xin'
auth = tweepy.OAuthHandler(app_auth[user].ckey, app_auth[user].csec)
auth.set_access_token(app_auth[user].atoken, app_auth[user].asec)
api = tweepy.API(auth)
server = pycouchdb.Server(couchdb_uri)
if db_name not in server:
    server.create(db_name)

if db_org_name not in server:
    server.create(db_org_name)

db = server.database(db_name)
db_org = server.database(db_org_name)

geo_code = '41.85,-87.650,15mi'
tweets_count = 100
max_id = 0


def get_recent_one():
    while True:
        one = api.search(geocode=geo_code, count=1, result_type='recent')
        time.sleep(10)
        if len(one) >= 1:
            return one


def init_data():
    save_data(get_recent_one())


def init_doc():
    _doc = {
        "_id": "_design/twitter_doc",
        "views": {
            "min": {
                "map": "function(doc) { emit(null, doc._id); }",
                "reduce":
                    """
                    function(keys, values) {
                        var min = "999999999999999999";
                        for (var idx in values)
                            if (values[idx] < min) {min = values[idx];}
                        return min;
                    }
                    """
            }
        }
    }
    db.save(_doc)


def save_data(statuses):
    global max_id
    count = 0
    for item in statuses:
        max_id = min(item.id, max_id)
        j = item._json
        if j["id_str"] not in db:
            db.save({
                "_id": j["id_str"],
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
                        datetime.strptime(j["created_at"], "%a %b %d %H:%M:%S +0000 %Y").timetuple())
                }
            })
            db_org.save(j)
            count += 1

    return count


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', action='store_true', help='init or not')
    args = parser.parse_args()

    if args.init:
        init_data()
        init_doc()
    else:
        # continuously get old tweets and update max_id if necessary
        # max: 1 request per 5 seconds
        max_id = get_recent_one()[0].id
        no_save = 0
        while True:
            data = api.search(geocode=geo_code, count=tweets_count, result_type='recent', max_id=max_id)
            save_len = save_data(data)
            print '[%s] max_id: %s, get: %s, save: %s' % (datetime.now(), max_id, len(data), save_len)
            time.sleep(10)
            no_save = no_save + 1 if save_len == 0 else 0

            if no_save >= 20:
                max_id = get_recent_one()[0].id
                no_save = 0
