__author__ = 'Xin Huang'


class Keys():
    """
        CONSUMER_KEY
        CONSUMER_SEC
        ACCESS_TOKEN
        ACCESS_SEC
    """

    def __init__(self, ckey, csec, atoken, asec):
        self.ckey = ckey
        self.csec = csec
        self.atoken = atoken
        self.asec = asec


db_name = 'twitter'
couchdb_uri = 'http://115.146.93.76:5984'
app_auth = {
    'xin': Keys(
        '04ERby2gwInEOTodxbLyGNbrZ',
        'poVkXJvOhnuwlc1AkaQuDWpO4N6YNZEmlB0YgS4rCRM1GHhOMQ',
        '2803020907-1d9ShXZ2tRzO1EzrP1QDyk42TpiOdubDnp7ekfa',
        'py2YB88r2YsP45gC7Fs3TbfVfxnG4Ef3gIn48gF5bepB0'
    ),

    'nikvi': Keys(
        'Gkov4WGDeIViDSct84klCJCoO',
        'xhdByIyeTSwU8byraNJg6b1RalyodjbILbhEsvSI0RRqMRUyh4',
        '47649768-W9aZXo9oQcQ8WYbYNn1YcEOaUrajxJrlAVne18VB2',
        'YorFM0a2VfgE6t7VffMpBfzPBbRul01a5tafJubi382h3'
    )
}

locations = [
    ["-87.940267,41.946774", "-87.524044, 42.023131"],
    ["-87.862968,41.870391", "-87.524044,41.946774"],
    ["-87.862968,41.794034", "-87.524044,41.870391"],
    ["-87.862968,41.717677", "-87.524044,41.794034"],
    ["-87.862968,41.644335", "-87.524044,41.717677"]
]