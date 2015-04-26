__author__ = 'nikki'
import couchdb
import couchdb.design

COUCH_SERVER = 'http://127.0.0.1:5984/'


class DataBaseManager(object):
    def __init__(self, url=COUCH_SERVER):
        try:
            self.server = couchdb.Server(COUCH_SERVER)
            self.db = self.server.create('tweets')
            # self._create_views()
        except couchdb.http.PreconditionFailed:
            self.db = self.server['tweets']

    def save_tweet(self, tw):
        self.db.save(tw)

