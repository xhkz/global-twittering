#!/usr/bin/env python
"""
Author: Team 8
City: Chicago
Subject: COMP90024
"""
import sys

import couchdb

from settings import couchdb_uri, db_name, app_auth
from tweets.twitter_access import TwitterAPIAccess


class DataBaseManager(object):
    def __init__(self):
        try:
            self.server = couchdb.Server(couchdb_uri)
            self.db = self.server.create(db_name)
        except couchdb.http.PreconditionFailed:
            self.db = self.server[db_name]

    def save_tweet(self, tw):
        try:
            self.db.save(tw)
        except couchdb.HTTPError as e:
            print 'duplicated'

    def not_exist(self, tid):
        return self.db.get(tid) is None


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "please provide user name and zone index"
        exit(-1)

    user_name = sys.argv[1]
    zone_index = int(sys.argv[2])
    if user_name not in app_auth:
        print "user name is incorrect"
        exit(-1)

    app = TwitterAPIAccess(DataBaseManager(), None, user_name, zone_index)
    app.start_stream()
