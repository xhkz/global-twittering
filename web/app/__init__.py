__author__ = 'Xin Huang'
import pycouchdb

from flask import Flask

app = Flask(__name__)
server = pycouchdb.Server('http://115.146.95.53:5984')
db = server.database('twitter_rest')

import views.routes

