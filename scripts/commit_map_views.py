import json
from couchdb.client import Server

server = Server('http://115.146.95.53:5984')
db = server['twitter_rest']

with open('map_views.json', 'r') as f:
    doc = json.load(f)
    db.save(doc)