__author__ = 'tuhung-te'

import views.dbRepository


class viewRepository(object):


    def top10twettersView(self):
        db =views.dbRepository.dbrepository();
        #db.view("Topic10Views/mostfollowers",10)
        rows =db.list("Topic10Views/sort","Topic10Views/mostfollowers")

    def latest100Tweets(self):
        db = views.dbRepository.dbrepository();
        rows= db.view("top10/latest100Twetts")
        for row in rows:
            print(row['key'][0]['contents'])
            print(row['key'][0]['time'])