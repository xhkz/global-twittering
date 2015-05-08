__author__ = 'rongzuoliu'

import couchdb
from couchdb.mapping import ViewField


def map_reduce(dbname, view_name, reduce_field):

    server = couchdb.Server(url= "http://115.146.95.53:5984/")
    db = server[dbname]

    map_fun = '''
        function(doc) {
            if(doc.''' + reduce_field + ''') {
                for(i in doc.''' + reduce_field + ''') {
                    emit(doc.''' + reduce_field + '''[i], 1);
                }
            }
        }
    '''
    reduce_fun = '''
        function(key, values) {
            var sum = 0;
            for(var i=0; i < values.length; i++) {
                 sum += values[i];
            }
            return sum;
        }
    '''
    design = {
        'views': {
            view_name: {
                'map': map_fun,
                'reduce': reduce_fun
            }
        }
    }

    db['_design/' + view_name + 'View'] = design



if __name__ == "__main__":

    view_name = 'Hashtags'

    # todo: you should change the field name to what you want to reduce
    reduce_field = 'what.entities.hashtags'

    dbname = 'twitter_rest'
    map_reduce(dbname, view_name, reduce_field)



