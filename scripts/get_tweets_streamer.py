__author__ = 'nikki'
import sys

import couchdb

from settings import couchdb_uri, db_name
from tweets.twitter_access import *


class DataBaseManager(object):
    def __init__(self):
        try:
            self.server = couchdb.Server(couchdb_uri)
            self.db = self.server.create(db_name)
        except couchdb.http.PreconditionFailed:
            self.db = self.server[db_name]

    def save_tweet(self, tw):
        self.db.save(tw)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "please provide user name and zone index"
        exit(-1)

    user_name = sys.argv[1]
    zone_index = int(sys.argv[2])
    if user_name not in app_auth:
        print "user name is incorrect"
        exit(-1)

    database_manager = DataBaseManager()
    app = TwitterAPIAccess(database_manager, None, user_name, zone_index)
    app.start_stream()
