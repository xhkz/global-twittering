"""
Author: Team 8
City: Chicago
Subject: COMP90024
"""


class Keys:
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


db_name = 'twitter_rest'
couchdb_uri = 'http://115.146.95.53:5984'
app_auth = {
    'xin': Keys(
        '04ERby2gwInEOTodxbLyGNbrZ',
        'poVkXJvOhnuwlc1AkaQuDWpO4N6YNZEmlB0YgS4rCRM1GHhOMQ',
        '2803020907-1d9ShXZ2tRzO1EzrP1QDyk42TpiOdubDnp7ekfa',
        'py2YB88r2YsP45gC7Fs3TbfVfxnG4Ef3gIn48gF5bepB0'
    ),

    'xin2': Keys(
        'pwsPSOEtWTt2m1OO5wQAby3iW',
        'xIB4aM18OklGrtNqQjqFrugJUHUBTT274hn02TjUxAAAsI2Fa1',
        '2803020907-m2W3Q7WeDSSMcnh2rFgChLXuTxg0oYZQdRnUFnc',
        '7srtksL6zIIUVc29SzYYRuZIwFbU35mx0ExRSChOMvp0k'
    ),

    'nikvi': Keys(
        'Gkov4WGDeIViDSct84klCJCoO',
        'xhdByIyeTSwU8byraNJg6b1RalyodjbILbhEsvSI0RRqMRUyh4',
        '47649768-W9aZXo9oQcQ8WYbYNn1YcEOaUrajxJrlAVne18VB2',
        'YorFM0a2VfgE6t7VffMpBfzPBbRul01a5tafJubi382h3'
    ),

    'zoey': Keys(
        "JuDAs23ssLkzgGv7HAzA08Rfd",
        "R4xrvBWIzU1Mqd7BU13hX4AiHmzRqNQIJUhXNXZZYH661TIX6h",
        "808402454-1JJqi9TDziPasFusqXRoiFcYnvBOAyzcuCZMkZHT",
        "lbZjgJI7S44A1HZdYE2p13PoAdHyqDAkCFbZfG0EBsTNH"
    ),

    'jacky': Keys(
        "ijnHtRNQixWg7o5EzoSPB8VgJ",
        "IDo3LZbqoYyXcvACpwwuseuFiCIWmV05W6EFh35HUjyHkKzJZ4",
        "3180754530-RHk7GnQsNvUbDBEX6kvATVEFWEGbsnnWiAV6ODX",
        "2e43UNUqa6oCZfwFMym5rftu0LpBF5ML5ceGZ9tSw5mVs"
    )
}

locations = [
    ["-87.940267,41.946774", "-87.524044, 42.023131"],
    ["-87.862968,41.870391", "-87.524044,41.946774"],
    ["-87.862968,41.794034", "-87.524044,41.870391"],
    ["-87.862968,41.717677", "-87.524044,41.794034"],
    ["-87.862968,41.644335", "-87.524044,41.717677"]
]
