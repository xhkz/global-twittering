__author__ = 'nikki'
from tweets.twitter_access import *
from tweets.database_manager import *
from tweets.twitter_info import user_info
#from twitter_info import stop_words

database_manager = DataBaseManager(user_info)
app = TwitterAPIAccess(database_manager, None, user_info, None);
app.start_stream();
