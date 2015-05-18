__author__ = 'nikki'
import time
import datetime

from whoosh.analysis import RegexTokenizer
from whoosh.analysis import LowercaseFilter
from whoosh.analysis import StopFilter
from TwitterAPI.TwitterAPI import TwitterAPI

from settings import app_auth, locations


class TwitterAPIAccess(object):
    def __init__(self, database_manager, stop_words, user_name, zone_index):
        self.dm = database_manager
        self.filter = RegexTokenizer() | LowercaseFilter() | StopFilter() | StopFilter(stop_words)
        self.zone_index = zone_index
        self.api = TwitterAPI(app_auth[user_name].ckey, app_auth[user_name].csec,
                              app_auth[user_name].atoken, app_auth[user_name].asec)

    def start_stream(self):
        while True:
            try:
                print 'in stream...'
                response = self.api.request('statuses/filter', {'locations': locations[self.zone_index]})
                for tweet in response:
                    filtered_tweet = self.map_tweet_fields(dict(tweet))
                    if self.dm.not_exist(filtered_tweet['_id']):
                        print "insert {0}".format(tweet["id_str"])
                        self.dm.save_tweet(filtered_tweet)
            except KeyboardInterrupt:
                print('TERMINATED BY USER')
                break
            except Exception as e:
                print('STOPPED: %s %s' % (type(e), e))

    @staticmethod
    def map_tweet_fields(json_object):
        response = {
            "_id": json_object["id_str"],
            "user": {
                "name": json_object["user"]["name"],
                "screen_name": json_object["user"]["screen_name"],
                "followers_count": json_object["user"]["followers_count"],
                "location": json_object["user"]["location"],
                "description": json_object["user"]["description"],
                "statuses_count": json_object["user"]["statuses_count"],
                "friends_count": json_object["user"]["friends_count"],
                "listed_count": json_object["user"]["listed_count"]
            },
            "where": {
                "coordinates": json_object["coordinates"]["coordinates"] if json_object["coordinates"] else None
            },
            "what": {
                "text": json_object["text"],
                "entities": json_object["entities"],
                "lang": json_object["lang"]
            },
            "about": {
                "retweet_count": json_object["retweet_count"],
                "source": json_object["source"],
                "favorite_count": json_object["favorite_count"]
            },
            "when": {
                "created_at_str": json_object["created_at"],
                "created_at_timestamp": time.mktime(
                    datetime.datetime.strptime(json_object["created_at"], "%a %b %d %H:%M:%S +0000 %Y").timetuple())
            }
        }

        return response
