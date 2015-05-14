__author__ = 'Xin Huang'
from couchdb.client import Server
from flask import Flask

app = Flask(__name__)
# http://115.146.95.53/ master
# http://115.146.95.246/ replicator
server = Server('http://115.146.95.246:5984')
db = server['twitter_rest']

import views.routes

