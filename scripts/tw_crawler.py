#!/usr/bin/python

import tweepy

CONSUMER_KEY = 'CHANGE_TO_YOUR_OWN'
CONSUMER_SEC = 'CHANGE_TO_YOUR_OWN'
ACCESS_TOKEN = 'CHANGE_TO_YOUR_OWN'
ACCESS_SEC = 'CHANGE_TO_YOUR_OWN'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SEC)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SEC)

api = tweepy.API(auth)

data = api.search(geocode='41.85,-87.650,10mi', count=1)



