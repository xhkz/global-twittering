__author__ = 'nikki'
import calendar
import json
import re
import time
from whoosh.analysis import RegexTokenizer
from whoosh.analysis import LowercaseFilter
from whoosh.analysis import StopFilter
from TwitterAPI.TwitterAPI import TwitterAPI



class TwitterAPIAccess(object):

    def __init__(self, database_manager, publisher, configuration_list, stop_words):
        self.db = database_manager
        self.user_info = configuration_list
        self.publisher = publisher
        self.filter = RegexTokenizer() | \
                      LowercaseFilter() | \
                      StopFilter() | \
                      StopFilter(stop_words)
        self.api    = TwitterAPI(self.user_info["API_KEY"], self.user_info["API_SECRET"], self.user_info["ACCESS_TOKEN"], self.user_info["ACCESS_TOKEN_SECRET"])

    def start_stream(self):
        while True:
            try:
                print 'in stream'
                r = self.api.request('statuses/filter', {'locations': self.user_info["locations"]})
                for tweet in r:
                    filtered_tweet = self.map_tweet_fields(dict(tweet))
                    if filtered_tweet != None:
                        print "attempting db insert and publish for {0}".format(tweet["id_str"])
                        if self.db != None:
                            self.db.save_tweet(filtered_tweet)
                        if self.publisher != None:
                            self.publisher.publish(json.dumps(filtered_tweet))
            except KeyboardInterrupt:
                print('TERMINATED BY USER')
                break
            except Exception as e:
                print('STOPPED: %s %s' % (type(e), e))
                break
    def map_tweet_fields(self, json_object):
        # If coordinates is not populated, then the tweet was was not within bounds
        if json_object['coordinates'] == None:
            return None
        else:
            response = {}
            response['_id'] = json_object['id_str']
            response['shard'] = json_object['coordinates']['coordinates'][0]
            (stripped_text, link_array) = self.strip_links(json_object['text'])
            tokens = [token.text for token in self.filter(stripped_text)]
            response['what'] = {'text': json_object['text'],
                            'tokens': tokens,
                            'link_array': link_array,
                            'tag': self.user_info['tag'],
                            'retweet_count': json_object['retweet_count'],
                            'followers_count': json_object['user']['followers_count'],
                            'hashtags': json_object['entities']['hashtags'],
                            'id': json_object['id_str']}
            lat = json_object['coordinates']['coordinates'][1]
            lon = json_object['coordinates']['coordinates'][0]
            response['where'] = {'location': [lat, lon],
                                "latitude" : lat,
                                "longitude" : lon}
            timestamp = time.strptime(json_object['created_at'],
                                  '%a %b %d %H:%M:%S +0000 %Y')
            response['when'] = {'date': calendar.timegm(timestamp) * 1000,
                            'shardtime': calendar.timegm(timestamp) * 1000}
            response['who'] = {'id': json_object['user']['id'],
                           'screen_name': json_object['user']['screen_name'],
                           'description': json_object['user']['description'],
                           'location': json_object['user']['location']}
            response['type'] = 'tweet'
            return response

    def strip_links(self, status):
        links = re.findall(r'(https?://\S+)', status)
        for url in links:
            status = status.replace(url, '')
        return (status, links)



