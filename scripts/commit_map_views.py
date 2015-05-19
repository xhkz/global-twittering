#!/usr/bin/env python
"""
Author: Team 8
City: Chicago
Subject: COMP90024
"""
import json

from couchdb.client import Server

server = Server('http://115.146.95.53:5984')
db = server['twitter_rest']

with open('map_views.json', 'r') as f:
    db.save(json.load(f))
