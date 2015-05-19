"""
Author: Team 8
City: Chicago
Subject: COMP90024
"""
from couchdb.client import Server
from flask import Flask

app = Flask(__name__)
server = Server('http://115.146.95.246:5984')
db = server['twitter_rest']

import views.routes
import views.data_api
