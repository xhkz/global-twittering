__author__ = 'tuhung-te'


import couchdb
import pycouchdb
from flask import render_template, jsonify

class dbrepository:

    def __init__(self):
        self.db_name = 'twitter_test'
        self.url = 'http://115.146.95.53:5984/'
        #server = pycouchdb.Server(self.url)
        #self.db = server.database(self.db_name)
        #server = couchdb.Database(url=self.url,self.db_name);
        self.db = couchdb.Database(url=self.url+self.db_name);

    def list(self,list_name,view_name):

        #data = list(self.db.query(view_name,group='true',limit=10));
        data = self.db.list(list_name,view_name,group='true');
        #data = self.db.list("top10/results","top10/test",group='true',limit='10');
        return data

    def view(self,view_name):
        rows = self.db.view(view_name,group='true',descending='true',limit='10')
        return rows

